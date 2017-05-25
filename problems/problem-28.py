import time


class direction():
    RIGHT = [0, 1]
    LEFT = [0, -1]
    DOWN = [1, 0]
    UP = [-1, 0]


def turn_right(d):
    if d == direction.RIGHT:
        return  direction.DOWN
    elif d == direction.DOWN:
        return direction.LEFT
    elif d == direction.LEFT:
        return direction.UP
    elif d == direction.UP:
        return direction.RIGHT
    elif d is None:
        return direction.RIGHT

if __name__=="__main__":
    start = time.time()
    height, width = 1001, 1001
    spiral = [[0 for row in range(width)] for col in range(height)]
    offset_x, offset_y = 0, 0
    n = 1
    row, col = int(height / 2), int(width / 2)
    x = row + offset_x
    y = col + offset_y
    spiral[x][y] = n
    print("x = {0}, y = {1}, n = {2}".format(x, y, n))
    current_d = None
    next_d = None
    while True:
        if n == height * width:
            break
        #print("x = {0}, y = {1}, n = {2}".format(x, y, n))
        n += 1
        if width > x >= 0 and height > y >= 0:
            # check if we can go right, if yes
            next_d = turn_right(current_d)
            if spiral[x + next_d[0]][y + next_d[1]] == 0:
                x += next_d[0]
                y += next_d[1]
                current_d = next_d
            # if no
            else:
                x += current_d[0]
                y += current_d[1]
        spiral[x][y] = n
    diagonal_sum = 0
    for row in range(height):
        #for col in range(width):
        #   print(" {} ".format(spiral[row][col]), end='')
        diagonal_sum += spiral[row][row] + spiral[row][width - row - 1]
        #print("\n")
    # subtract origin as we added that twice in the loop above
    diagonal_sum -= spiral[int(height / 2)][int(width / 2)]
    print("diagonal sum = {}".format(diagonal_sum))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))