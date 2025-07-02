board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))

def game():
    turn = 'X'
    for _ in range(9):
        print_board()
        move = int(input(f"Enter position (0-8) for {turn}: "))
        if board[move] == ' ':
            board[move] = turn
            turn = 'O' if turn == 'X' else 'X'
    print_board()

game()
