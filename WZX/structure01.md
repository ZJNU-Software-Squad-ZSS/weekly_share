#### ArrayList：
- 优点：操作读取操作效率高，基于数组实现的，可以为null值，可以允许重复元素，有序，异步。
- 缺点：由于它是由动态数组实现的，不适合频繁的对元素的插入和删除操作，因为每次插入和删除都需  要移动数组中的元素。
![](https://raw.githubusercontent.com/bananahab/text/master/docs/%E7%AC%AC%E4%B9%9D%E5%91%A8%E4%BD%9C%E4%B8%9A/image/03.png?token=AKNGWSMLYAFZ2BFXGSVHR3S5X3DWK)

#### LinkedList：
- 优点：LinkedList由双链表实现，增删由于不需要移动底层数组数据，其底层是链表实现的，只需要修改链表节点指针，对元素的插入和删除效率较高。
- 缺点： 遍历效率较低。HashMap和双链表也有关系。
![](https://raw.githubusercontent.com/bananahab/text/master/docs/%E7%AC%AC%E4%B9%9D%E5%91%A8%E4%BD%9C%E4%B8%9A/image/04.png?token=AKNGWSODH6VYLBEKXCX5ZMC5X3FWQ)

#### HashMap:
- HashMap实际上是一个"链表散列"的数据结构,即数组和链表的结合体。
- 数组中的每一项又是一个链表,当新建一个HashMap时,就会初始化一个数组。
![](https://raw.githubusercontent.com/bananahab/text/master/docs/%E7%AC%AC%E4%B9%9D%E5%91%A8%E4%BD%9C%E4%B8%9A/image/05.png?token=AKNGWSK52LKK35IOQK3HENK5X3FDM)

#### Set：
- set是一个内部自动有序且不含重复元素的容器。
- set集合容器实现了红黑树（Red-Black Tree）的平衡二叉检索树的数据结构，在插入元素时，它会自动调整二叉树的排列，把该元素放到适当的位置，以确保每个子树根节点的键值大于左子树所有节点的键值，而小于右子树所有节点的键值。另外，还得确保根节点左子树的高度与右子树的高度相等，这样，二叉树的高度最小，从而检索速度最快。要注意的是，它不会重复插入相同键值的元素，而采取忽略处理。如图是一个典型的红黑树。
![](https://raw.githubusercontent.com/bananahab/text/master/docs/%E7%AC%AC%E4%B9%9D%E5%91%A8%E4%BD%9C%E4%B8%9A/image/06.png?token=AKNGWSPY6RPNH5GLLEDCOIK5X3EP4)