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
        #exit_game()
    else:
        print('Invalid choice, please try again.')
        main_menu()

def start_game():
    table = [['0' for _ in range(8)] for _ in range(8)]

def exit_game():
    print('Game exited.')
    raise SystemExit

if __name__ == "__main__":
    main()