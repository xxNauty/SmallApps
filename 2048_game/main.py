import logic

def pretty_print_mat(mat):
    longest_num = len(str(max((num for row in mat for num in row),key=lambda n: len(str(n)))))
    for row in mat:
        print("[", end="")
        iteration = 0
        for num in row:
            diff_in_length = longest_num - len(str(num))
            print("0" * diff_in_length + str(num), end="")
            if iteration != 3:
                print(",", end="")
            iteration += 1
        print("]")

if __name__ == '__main__':
    mat = logic.start_game()

while True:
    x = input("Press the command : ")

    if x == 'W' or x == 'w':
        mat, flag = logic.move_up(mat)
        status = logic.get_current_state(mat)
        print(status)

        if status == 'GAME NOT OVER':
            logic.add_new_2(mat)
        else:
            pretty_print_mat(mat)
            break

    elif x == 'S' or x == 's':
        mat, flag = logic.move_down(mat)
        status = logic.get_current_state(mat)
        print(status)

        if status == 'GAME NOT OVER':
            logic.add_new_2(mat)
        else:
            pretty_print_mat(mat)
            break

    elif x == 'A' or x == 'a':
        mat, flag = logic.move_left(mat)
        status = logic.get_current_state(mat)
        print(status)

        if status == 'GAME NOT OVER':
            logic.add_new_2(mat)
        else:
            pretty_print_mat(mat)
            break

    elif x == 'D' or x == 'd':
        mat, flag = logic.move_right(mat)
        status = logic.get_current_state(mat)
        print(status)

        if status == 'GAME NOT OVER':
            logic.add_new_2(mat)
        else:
            pretty_print_mat(mat)
            break
    else:
        print("Invalid Key Pressed")

    pretty_print_mat(mat)
