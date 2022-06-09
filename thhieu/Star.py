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
                print("Path Doesn't Exist")
                return None

            if n == stop:
                reconst_tour = []
                while(par[n] != n):
                    reconst_tour.append(n)
                    n = par[n]

                reconst_tour.append(start)
                reconst_tour.reverse()

                print('Path found is as follows:')
                for i in reconst_tour[:-1]:
                    print(i, end="->")
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
        print('tour does not exist!')
        return None


if __name__ == '__main__':
    g = {
        'S': [('A', 6), ('B', 5), ('C', 10)],
        'A': [('S', 6), ('E', 10)],
        'B': [('S', 5), ('E', 6), ('D', 7)],
        'C': [('S', 10), ('D', 6)],
        'D': [('C', 6), ('B', 7), ('F', 10)],
        'E': [('A', 6), ('B', 6), ('F', 4)],
        'F': [('E', 4), ('D', 6), ('G', 3)]
    }
    heur = {
        'A': 10,
        'B': 13,
        'C': 4,
        'D': 2,
        'E': 4,
        'F': 1,
        'G': 0
    }
    gr = Graph(g)
    gr.set_heuristic(heur)
    gr.a_star(start='S', stop='G')