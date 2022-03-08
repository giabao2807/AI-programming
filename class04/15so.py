import random
from queue import PriorityQueue


def C_0(S):
    n = len(S)
    for i in range(n):
        for j in range(n):
            if S[i][j] == 0:
                return i, j

# O = 0: Up
# O = 1: Down
# O = 2: Left
# O = 3: Right


def move(S, O):
    n = len(S)
    L = [list(x) for x in S]
    i, j = C_0(S)
    if O == 0:
        if i < n-1:
            L[i][j] = L[i+1][j]
            L[i+1][j] = 0
            return tuple([tuple(x) for x in L])
        else:
            return None
    if O == 1:
        if i > 0:
            L[i][j] = L[i-1][j]
            L[i-1][j] = 0
            return tuple([tuple(x) for x in L])
        else:
            return None
    if O == 2:
        if j < n-1:
            L[i][j] = L[i][j+1]
            L[i][j+1] = 0
            return tuple([tuple(x) for x in L])
        else:
            return None
    if O == 3:
        if j > 0:
            L[i][j] = L[i][j-1]
            L[i][j-1] = 0
            return tuple([tuple(x) for x in L])
        else:
            return None


def distance(A, B):
    n = len(A)
    ans = 0
    for i in range(n):
        for j in range(n):
            if A[i][j] != 0 and A[i][j] != B[i][j]:
                ans += 1
    return ans


#Goal = ((1,2,3,4),(5,6,7,8),(9,10,11,12),(13,14,15,0))
Goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
Start = Goal
for _ in range(5000):
    i = random.choice(range(4))
    O = move(Start, i)
    if O != None:
        Start = O
for _ in Start:
    print(_)

# 1. Cho đỉnh xuất phát vào open.
Open = PriorityQueue()
Open.put(((0, 0, 0), Start, None, None))
Closed = {Start}

OK = False

count = 0
# 2. Nếu open rỗng thì tìm kiếm thất bại, kết thúc việc tìm kiếm.
# 6. Trở lại bước 2.
while not Open.empty():
    count += 1
    # 3. Lấy đỉnh đầu trong open ra và gọi đó là ʘ. Cho ʘ vào closed
    O_cha = Open.get()
    O = O_cha[1]
    # 4. Nếu ʘ là đỉnh đích thì tìm kiếm thành công, kết thúc việc tìm kiếm.
    if O == Goal:
        OK = True
        break
    # 5. Tìm tất cả các đỉnh con của ʘ không thuộc open và closed cho vào cuối của open
    for _ in range(4):
        child = move(O, _)
        if child != None and child not in Closed:
            g = O_cha[0][1]+1
            h = distance(child, Goal)
            f = g+h
            Open.put(((f, g, h), child, _, O_cha))
            Closed.add(child)
print(OK, count)


def Myprint(O_cha):
    if O_cha[2] != None:
        Myprint(O_cha[3])
        print(O_cha[2])
    for _ in O_cha[1]:
        print(_)


Myprint(O_cha)
