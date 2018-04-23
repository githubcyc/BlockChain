from django.http import HttpResponseBadRequest
from django.shortcuts import render,HttpResponse
from uuid import uuid4
import json
from BlockApp.core.Blockchain import Blockchain
from BlockApp.core.myutils import data_prettified

node_identifier = str(uuid4()).replace("-", "")
# Instantiate the Blockchain
blockchain = Blockchain()


def mine(request):
    last_block = blockchain.last_block
    last_proof = last_block["proof"]
    proof = blockchain.proof_of_work(last_proof)
    print(proof)
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )
    # Forge the new Block by adding it to the chain
    block = blockchain.new_block(proof)
    response = {
        "message": "New Block Forged",
        "index": block["index"],
        "transactions": block["transactions"],
        "proof": block["proof"],
        "previous_hash": block["previous_hash"],
    }
    print(response)
    return HttpResponse(data_prettified(response))


def new_transaction(request):
    values = {
        "sender": "0",
        "recipient": "d5ead01f6f2f4dc6b0ad0ec74778205b",
        "amount": 5
    }
    # values = json.dumps(values)
    required = ["sender", "recipient", "amount"]
    if not all(k in values for k in required):
        return "Missing values"
    index = blockchain.new_transaction(values["sender"], values["recipient"], values["amount"])
    print(index)
    response = {"message": "Transaction will be added to Block %s"% index}
    return HttpResponse(data_prettified(response))


def full_chain(request):
    response = {
        "chain": blockchain.chain,
        "length": len(blockchain.chain),
    }
    return HttpResponse(data_prettified(response))

def register_nodes(request):
    # request.POST.get()
    print(request.body)
    # values = json.loads(request.body.decode('utf-8'))
    # python3
    # request.META.get('CONTENT_TYPE', '').lower() == 'application/json'
    if  len(request.body) > 0:
        try:
            values = json.loads(request.body.decode('utf-8'))
        except Exception as e:
            return HttpResponseBadRequest(data_prettified({'error': 'Invalid request: {0}'.format(str(e))}),
                                          content_type="application/json")
    nodes = values.get('node')
    print(nodes)
    # ['http:127.0.0.1:8000']
    if nodes is None:
        return "Error: Please supply a valid list of nodes"
    for node in nodes:
        print(node)
        blockchain.register_node(node)
    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    print(blockchain.nodes)
    return HttpResponse(data_prettified(response))

def consensus(request):
    replaced = blockchain.resolve_conflicts()
    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }
    return HttpResponse(data_prettified(response))
