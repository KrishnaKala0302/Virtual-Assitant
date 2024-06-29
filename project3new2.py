def analyseboard(board):
    c = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(0, 8):
        if board[c[i][0]] != 0 and board[c[i][0]] == board[c[i][1]] == board[c[i][2]]:
            return board[c[i][0]]
    return 0

def ConstBoard(board):
    print("The current state of the board:  \n\n")
    for i in range(0, 9):
        if i > 0 and i % 3 == 0:
            print("\n")
        if board[i] == 0:
            print("_ ", end=" ")
        elif board[i] == 1:
            print("O ", end=" ")
        elif board[i] == -1:
            print("X ", end=" ")
    print("\n")

def UserTurn1(board):
    while True:
        try:
            pos = int(input("Enter 'X' position [1-9]: "))
            if pos < 1 or pos > 9:
                print("Invalid move: Position must be between 1 and 9.")
                continue
            if board[pos - 1] != 0:
                print("Invalid move: Position already taken.")
                continue
            board[pos - 1] = -1
            break
        except ValueError:
            print("Invalid move: Please enter a number.")

def UserTurn2(board):
    while True:
        try:
            pos = int(input("Enter 'O' position [1-9]: "))
            if pos < 1 or pos > 9:
                print("Invalid move: Position must be between 1 and 9.")
                continue
            if board[pos - 1] != 0:
                print("Invalid move: Position already taken.")
                continue
            board[pos - 1] = 1
            break
        except ValueError:
            print("Invalid move: Please enter a number.")

def minmax(board,player):
    x=analyseboard(board)
    if(x!=0):
        return (x*player)
        pos=-1
        value=-2 
        for i in range(0,9):
            if(board[i]==0):
                board[i]=player
                score=-minmax(board,-player)
                board[i]=0
                if(score>value):
                    value=score
                    pos=i
        if(pos==-1):
         return 0
        return value


def CompTurn(board):
    pos = -1
    value = -2
    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            score = -minmax(board, -1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    if pos != -1:
        board[pos] = 1

# def CompTurn(board):
#     pos=-1
#     value=-2
#     for i in range(0,9):
#         if (board[i]==0):
#            board[i]=1
#            score= -minmax(board,-1)
#            board[i]=0
#            if(score>value):
#                 value=score
#                 pos=i

    # if(pos!=0):
    #  board[pos]=1

def main():
    choice = int(input("Enter 1 for Single player or 2 for Multiplayer: "))
    board = [0] * 9
    if choice == 1:
        print("Single player game")
        print("Computer 'O' vs You 'X': \n")
        player=int(input("Enter to play 1st('1') or 2nd('2'): "))
        for i in range(0,9):
            if(analyseboard(board)!=0):
                break
            if((i+player)%2==0):
                CompTurn(board)
            else:
                ConstBoard(board)
                UserTurn1(board)
        
    else:
        print("Multiplayer game")
        for i in range(0, 9):
            ConstBoard(board)
            if analyseboard(board) != 0:
                break
            if i % 2 == 0:
                UserTurn1(board)
            else:
                UserTurn2(board)

    ConstBoard(board)
    winner = analyseboard(board)
    if winner == 0:
        print("Draw")
    elif winner == -1:
        print("Player 1 (X) has won!")
    else:
        print("Player 2 (O) has won!")

if __name__ == "__main__":
    main()
