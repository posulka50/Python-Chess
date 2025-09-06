def main():
    main_menu()


def main_menu():
    print('Welcome to the Main Menu')
    print('1. Start Game')
    print('2. Exit')
    choice = input('Please select an option: ')
    if choice == '1':
        start_game()
    elif choice == '2':
        print('Exiting the game. Goodbye!')
        exit_game()
    else:
        print('Invalid choice, please try again.')
        main_menu()


def validate_coordinates(x, y):
    if 0 <= x < 8 and 0 <= y < 8:
        return True
    return False

def letter_to_number(letter):
    letters = 'abcdefgh'
    if letter in letters:
        return letters.index(letter)
    return -1


def init_board():
    board = [['0' for _ in range(9)] for _ in range(9)]
    return board


def print_board(board):
    for row in board:
        print(' '.join(row))


def start_game():
    board = init_board()
    print_board(board)
    game_loop()


def select_figure():
    while True:
        print('Select a figure:')


def game_loop():
    while True:
        command = input('Enter command (move/exit): ')


def exit_game():
    print('Game exited.')
    raise SystemExit


if __name__ == "__main__":
    main()
    select_figure()
