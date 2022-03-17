import random
from queue import PriorityQueue
# Trò chơi 8 số


def ToadoZero(S):
  n = len(S)
  for i in range(n):
    for j in range(n):
      if S[i][j] == 0:
        return i, j

# o = 0 : Up
# o = 1 : Down
# o = 2 : Left
# o = 3 : Right


def move(S, o):
  n = len(S)
  L = [list(x) for x in S]
  i, j = ToadoZero(S)
  if o == 0:
    if i < n-1:
      L[i][j] = L[i+1][j]
      L[i+1][j] = 0
      return tuple([tuple(x) for x in L])
  elif o == 1:
    if i > 0:
      L[i][j] = L[i-1][j]
      L[i-1][j] = 0
      return tuple([tuple(x) for x in L])
  elif o == 2:
    if j < n-1:
      L[i][j] = L[i][j+1]
      L[i][j+1] = 0
      return tuple([tuple(x) for x in L])
  elif o == 3:
    if j > 0:
      L[i][j] = L[i][j-1]
      L[i][j-1] = 0
      return tuple([tuple(x) for x in L])
  return None


def distance(S, G):
  ans = 0
  n = len(S)
  for i in range(n):
    for j in range(n):
      if S[i][j] != G[i][j]:
        ans += 1
  return ans


#Goal = ((1,2,3),(4,5,6),(7,8,0))
Goal = ((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 0))
#Goal = tuple([tuple([(i*5 + j+1)%25 for j in range(5)]) for i in range(5)])
print(Goal)
Start = Goal
for _ in range(50000):
  O = move(Start, random.randint(0, 3))
  if O != None:
    Start = O

for _ in Start:
  print(_)

OK = False
count = 0
# 1.Cho đỉnh xuất phát vào open.
Open = PriorityQueue()
Open.put(((0, 0), Start, None, None))
Closed = {Start}
# 2. Nếu open rỗng thì tìm kiếm thất bại, kết thúc việc tìm kiếm.
# 6. Trở lại bước 2.
while not Open.empty():
  count += 1
  # 3. Lấy đỉnh đầu trong open ra và gọi đó là ʘ. Cho ʘ vào closed
  O_TT = Open.get()
  O = O_TT[1]
  # 4. Nếu ʘ là đỉnh đích thì tìm kiếm thành công, kết thúc việc tìm kiếm.
  if O == Goal:
    OK = True
    break
  # 5. Tìm tất cả các đỉnh con của ʘ không thuộc open và closed cho vào cuối của open
  for i in range(4):
    child = move(O, i)
    if child != None and child not in Closed:
      g = O_TT[0][1] + 1
      h = distance(child, Goal)
      f = g + h
      Open.put(((h, g), child, i, O_TT))
      Closed.add(child)


def MyPrint(O_TT):
  if O_TT[3] != None:
    MyPrint(O_TT[3])
    print(O_TT[2])
  for _ in O_TT[1]:
    print(_)


MyPrint(O_TT)
print(OK, count)
