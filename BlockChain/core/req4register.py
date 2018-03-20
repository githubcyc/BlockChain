import requests,json
import fire

def register(url, node_url):
    # url = "http://127.0.0.1:8000"
    pay_load = {
        "node" : [node_url]
    }
    url = url+'/register'
    print(pay_load['node'])
    # post data must be json string
    req = requests.post(url, data=json.dumps(pay_load))
    print(req.status_code)
    print(req.json())

# python3 req4register.py http://127.0.0.1:8000 http://127.0.0.1:8001


if __name__ == '__main__':
    fire.Fire(register)