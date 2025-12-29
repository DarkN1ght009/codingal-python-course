import math

board = ["" for _ in range(9)] 

def print_board():
    for i in range(0, 9, 3):
        print(board[i], "", board[i+1], "", board[i+2])
    print()

def check_winner(player):
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for pos in win_positions:
        if board[pos[0]] == board [pos[1]] == board [pos[2]] == player:
            return True
    return False

def is_draw():
    return ' ' not in board
#Minimax Algorithm
def minimax(is_maximizing): 
    if check_winner("0"):
        return 1 
    if check_winner("X"): 
        return -1
    if is_draw():
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(False)
                board[i] = ""
                best_score = max(score, best_score)
                return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(True)
                board[i] = ""
                best_score = min(score, best_score)
                return best_score


def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == "":
            board[i] = "0"
            score = minimax(False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i

    board[move] = "0"


print("You are X, AI is 0")
print_board()
while True:

    move = int(input("Enter your move (0-8): "))
    if board[move] != "":
        print("Invalid move!")
        continue
    board[move] = "X"
    print_board()
    if check_winner("X"):
        print("You win! 🏆")
        break

    if is_draw():
        print("It's a draw!")
        break
   
    ai_move()
    print("AI played:")
    print_board()
    if check_winner("O"):
        print("AI wins ")
        break