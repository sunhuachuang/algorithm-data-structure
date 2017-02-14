# 模拟链式的列表
import ctypes

# 单向链表
class SingleNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def car(self):
        return self.value

    def cdr(self):
        return self.next

    # only for remember
    def cadr(self):
        return self.next

    def __repr__(self):
        return 'value: ' + str(self.value) + ', next id is ' + str(self.next)

class SingleLinkedList:
    def __init__(self, first_value=None):
        if first_value:
            first_node = SingleNode(first_value, None)
            self.head_node = SingleNode('', first_node)
        else:
            self.head_node = SingleNode('', None)

    def __repr__(self):
        tmp_node = self.head_node
        count = 0
        while tmp_node.cdr():
            count += 1
            # tmp_node = ctypes.cast(tmp_node.cdr(), ctypes.py_object).value # core dumped
            tmp_node = tmp_node.cdr()
            print(tmp_node)
        return 'count length: ' + str(count)

# test
single_linked_list = SingleLinkedList('a')
print(single_linked_list)

# 双向链表
