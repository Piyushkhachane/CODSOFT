# TASK-2 TIC-TAC-TOE AI

import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

def evaluate(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return 10 if row[0] == 'O' else -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return 10 if board[0][col] == 'O' else -10

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return 10 if board[0][0] == 'O' else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return 10 if board[0][2] == 'O' else -10

    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score

    if not is_moves_left(board):
        return 0

    if is_max:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'O'  
                    best_score = max(best_score, minimax(board, depth + 1, False))
                    board[i][j] = " " 
        return best_score

    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'X'  
                    best_score = min(best_score, minimax(board, depth + 1, True))
                    board[i][j] = " "  
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'O'  
                move_score = minimax(board, 0, False)
                board[i][j] = " "  
                if move_score > best_score:
                    best_move = (i, j)
                    best_score = move_score

    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while is_moves_left(board) and evaluate(board) == 0:
        while True:
            try:
                player_move = int(input("Enter your move (1-9): ")) - 1
                row, col = divmod(player_move, 3)
                if board[row][col] == " ":
                    board[row][col] = 'X'
                    break
                else:
                    print("That cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 1 and 9.")

        print("Your move:")
        print_board(board)

        if evaluate(board) != 0 or not is_moves_left(board):

            break

        print("Computer is making a move...")
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = 'O'

        print("Computer's move:")
        print_board(board)

    final_score = evaluate(board)
    if final_score == 10:
        print("Computer wins! Better luck next time.")
    elif final_score == -10:
        print("Congratulations! You win!")
    else:
        print("It's a tie!")

if __name__ == "__main__": 
    main()
    