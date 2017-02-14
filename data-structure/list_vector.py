# 模拟连续空间的列表
class VectorList:
    max_size = 0
    stores = {}

    def __init__(self, max_size, *values):
        self.max_size = max_size
        self.stores = { key: value for key, value in enumerate(values) }

    def get_key(self, value):
        for key, value in self.stores.items():
            if value == value:
                return key

    def get_value(self, key):
        if key >= 0 and key < self.max_size:
            return self.stores[key]

    def len(self):
        return len(self.stores)

    def add_element(self, value, set_key=None):
        if set_key == None and self.len() < self.max_size - 1:
            self.stores[self.len()] = value

        elif set_key >= 0 and set_key < self.max_size and self.len() < (self.max_size - 1):
            for i in range(self.len(), set_key, -1):
                self.stores[i] = self.stores[i-1]

            self.stores[set_key] = value

    def del_element(self, del_key):
        if del_key >= 0 and del_key < (self.len() - 1):
            for i in range(del_key, self.len() - 1):
                self.stores[i] = self.stores[i+1]

            del self.stores[self.len() - 1]

    def __repr__(self):
        for key, value in self.stores.items():
            print(key, ': ', value)

        return 'len_size: ' + str(self.len())


# test
vector_list = VectorList(10, 'a', 'b', 'c')
print(vector_list.len())
print(vector_list.get_key('a'))
print(vector_list.get_value(1))

vector_list.add_element('d')
print(vector_list.len())

vector_list.add_element('bbb', 1)
print(vector_list)

vector_list.del_element(1)
print(vector_list)
