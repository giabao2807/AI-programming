def Check(O):
    if O[0] > 0 and O[0] < O[1]:
        return False
    if O[3] > 0 and O[3] < O[4]:
        return False
    return True


def Children(O):
    res = []
    # 1. 2 nguoi qua song
    if O[2] == 0:
        if O[0] >= 2:
            child = [O[0]-2, O[1], 1, O[3]+2, O[4]]
            if Check(child):
                res.append(child)
    else:
        if O[3] >= 2:
            child = [O[0]+2, O[1], 0, O[3]-2, O[4]]
            if Check(child):
                res.append(child)
    # 2. 2 quy qua song
    if O[2] == 0:
        if O[1] >= 2:
            child = [O[0], O[1]-2, 1, O[3], O[4]+2]
            if Check(child):
                res.append(child)
    else:
        if O[4] >= 2:
            child = [O[0], O[1]+2, 0, O[3], O[4]-2]
            if Check(child):
                res.append(child)

    # 3. 1 nguoi qua song
    if O[2] == 0:
        if O[0] >= 1:
            child = [O[0]-1, O[1], 1, O[3]+1, O[4]]
            if Check(child):
                res.append(child)
    else:
        if O[3] >= 1:
            child = [O[0]+1, O[1], 0, O[3]-1, O[4]]
            if Check(child):
                res.append(child)

    # 4. 1 quy qua song
    if O[2] == 0:
        if O[1] >= 1:
            child = [O[0], O[1]-1, 1, O[3], O[4]+1]
            if Check(child):
                res.append(child)
    else:
        if O[4] >= 1:
            child = [O[0], O[1]+1, 0, O[3], O[4]-1]
            if Check(child):
                res.append(child)

    # 5. 1 nguoi 1 quy qua song
    if O[2] == 0:
        if O[0] >= 1 and O[1] >= 1:
            child = [O[0]-1, O[1]-1, 1, O[3]+1, O[4]+1]
            if Check(child):
                res.append(child)
    else:
        if O[3] >= 1 and O[4] >= 1:
            child = [O[0]+1, O[1]+1, 0, O[3]-1, O[4]-1]
            if Check(child):
                res.append(child)

    return res


# Số người ở trái, Số quỷ bên trái, vị trí thuyền, Người bên phải, Quỷ bên phải
Start = [3, 3, 0, 0, 0]
Goal = [0, 0, 1, 3, 3]

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
