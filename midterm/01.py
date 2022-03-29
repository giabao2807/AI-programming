vertexes = ["a", "b", "c", "d", "e", "f"]
edges = [("a", "d"), ("a", "f"),
         ("b", "c"),
         ("c", "c"), ("c", "e"), ("c", "d"),
         ("d", "f")]

start = "a"
goal = "b"
open = [(start, None)]
closed = {start}
while open:
    O_TT = open.pop(-1)
    O = O_TT[0]
    if O == goal:
        OK = True
        break
    for p1, p2 in [x for x in edges if x[0] == O or x[1] == O]:
        child = p2 if p1 == O else p1
        if child not in closed:
            open.append((child, O_TT))
            closed.add(child)
else:
    OK = False


def MyPrint(O_TT):
    if O_TT != None:
        MyPrint(O_TT[-1])
        print(O_TT[0], end=' ' if O_TT[0] != goal else '\n')


if OK:
    MyPrint(O_TT)
else:
    print('Khong tim thay duong di')
