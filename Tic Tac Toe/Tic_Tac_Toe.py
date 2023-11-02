# Tic-Tac-Toe 
def print_board(board, light_mode=True):
    if light_mode:
        cell_separator = ' | '
        horizontal_line = '-' * 9
    else:
        cell_separator = ' │ '
        horizontal_line = '─' * 9

    for row in board:
        print(cell_separator.join(row))
        print(horizontal_line)

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

def toggle_mode(current_mode):
    return not current_mode

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    light_mode = True  # Initialize with light mode

    while True:
        print_board(board, light_mode)
        print("Toggle Mode: 1 for Light Mode, 2 for Dark Mode")
        mode_choice = input("Enter your choice: ")

        if mode_choice == '1':
            light_mode = True
        elif mode_choice == '2':
            light_mode = False
        elif mode_choice.lower() == 'quit':
            print("Exiting the game.")
            break
        else:
            row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

            if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
                print("Invalid move! Try again.")
                continue

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board, light_mode)
                print(f"Player {current_player} wins!")
                break
            elif is_full(board):
                print_board(board, light_mode)
                print("It's a tie!")
                break

            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
