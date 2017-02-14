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

    def set_cdr(self, value):
        self.next = value

    # only for remember
    def cadr(self):
        return self.next

    def __repr__(self):
        return 'value: ' + str(self.value)

class SingleLinkedList:
    def __init__(self, first_value=None):
        if first_value:
            first_node = SingleNode(first_value, None)
            self.head_node = SingleNode('', first_node)
        else:
            self.head_node = SingleNode('', None)

    # O(n) 第n个元素， 从1开始计数
    def get_element(self, n):
        if n > 1:
            tmp_node = self.head_node
            i = 0
            while tmp_node.cdr() and i < n:
                tmp_node = tmp_node.cdr()
                i += 1
            if tmp_node and n == i:
                return tmp_node
        else:
            return self.head_node.cdr()

    # O(n) 第n个元素， 从1开始计数
    def add_element(self, value, n=None):
        add_node = SingleNode(value, None)
        tmp_node = self.head_node

        i = 1
        while True:
            if i == n or not tmp_node.cdr():
                add_node.set_cdr(tmp_node.cdr())
                tmp_node.set_cdr(add_node)
                break
            else:
                tmp_node = tmp_node.cdr()
                i += 1

    # O(n) 第n个元素， 从1开始计数
    def del_element(self, n):
        tmp_node = self.head_node
        i = 1
        while i < n and tmp_node.cdr():
            tmp_node = tmp_node.cdr()
            if i+1 == n:
                if tmp_node.cdr():
                    del_node = tmp_node.cdr()
                    tmp_node.set_cdr(del_node.cdr())
                    del del_node
                break
            i += 1

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
single_linked_list.add_element('b')
print(single_linked_list)
single_linked_list.add_element('c')
single_linked_list.add_element('aa', 1)
single_linked_list.add_element('zz', 4)
single_linked_list.add_element('last', 100)
print(single_linked_list)
single_linked_list.del_element(2)
single_linked_list.del_element(100)
print(single_linked_list)


# 双向链表
