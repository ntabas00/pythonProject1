board = [

    [14, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 3, 0, 11, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 13, 0, 2, 11, 15, 9, 0, 0, 0],
    [0, 0, 0, 13, 0, 0, 2, 9, 0, 0, 7, 1, 14, 15, 5, 0],
    [1, 0, 10, 0, 0, 11, 0, 5, 9, 0, 0, 4, 0, 0, 0, 0],
    [9, 0, 0, 0, 0, 12, 0, 14, 7, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 0, 7, 1, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 9, 1, 0, 12, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 8, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 11, 13, 0, 0, 0, 4, 3, 0],
    [0, 16, 0, 0, 0, 0, 0, 12, 2, 0, 0, 0, 0, 14, 0, 0],
    [13, 0, 14, 5, 0, 0, 0, 0, 0, 0, 0, 9, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0],
    [0, 0, 5, 0, 0, 15, 0, 2, 1, 7, 0, 14, 0, 3, 13, 0],
    [0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 13, 9, 0, 0, 0, 0, 0, 0, 0, 4, 12, 0, 0, 0, 0],
    [12, 2, 0, 0, 1, 0, 4, 0, 5, 0, 0, 0, 16, 6, 0, 11]

]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 17):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 4
    box_y = pos[0] // 4

    for i in range(box_y * 4, box_y * 4 + 4):
        for j in range(box_x * 4, box_x * 4 + 4):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 4 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - - - - - -- - - - - ")

        for j in range(len(bo[0])):
            if j % 4 == 0 and j != 0:
                print(" | ", end="")

            if j == 15:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


print_board(board)
solve(board)
print("__________________________________________________________________________")
print_board(board)
