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

**工作量证明**

新的区块依赖工作量证明算法（PoW）来构造。PoW的目标是找出一个符合特定条件的数字， 这个数字很难计算出来，但容易验证 。这就是工作量证明的核心思想。
