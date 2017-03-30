# Diejkstra 迪杰斯特拉 最短路径算法
#

def mini_path_dijkstra(graph):
    pass

if __name__ == '__main__':
    from adjacency_matrix import AdjacencyMatrix
    test = AdjacencyMatrix(False, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I')
    test.insert_arc('A', 'B', 10)
    test.insert_arc('A', 'F', 11)
    test.insert_arc('B', 'G', 16)
    test.insert_arc('F', 'G', 17)
    test.insert_arc('E', 'F', 26)
    test.insert_arc('E', 'H', 7)
    test.insert_arc('D', 'E', 20)
    test.insert_arc('D', 'H', 16)
    test.insert_arc('G', 'H', 19)
    test.insert_arc('D', 'G', 24)
    test.insert_arc('D', 'I', 21)
    test.insert_arc('C', 'D', 22)
    test.insert_arc('C', 'I', 8)
    test.insert_arc('B', 'C', 18)
    test.insert_arc('B', 'I', 12)

    mini_path_dijkstra(test)
