import backend.board_transformations as board_transformations

def start_game():
    mat = []
    for _ in range(4):
        mat.append([0] * 4)

    print("Commands are as follows : ")
    print("'W' or '↑' : Move Up")
    print("'S' or '↓' : Move Down")
    print("'A' or '←' : Move Left")
    print("'D' or '→' : Move Right")

    board_transformations.add_new_2(mat)
    return mat