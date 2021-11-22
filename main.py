board = list(range(1, 10))


def welcome():
    print("Добро пожаловать в игру")
    print("    крестики-нолики!    ")
    print("   Для выигрыша вы должны")
    print("выстроить три крестика или ")
    print("нолика в ряд. Ходить пооче-")
    print("рёдно до победы, указывая ")
    print("номер поля согласно шаблону")
    print("ниже.")


def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-------------")


def turn_input(player_flag):
    while True:
        turn_value = input("Куда поставим " + player_flag + "? ")
        if not (turn_value.isdigit()):
            print("Символ не распознан, введите число")
            continue

        turn_value = int(turn_value)

        if 1 > turn_value or turn_value > 9:
            print("Значение не распознано. Введите число от 1 до 9.")
            continue

        if str(board[turn_value - 1]) in "XO":
            print("Эта клетка уже занята, введите номер другой клетки.")
            continue
        board[turn_value - 1] = player_flag
        print_board(board)
        return turn_value


def win_check(board):
    win_line = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for field in win_line:
        if board[field[0]] == board[field[1]] == board[field[2]]:
            print("Выиграл " + str(board[field[1]]) + "!")
            return board[field[1]]
    return False


def main(board):
    welcome()
    print_board(board)
    win = False
    turn_counter = 0
    while not win:
        if turn_counter % 2 == 0:
            turn_input("X")
        else:
            turn_input("0")
        turn_counter += 1
        if turn_counter > 4:
            tmp = win_check(board)
            if tmp:
                break
        if turn_counter == 9:
            print("Ничья!")
            break
    print_board(board)


main(board)

