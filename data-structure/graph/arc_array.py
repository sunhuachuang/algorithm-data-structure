# arc Array 边集数组
class Vertex:
    store = []
    def __init__(self, *value):
        self.store = list(value)

class ArcNode:
    def __init__(self, weight,  tail, head):
        self.weight = weight
        self.tail = tail
        self.head = head

class Arc:
    store = []
    def __init__(self, *arc_nodes):
        self.store = list(arc_nodes)
