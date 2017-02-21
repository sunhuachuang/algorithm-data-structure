# 树 Tree
*相关概念*

1. Root(根结点)
1. SubTree(子树)
1. n >= 0(结点)
1. m > 0(其余结点组成的互不相交的有限集合)
1. Degree (度): 结点拥有的子树的个数，称为结点的度
1. Leaf (叶结点， 终端结点): degree为0的结点
1. 非终端结点或分支结点: degree不为0
1. 除了根结点外， 其他分支结点称为内部结点
1. 树的度(Tree Degree): 树内各个结点中的度的最大值
1. Child (结点的子树的根结点， 就是结点紧挨着的下面的结点， 称为该结点的Child)
1. Parent (相应的该结点称为下面child的Parent)
1. Sibling (兄弟结点, parent 的其他 child)
1. 结点的祖先是从root到parent的所有结点, 反之从该点开始下面的所有结点都是该点的子孙
1. Level (结点的层次) root 为 第一层, 同层不一样parent的结点互为堂兄弟
1. Depth (深度或者高度) tree's max level
1. 有序树和无序树, 所有子树从左到右是否都不能互换
1. Forest (森林) m >= 0 互不相交的 tree, 对每个结点而言, 其子树的集合就是一个forest

## 树的抽象数据模型
1. [base tree](https://github.com/sunhuachuang/algorithm-data-structure/blob/master/data-structure/tree/base.py)
2. [binary tree 二叉树](https://github.com/sunhuachuang/algorithm-data-structure/blob/master/data-structure/tree/binary.py)

### 二叉树
二叉树: 每个结点只能有一个或者两个子结点, 而且是有序的左子树和右子树, 即使只有一颗子树, 也要区分左右子树
#### 特殊的二叉树:
1. **斜树**: 每个结点只有左子树, 称为左斜树, 同理, 右斜树.
  1. *结点个数等于树的深度 (类似线性表)*
2. **满二叉树**: 所有分支结点都有左右子树, 而且所有叶子都在同一层.
  1. *同样深度的二叉树中, 满二叉树结点个数最多*
3. **完全二叉树**: n个结点按层排序, 如果编号i(n >= i >=0)的结点与同样深度的满二叉树中编号为i的结点在二叉树中的位置完全相同.
  1. *叶子结点只能出现在最下面两层*
  2. *最下层的叶子集中在左边连续位置*
  3. *倒数第二层若有叶子结点, 必然在右边连续位置*
  4. *如果该结点的度为1, 则只有左结点*
  5. *同样个数的二叉树, 完全二叉树的深度最小*

#### 二叉树的性质
1. 在i层最多有 ```2^(i-1)``` 个结点
1. 深度为k的二叉树, 最多有 ```2^k - 1``` 个结点
1. 任何二叉树, 终端结点数为n0, 度为2的结点数为n2, 则 ```n0 = n2 + 1```, 由 ```n=n0+n1+n2``` 与 ```n-1=n1+2n2```线总数, 可以推出
1. 具有n个结点的完全二叉树的深度为 ```floor(log n) + 1 = ceil(log n)``` 参照```2^k - 1```
1. n个结点的完全二叉树, 按层序号, 第i个结点:
  1. i = 1 则i是root, i>1, 则双亲结点是i/2
  2. 如果 2i > n, 则结点i无左子树(i为叶子结点), 否则左子树是结点2i
  3. 如果 2i + 1 > n, 则结点i无右子树, 否则右子树是结点 2i+1

#### 二叉树的存储结构模型
1. 完全二叉树的顺序存储结构, 按层序号排列好的.
1. [二叉树二叉链表 三叉链表](https://github.com/sunhuachuang/algorithm-data-structure/blob/master/data-structure/tree/binary.py)

## 树的存储结构模型
1. parent表示法
2. child表示法
3. child_sibling表示法
