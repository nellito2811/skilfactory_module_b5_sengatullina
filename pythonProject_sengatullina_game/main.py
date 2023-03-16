board = [['-'] * 3 for _ in range(3)]

print('Добро пожаловать в игру "Крестики нолики"!')

def draw_board(f):
    print('  0 1 2')
    for i in range(len(board)):
        print(str(i), *board[i])

def users_step(f):
    while True:
        place = input('Введите координаты через пробел: ').split()
        if len(place) != 2:
            print('Введите две координаты.')
            continue
        if not (place[0].isdigit() and place[1].isdigit()):
            print('Введите числа.')
            continue
        x, y = map(int, place)
        if not (x >= 0 and x < 3 and y >= 0 and y < 3):
            print('Вышли из диапазона')
            continue
        if f[x][y] != '-':
            print('Клетка занята')
            continue
        break
    return x, y


def check_win(f, user):
    def chek_line(a1, a2, a3, user):
        if a1 == user and a2 == user and a3 == user:
            return True
        return False

    for i in range(3):
        if chek_line(f[i][0], f[i][1], f[i][2], user) or \
            chek_line(f[0][i], f[1][i], f[2][i], user) or \
            chek_line(f[0][0], f[1][1], f[2][2], user) or \
                chek_line(f[2][0], f[1][1], f[0][2], user):
            return True
    return False

count = 0

while True:
    if count % 2 == 0:
        user = 'x'
    else:
        user = '0'
    draw_board(board)
    if count < 9:
        x, y = users_step(board)
        board[x][y] = user
    if count == 9 and not check_win(board, user):
        print('Ничья')
        break
    if check_win(board, user):
        print(f"Выйграл: {user}")
        draw_board(board)
        break
    count += 1
