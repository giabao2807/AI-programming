from pickle import FALSE


def DFS(initialState, goal):
    frontier = [initialState]
    explored = []
    while frontier:
        state = frontier.pop(len(frontier)-1)
        explored.append(state)
        if goal == state:
            return explored
        for neighbor in graph[state]:
            if neighbor not in (explored and frontier):
                frontier.append(neighbor)
    return FALSE

if __name__ == '__main__':
    graph = {
        # 'A': ['B','C'],
        # 'B': ['D','E'],
        # 'C': ['F','J'],
        # 'D': ['H','I'],
        # 'E': ['J','K'],
        # 'F': ['L','M'],
        # 'G': ['N','O'],
        # 'H': [],
        # 'I': [],
        # 'J': [],
        # 'K': [],
        # 'L': [],
        # 'M': [],
        # 'N': [],
        # 'O': []

        'S' : ['A','B','C'],
        'A' : ['D'],
        'B' : ['D','E','G'],
        'C' : ['E'],
        'D' : ['F'],
        'E' : ['F','H'],
        'F' : ['E','G'],
        'G' : ['F','H'],
        'H' : ['E','G']
    }
    result = DFS('S','G')
    if result:
        s = 'explored: '
        for i in result:
            s += i + ' '
            print(s)
    else:
        print('404 Not Found')