from collections import deque


class Graph:
    def __init__(self, graph) -> None:
        self.graph = graph

    def get_neighbours(self, v):
        return self.graph[v]

    def set_heuristic(self, h):
        self.heuristic = h

    def heuristic_val(self, n):
        return self.heuristic[n]

    def a_star(self, start, stop):
        open_list = set([start])
        closed_list = set([])

        tour = {}
        tour[start] = 0

        par = {}
        par[start] = start

        while(len(open_list) > 0):
            n = None
            for v in open_list:
                if n == None or tour[v]+self.heuristic_val(v) < tour[n]+self.heuristic_val(n):
                    n = v

            if n == None:
                print("Không có đường đi")
                return None

            if n == stop:
                reconst_tour = []
                while(par[n] != n):
                    reconst_tour.append(n)
                    n = par[n]

                reconst_tour.append(start)
                reconst_tour.reverse()

                print('Đường đi cuối cùng:')
                for i in reconst_tour[:-1]:
                    print(i, end="=>")
                print(reconst_tour[-1])
                return reconst_tour

            for (m, weight) in self.get_neighbours(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    par[m] = n
                    tour[m] = tour[n]+weight
                else:
                    if tour[m] > tour[n]+weight:
                        tour[m] = tour[n]+weight
                        par[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            open_list.remove(n)
            closed_list.add(n)
            print(closed_list)
        print('Không tồn tại đường đi')
        return None


if __name__ == '__main__':
    g = {
        'S': [('A', 5), ('B', 6), ('C', 5)],
        'A': [('S', 6), ('D', 6), ('E', 7)],
        'B': [('S', 6), ('F', 3), ('G', 4)],
        'C': [('S', 5), ('H', 6), ('K', 4)],
        'D': [('A', 6), ('M', 5), ('N', 8)],
        'E': [('A', 7), ('I', 8)],
        'F': [('B', 3), ('J', 4), ('L', 4)],
        'G': [('B', 4)],
        'H': [('C', 6)],
        'K': [('C', 4), ('Z', 2)],
        'M': [('D', 5)],
        'N': [('D', 8)],
        'I': [('E', 8)],
        'J': [('F', 4)],
        'L': [('F', 4)],
        'Z': [('K', 2)]
    }
    heur = {
        'S': 10,
        'A': 9,
        'B': 8,
        'C': 7,
        'D': 6,
        'E': 5,
        'F': 4,
        'G': 10,
        'H': 10,
        'K': 3,
        'M': 0,
        'N': 10,
        'I': 6,
        'J': 0,
        'L': 9,
        'Z': 8
    }
    gr = Graph(g)
    gr.set_heuristic(heur)
    print("=============================")
    print("Thứ tự khám phá đường đi S=>M: ")
    gr.a_star(start='S', stop='M')
    print("=============================")
    print("Thứ tự khám phá đường đi S=>J: ")
    gr.a_star(start='S', stop='J')
