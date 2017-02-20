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

## 树的存储结构模型
1. parent表示法
2. child表示法
3. child_sibling表示法
