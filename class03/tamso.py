import random


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
    L = [list(x) for x in S]
    i, j = C_0(S)
    if O == 0:
        if i < 2:
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
        if j < 2:
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


Goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
Start = Goal
for _ in range(10000):
    i = random.choice(range(4))
    O = move(Start, i)
    if O != None:
        Start = O
for _ in Start:
    print(_)

# 1. Cho đỉnh xuất phát vào open.
Open = [(Start, None, None)]
Closed = {Start}

OK = False

# 2. Nếu open rỗng thì tìm kiếm thất bại, kết thúc việc tìm kiếm.
# 6. Trở lại bước 2.
while len(Open) > 0:
    # 3. Lấy đỉnh đầu trong open ra và gọi đó là ʘ. Cho ʘ vào closed
    O_cha = Open.pop(0)
    O = O_cha[0]
    # 4. Nếu ʘ là đỉnh đích thì tìm kiếm thành công, kết thúc việc tìm kiếm.
    if O == Goal:
        OK = True
        break
    # 5. Tìm tất cả các đỉnh con của ʘ không thuộc open và closed cho vào cuối của open
    for _ in range(4):
        child = move(O, _)
        if child != None and child not in Closed:
            Open.append((child, _, O_cha))
            Closed.add(child)

print(OK)


def Myprint(O_cha):
    if O_cha[2] != None:
        Myprint(O_cha[2])
        print(O_cha[1])
    for _ in O_cha[0]:
        print(_)


Myprint(O_cha)
