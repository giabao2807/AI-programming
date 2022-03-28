# uniform cost search

from queue import PriorityQueue
V = ["a", "b", "c", "d", "e", "f"]
E = [("a", "b", 3), ("a", "f", 5), ("a", "d", 4),
     ("b", "c", 1), ("b", "f", 1),
     ("c", "d", 2),
     ("d", "b", 3),
     ("e", "d", 3), ("e", "f", 2),
     ("f", "d", 2)]


def child(O):
    child = []
    for i in E:
        if i[0] == O:
            child.append((i[1], i[2]))
    return child


Start = "a"
Goal = "f"

Open = PriorityQueue()
Open.put((0, Start, None))
Closed = {Start}

OK = False

while not Open.empty():
    O_cha = Open.get()
    O = O_cha[1]
    if O == Goal:
        OK = True
        break

    for ch in child(O):
        if ch != None and ch not in Closed:
            Open.put((ch[1], ch[0], O_cha))
            Closed.add(ch[1])


print(OK)
print(O_cha)
