# depth first search
# adjacency matrix

class AdjacencyMatrix:
    directed = False # is or not directed
    vertex = []
    arc = []
    def __init__(self, directed, *args):
        self.directed = directed
        number = len(args)
        self.vertex = list(args)
        self.arc = [[None for _ in range(number)] for _ in range(number)]

    def insert_arc(self, v1, v2, weight):
        index1 = self.vertex.index(v1)
        index2 = self.vertex.index(v2)
        self.arc[index1][index2] = weight

        if not self.directed:
            self.arc[index2][index1] = weight

    def has_arc(self, k1, k2):
        return self.arc[k1][k2]

    def get_number(self):
        return len(self.vertex)

    def get_vertex_value(self, key):
        return self.vertex[key]


def depth_first_search(graph, i):
    global vertex_visited
    vertex_visited[i] = True
    print(graph.get_vertex_value(i))

    for j in range(graph.get_number()):
        if graph.has_arc(i, j) and not vertex_visited[j]:
            depth_first_search(graph, j)

def depth_first_search_traverse(graph):
    global vertex_visited
    for i in range(graph.get_number()):
        if not vertex_visited[i]:
            depth_first_search(graph, i)


test = AdjacencyMatrix(False, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I')
test.insert_arc('A', 'B', 1)
test.insert_arc('A', 'F', 1)
test.insert_arc('B', 'G', 1)
test.insert_arc('F', 'G', 1)
test.insert_arc('E', 'F', 1)
test.insert_arc('E', 'H', 1)
test.insert_arc('D', 'E', 1)
test.insert_arc('D', 'H', 1)
test.insert_arc('G', 'H', 1)
test.insert_arc('D', 'G', 1)
test.insert_arc('D', 'I', 1)
test.insert_arc('C', 'D', 1)
test.insert_arc('C', 'I', 1)
test.insert_arc('B', 'C', 1)
test.insert_arc('B', 'I', 1)

vertex_visited = [False] * test.get_number()
depth_first_search_traverse(test)
