# 二叉链表
class TwoBinaryNode:
    def __init__(self, data, left_child, right_child):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

# 三叉链表
class ThreeBinaryNode:
    def __init__(self, data, left_child, right_child, parent):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent
