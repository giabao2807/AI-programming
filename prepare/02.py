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


Start = "c"
Goal = "e"
count = 0
Open = PriorityQueue()
Open.put((0, Start, None))
Closed = {Start}

OK = False

while not Open.empty():
    count += 1
    O_cha = Open.get()
    O = O_cha[1]
    if O == Goal:
        OK = True
        break

    for ch in child(O):
        print(ch)
        if ch != None and ch not in Closed:
            Open.put((ch[1], ch[0], O_cha))
            Closed.add(ch[1])
    if len(E) == count:
        break


def Myprint(O_cha):
    if O_cha[2] != None:
        Myprint(O_cha[2])
        print(O_cha[1])
#   for _ in O_cha[1]: print(_)


print(OK)

if not OK:
    print("Ko co duong di")
else:
    print(Start)
    Myprint(O_cha)
