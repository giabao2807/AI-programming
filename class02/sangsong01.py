# Bài tập: Viết chương trình tìm cách đưa 3 người và 3 quỷ sang sông!!!

def check(child):
    if child[0] == child[1]:
        return True
    if child[0] == 0 or child[0] == 3:
        return True
    return False


def Children(O):
    ans = []
    # Trường hợp đưa 1 người và 1 quỷ qua sông
    if O[0] >= 1 and O[1] >= 1:
        child = [4-O[0], 4-O[1], 1-O[2]]
        if check(child):
            ans.append(child)
    # Trường hợp đưa 2 người
    if O[0] >= 2:
        child = [5-O[0], 3-O[1], 1-O[2]]
        if check(child):
            ans.append(child)
    # Trường hợp đưa 2 quỷ qua sông
    if O[1] >= 2:
        child = [3-O[0], 5-O[1], 1-O[2]]
        if check(child):
            ans.append(child)
    # Trường hợp đưa 1 người
    if O[0] >= 1:
        child = [4-O[0], 3-O[1], 1-O[2]]
        if check(child):
            ans.append(child)
    # Trường hợp đưa 2 quỷ qua sông
    if O[1] >= 1:
        child = [3-O[0], 4-O[1], 1-O[2]]
        if check(child):
            ans.append(child)
    return ans


# [Số người ở phía thuyền, Số quỷ ở phía thuyền, vị trí thuyền]
Start = [3, 3, 0]
Goal = [3, 3, 1]


OK = False

# 1.Cho đỉnh xuất phát vào open.
Open = [Start]
Closed = []
# 2. Nếu open rỗng thì tìm kiếm thất bại, kết thúc việc tìm kiếm.
# 6. Trở lại bước 2.
while len(Open) > 0:
    # 3. Lấy đỉnh đầu trong open ra và gọi đó là ʘ. Cho ʘ vào closed
    O = Open.pop(0)

    Closed.append(O)
    # 4. Nếu ʘ là đỉnh đích thì tìm kiếm thành công, kết thúc việc tìm kiếm.
    if O == Goal:
        OK = True
        break
    # 5. Tìm tất cả các đỉnh con của ʘ không thuộc open và closed cho vào cuối của open
    for child in Children(O):
        if child not in Open and child not in Closed:
            Open.append(child)


print(OK)
