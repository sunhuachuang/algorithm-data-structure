# Adjacency List
# one is array to store vertex, another is list to store arc
def get_next_arc(arc):
    if arc.next_arc:
        return get_next_arc(arc.next_arc)
    return arc

def print_list_arc(arc, root):
    if arc.next_arc:
        print_list_arc(arc.next_arc, root)
    print(root.value, ' -> ', arc.to_vertex.value, ' : ', arc.weight)

class VertexNode:
    def __init__(self, value, first_arc=None):
        self.value = value
        self.first_arc = first_arc

    def add_arc(self, arc):
        if self.first_arc:
            self.get_last_arc().set_next_arc(arc)
        else:
            self.first_arc = arc

    def get_last_arc(self):
        return get_next_arc(self.first_arc)

    def __repr__(self):
        if not self.first_arc:
            return self.value + ': None'
        print_list_arc(self.first_arc, self)
        return ''

class ArcNode:
    to_vertex = None
    weight = 0
    next_arc = None

    def __init__(self, weight, to_vertex):
        self.weight = weight
        self.to_vertex = to_vertex

    def set_next_arc(self, arc):
        self.next_arc = arc

class AdjacencyList:
    directed = False
    vertex = []
    def __init__(self, directed, *args):
        self.directed = directed
        self.vertex = list(args)

    def add_vertex(self, vertex):
        self.vertex.append(vertex)

    def add_arc(self, v1, v2, weight):
        arc = ArcNode(weight, v2)
        v1.add_arc(arc)

        if not self.directed:
            arc2 = ArcNode(weight, v1)
            v2.add_arc(arc2)

    def __repr__(self):
        print('----------')
        for i in self.vertex:
            print(i)
        return '---------'


a = VertexNode('A')
b = VertexNode('B')
c = VertexNode('C')
d = VertexNode('D')

test = AdjacencyList(False, a, b, c, d)
test.add_arc(a, b, 1)
test.add_arc(a, c, 2)
test.add_arc(c, b, 3)
test.add_arc(d, b, 4)
print(test)

a = VertexNode('A')
b = VertexNode('B')
c = VertexNode('C')
d = VertexNode('D')
test2 = AdjacencyList(True, a, b, c, d)
test2.add_arc(a, b, 1)
test2.add_arc(a, c, 2)
test2.add_arc(c, b, 3)
test2.add_arc(d, b, 4)
print(test2)
