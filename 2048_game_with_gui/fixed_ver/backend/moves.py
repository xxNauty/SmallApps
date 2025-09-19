import backend.board_transformations as board_transformations

def move_left(grid):
    new_grid, changed1 = board_transformations.compress(grid)
    new_grid, changed2 = board_transformations.merge(new_grid)
    changed = changed1 or changed2
    new_grid, temp = board_transformations.compress(new_grid)

    return new_grid, changed

def move_right(grid):
    new_grid = board_transformations.reverse(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = board_transformations.reverse(new_grid)

    return new_grid, changed

def move_up(grid):
    new_grid = board_transformations.transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = board_transformations.transpose(new_grid)

    return new_grid, changed

def move_down(grid):
    new_grid = board_transformations.transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = board_transformations.transpose(new_grid)

    return new_grid, changed