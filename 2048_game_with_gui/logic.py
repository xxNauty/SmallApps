import random

def start_game():
    mat = []
    for _ in range(4):
        mat.append([0] * 4)

    print("Commands are as follows : ")
    print("'W' or '↑' : Move Up")
    print("'S' or '↓' : Move Down")
    print("'A' or '←' : Move Left")
    print("'D' or '→' : Move Right")

    add_new_2(mat)
    return mat

def find_empty(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return i, j
    return None, None

def add_new_2(mat):
    if all(all(cell != 0 for cell in row) for row in mat):
        return

    tries = 0
    while tries < 30:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
        if mat[r][c] == 0:
            mat[r][c] = 2
            return
        tries += 1

    r, c = find_empty(mat)
    if r is not None and c is not None:
        mat[r][c] = 2

def get_current_state(mat):
    max = 0
    for i in range(4):
        for j in range(4):
            field_val = mat[i][j]
            if field_val > max:
                max = field_val
            if field_val == 2048:
                return 'WON', max

    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER', None

    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return 'GAME NOT OVER', None

    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return 'GAME NOT OVER', None

    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return 'GAME NOT OVER', None

    return 'LOST', max

def compress(mat):
    changed = False

    new_mat = []
    for _ in range(4):
        new_mat.append([0] * 4)

    for i in range(4):
        pos = 0

        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1

    return new_mat, changed

def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
                changed = True

    return mat, changed

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3 - j])

    return new_mat

def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])

    return new_mat


def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, temp = compress(new_grid)

    return new_grid, changed

def move_right(grid):
    new_grid = reverse(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = reverse(new_grid)

    return new_grid, changed

def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose(new_grid)

    return new_grid, changed

def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose(new_grid)

    return new_grid, changed