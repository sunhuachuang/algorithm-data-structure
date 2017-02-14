# 连续空间的列表
class ListVector:
    max_size = 0
    stores = {}

    def __init__(self, max_size, *values):
        self.max_size = max_size
        self.stores = { key: value for key, value in enumerate(values) }

    def get_key(self, value):
        for key, value in self.stores.items():
            if value == value:
                return key

    def len(self):
        return len(self.stores)

    def get_value(self, key):
        if key >= 0 and key < self.max_size:
            return self.stores[key]

    def add_element(self, value, set_key=None):
        if set_key >= 0 and set_key < self.max_size and self.len() < (self.max_size - 1):
            tmp_stores = self.stores
            for key, value in self.stores.items():
                if key > set_key:
                    self.stores[key+1] = tmp_stores[key]
            self.stores[key] = value

    def del_element(self, del_key):
        if del_key >= 0 and del_key < (self.len() - 1):
            tmp_stores = self.stores
            for key, value in self.stores.items():
                if key >= del_key:
                    self.stores[key] = tmp_stores[key+1]
            del self.stores[self.len() - 1]
