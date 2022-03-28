
from cmath import inf
from tracemalloc import start, stop
import numpy as np
import random

# tạo bàn cờ


def create_empty_board():
    return np.zeros((10, 10))

# kiểm tra danh sách rỗng


def possibilities(board):

    a = np.nonzero(board == 0)

    a = list(zip(*a))

    return a


def all_line(board):
    board = np.copy(board)
    rs = []
    for i in range(board.shape[0]):
        rs.append(board[i])
    for i in range(board.shape[1]):
        rs.append(board[:, i])
    for i in range(board.shape[0]):
        j = min((board.shape[0], board.shape[1], board.shape[0]-i))
        rs.append(board[np.arange(i, i+j), np.arange(j)])
        rs.append(board[board.shape[0]-np.arange(i, i+j) -
                  1, board.shape[1]-np.arange(j)-1])
    for i in range(1, board.shape[1]):
        j = min((board.shape[0], board.shape[1], board.shape[1]-i))
        rs.append(board[np.arange(j), np.arange(i, i+j)])
        rs.append(board[board.shape[0]-np.arange(j)-1,
                  board.shape[1]-np.arange(i, i+j)-1])
    return rs


def win(board: np.ndarray, player):
    board = board == player
    # row win
    for i in range(board.shape[0]):
        count = 0
        for j in range(board.shape[1]):
            if board[i, j]:
                count += 1
            else:
                if count == 5:
                    return True
                count = 0
        if count >= 5:
            return True

    # col win
    for i in range(board.shape[1]):
        count = 0
        for j in range(board.shape[0]):
            if board[j, i]:
                count += 1
            else:
                if count == 5:
                    return True
                count = 0
        if count == 5:
            return True
    # diag win song song voi cheo chinh
    for i in range(board.shape[0]):
        count = 0
        for j in range(0, min((board.shape[0], board.shape[1], board.shape[0]-i))):
            x = i + j
            y = j

            if board[x, y]:
                count += 1
            else:
                if count == 5:
                    return True
                count = 0
        if count == 5:
            return True

    for i in range(board.shape[0]):
        count = 0
        for j in range(0, min((board.shape[0], board.shape[1], board.shape[0]-i))):
            x = i + j
            y = j
            x = board.shape[0]-x-1
            y = board.shape[1]-y-1

            if board[x, y]:
                count += 1
            else:
                if count == 5:
                    return True
                count = 0
        if count == 5:
            return True

    for i in range(1, board.shape[1]):
        count = 0
        for j in range(0, min((board.shape[0], board.shape[1], board.shape[1]-i))):
            y = i + j
            x = j
            if board[x, y]:
                count += 1

            else:
                if count == 5:
                    return True
                count = 0

        if count == 5:
            return True

    for i in range(1, board.shape[1]):
        count = 0
        for j in range(0, min((board.shape[0], board.shape[1], board.shape[1]-i))):
            y = i + j
            x = j
            x = board.shape[0]-x-1

            y = board.shape[1] - y-1

            if board[x, y]:
                count += 1

            else:
                if count == 5:
                    return True
                count = 0

        if count == 5:
            return True
    return False

# danh gia thang thua hoa


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if win(board, player):
            winner = player

    if np.all(board != 0) and winner == 0:
        winner = -1

    return winner


PC, HUMAN = 1, 2

# tinh gia tri ban co doi voi PC


def score_for_line(line, player):
    dic = {}
    dic = {1: 10, 2: 100, 3: 1000, 4: 5000}
    s = 0
    i = 0
    while i < len(line):
        if line[i] == player:
            start_ = i
            while i < len(line):
                if line[i] != player:
                    stop = i
                    break
                i += 1
            else:
                stop = i
            w = 0
            if start_ != 0 and line[start_-1] != 3-player:
                w += 0.5
            if stop != len(line) and line[stop] != 3-player:
                w += 0.5
            s += dic[stop-start_]*w
        i += 1
    return s


def score(board, player):

  
    return sum([score_for_line(line, player) for line in all_line(board)])


def value(board):
    v = evaluate(board)
    if v == PC:

        return 1000000
    elif v == HUMAN:
        return -1000000
    else:

        return score(board, PC) - score(board, HUMAN)


def minimax(board, depth, player, alpha=float('-inf'), beta=float('inf')):

    if depth == 0 or evaluate(board) != 0:
        return board, value(board)
    pos = possibilities(board)
    if np.all(board == 0):
        pos = [(random.randint(0, board.shape[0]-1),
                random.randint(0, board.shape[1]-1))]
    else:
        pos = [x for x in pos if np.any(board[np.amax((0, x[0]-2)):np.amin(
            (x[0]+2, board.shape[0])), np.amax((0, x[1]-2)):np.amin((board.shape[1], x[1]+2))])]
    if player == PC:
        max, bmax = float('-inf'), 1

        for x, y in pos:
            child = board.copy()
            child[x, y] = player

            b, v = minimax(child, depth-1, HUMAN, alpha, beta)
            if max <= v:
                bmax, max = child, v
            alpha = np.amax((alpha, max))
            if beta <= alpha:
                break
        return bmax, max
    else:
        min, bmin = float('inf'), 1
        for x, y in pos:
            child = board.copy()
            child[x, y] = player
            b, v = minimax(child, depth-1, PC, alpha, beta)
            if min >= v:
                bmin, min = child, v
            alpha = np.amin((min, beta))

            if beta <= alpha:
                break
        return bmin, min


# lựa chọn nước đi sử dụng minimax
def minimax_place(board):
    b, v = minimax(board, 2, PC)
    return b

# chọn thủ công


def hand_place(board, player):
    selection = possibilities(board)
    i, j = map(int, input().split())
    if (i, j) in selection:
        board[i, j] = player
    return(board)


# Main function to start the game
def play_game():
    board, winner, counter = create_empty_board(), 0, 1
    print(board)

    while winner == 0:
        for player in [1, 2]:
            if player == PC:
                print("PC move")
                board = minimax_place(board)
            else:
                print("you move")
                board = hand_place(board, player)

            print(board)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    return(winner)


# Driver Code
print("Winner is: " + str(play_game()))
