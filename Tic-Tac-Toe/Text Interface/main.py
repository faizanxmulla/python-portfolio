def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_X_turn = True

    print("Welcome to Tic Tac Toe !!!")

    while True:
        print_board(board)
        if player_X_turn:
            print("Player X's turn")
        else:
            print("Player O's turn")

        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue

        if player_X_turn:
            board[row][col] = 'X'
            if check_winner(board, 'X'):
                print_board(board)
                print("Player X wins!")
                break
        else:
            board[row][col] = 'O'
            if check_winner(board, 'O'):
                print_board(board)
                print("Player O wins!")
                break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player_X_turn = not player_X_turn

    print("Thanks for playing !!")

if __name__ == "__main__":
    main()
