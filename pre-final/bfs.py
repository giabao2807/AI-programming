vertexes = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
edges = [('S', 'A'), ('S', 'B'),
         ('S', 'C'), ('A', 'D'),
         ('A', 'B'), ('B', 'C'),
         ('B', 'G'), ('B', 'F'),
         ('C', 'F'), ('D', 'E'),
         ('E', 'G'), ('F', 'H'),
         ('H', 'G'), ('E', 'F'),
         ('B', 'D')]

# best first search


START = 'S'
END = 'G'
open = [START]
closed = []
path = {}
count = 0
is_found = False
while(len(open) > 0):
    count += 1
    O = open.pop(0)
    closed.append(O)
    if O == END:
        is_found = True
        break
    for edge in edges:
        if O in edge:
            next = edge[0] if O == edge[1] else edge[1]
            if next not in open and next not in closed:
                path[next] = O
                open.append(next)

if is_found:
    v = END
    arr = [v]
    while path.get(v):
        v = path[v]
        arr.append(v)
    arr.reverse()
    print(*arr)
else:
    print("Khong tim thay duong di")
