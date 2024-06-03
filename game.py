field = [[0, 1, 2, 3],
         [1, '-', '-', '-'],
         [2, '-', '-', '-'],
         [3, '-', '-', '-']]


def step_processing(counter_step):
    if counter_step % 2 == 0:
        gamer = 'x'
    else:
        gamer = 'o'
    try:
        try:
            coordinate_x = int(input(f"Игрок {gamer}, введи поле хода 'X':"))
            coordinate_y = int(input(f"Игрок {gamer}, введи поле хода 'Y':"))

            if (coordinate_x == 0
                    or coordinate_y == 0
                    or field[coordinate_x][coordinate_y] != '-'):
                print('Game Error, введено неверное значение, повторите ввод')
                step_processing(counter_step)
            else:
                if counter_step % 2 == 0:
                    field[coordinate_x][coordinate_y] = 'x'
                elif counter_step % 2 == 1:
                    field[coordinate_x][coordinate_y] = 'o'
        except ValueError:
            print('Game Error, введено неверное значение, повторите ввод')
            step_processing(counter_step)
    except IndexError:
        print('Game Error, введено неверное значение, повторите ввод')
        step_processing(counter_step)



def gameplay():
    for counter_step in range(9):
        if counter_step == 0:
            print('Game start')
        else:
            print('Game in!')

        print('\n', *field[0], '\n', *field[1], '\n', *field[2], '\n', *field[3], sep='  ')
        step_processing(counter_step)
        if win_check():
            if counter_step % 2 == 0:
                gamer = "x"
            else:
                gamer = "o"
            print('\n', *field[0], '\n', *field[1], '\n', *field[2], '\n', *field[3], sep='  ')
            print('Gamer', gamer, 'win!')
            break



def win_check():
    win = [[field[1][1], field[1][2], field[1][3]],
           [field[2][1], field[2][2], field[2][3]],
           [field[3][1], field[3][2], field[3][3]],
           [field[1][1], field[2][1], field[3][1]],
           [field[1][2], field[2][2], field[3][2]],
           [field[1][3], field[2][3], field[3][3]],
           [field[1][1], field[2][2], field[3][3]],
           [field[1][3], field[2][2], field[3][1]]]
    for l in win:
        if l == ['x', 'x', 'x'] or l == ['o', 'o', 'o']:
            return True


gameplay()