# BlockChain 
## How to run
* initial project
```angular2html
python manage.py makemigrations
python manage.py migrate
# input admin info
# admin/django123
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:8000
# make a new mining node, just run django with a diffrent port(like 8001) 
```
* route 
```text
127.0.0.1:8000/mine
~/transactions/new/
~/chain/
~/register
~/resolve

```
##区块链应用实例

区块链是由区块的记录构成的不可变、有序的链结构，记录可以是交易、文件或任何你想要的数据，重要的是它们是通过哈希值（hashes）链接起来的。

**块结构**

每个区块包含属性：索引（index），Unix时间戳（timestamp），交易列表（transactions），工作量证明（稍后解释）以及前一个区块的Hash值。

以下是一个区块的结构：

	block = {
  		'index': 1,
  		'timestamp': 1521018683.336017
  		'transactions': [
    		{
      		'sender': "88e18b5ae365934f8af145de4a0acc40",
      		'recipient': "353ec73348254c42bc9d54ab8ee898ff",
      		'amount': 1,
    		}
  		],
  		'proof': 1,
  		'previous_hash': "2304dd1298ea0c4e0e7dc12c29ee7cbe7f161e5c1fa5c76e21c17754"
}

**POW**

新的区块依赖工作量证明算法（PoW）来构造。PoW的目标是找出一个符合特定条件的数字， 这个数字很难计算出来，但容易验证 。这就是工作量证明的核心思想。

## Reference
* **[Blockchain App](http://mp.weixin.qq.com/s/fwlKewtWWlct6wdaVcbezg)**

* [Learn Blockchains by Building One](https://learnblockchain.cn/2017/10/27/build_blockchain_by_python/)

* [zhihu](https://zhuanlan.zhihu.com/p/33710384)

* [Flask Version](https://github.com/silasiebert/learn-blockchains-by-building-one)