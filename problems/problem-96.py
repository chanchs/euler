# Ref https://euler.stephan-brumme.com/96/

import lib.utilities as ut
import math
import time

board = []


def solve(board):
    empty = 0
    row = len(board)
    col = len(board[0])

    for y in range(row):
        for x in range(col):
            if board[x][y] != empty:
                continue
            #           [  0   ,  1 ,  2   ,  3 ,   4  ,  5 ,  6  ,   7 ,   8 ,  9  ]
            available = [False, True, True, True, True, True, True, True, True, True]

            for i in range(row):
                if board[i][y] != empty:
                    available[board[i][y]] = False
                if board[x][i] != empty:
                    available[board[x][i]] = False
            rx = (x // 3) * 3
            ry = (y // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[i + rx][j + ry] != empty:
                        available[board[i + rx][j + ry]] = False

            for i in range(1, row + 1):
                if available[i]:
                    board[x][y] = i
                    if solve(board):
                        return True
            board[x][y] = empty
            return False
    return True


if __name__ == '__main__':
    start = time.time()
    count = 0
    brd = []
    sum = 0
    with open("problem-96.txt") as f:
        for line in f:
            if "Grid" not in line:
                r = []
                for c in line:
                    if c != '\n':
                        r.append(int(c))
                brd.append(r)
    for brd_num in range(0, 50):
        board = brd[9 * brd_num + 0:9 * brd_num + 9][0:9]
        print(board)
        solve(board)
        print(board)
        print(board[0][0], board[0][1], board[0][2])
        sum += 100 * board[0][0] + 10 * board[0][1] + board[0][2]
        print("running sum = {}".format(sum))
    print("Final sum = {}".format(sum))

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))