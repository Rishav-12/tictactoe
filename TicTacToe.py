def available(pos, board):
    if board[pos] == ' ':
        return True
    else:
        return False

def showBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print("-+-+-")
    print(board[3] + '|' + board[4] + '|' + board[5])
    print("-+-+-")
    print(board[6] + '|' + board[7] + '|' + board[8])
    print("\n")
    print("******************************")

def check_win(board):
    for i in range(0, 7, 3):
        if not available(i, board) and board[i] == board[i+1] and board[i] == board[i+2]:
            return True
    for i in range(3):
        if not available(i, board) and board[i] == board[i+3] and board[i] == board[i+6]:
            return True
    if not available(0, board) and board[0] == board[4] and board[0] == board[8]:
        return True
    if not available(2, board) and board[2] == board[4] and board[2] == board[6]:
        return True

def game():
    running = True
    valid_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while running:
        
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ans = ''
        total_moves = 0
        
        print("1|2|3")
        print("-+-+-")
        print("4|5|6")
        print("-+-+-")
        print("7|8|9")
        
        print("\nLet's play. X goes first.\n")
        
        player = 'X'
        
        while True:
            user_input = input(f"Player ({player}) choose your position: (1-9): ")
            
            if user_input.isdigit():
                pos = int(user_input)
            else:
                print("Please enter a valid position")
                continue
            if pos not in valid_positions:
                print("Please enter a valid position (1-9)")
                continue
            
            if available(pos-1, board): #Check if the desired position is available
                board[pos-1] = player
                showBoard(board) #Display the board after every valid move
                if check_win(board): #Check if the current player has won
                    print("\nGame Over")
                    print(f"***Player ({player}) wins.***")
                    break
                total_moves += 1
                if total_moves == 9: #If all 9 squares are covered, it's a tie
                    print("\nGame Over")
                    print("***Tie***")
                    break
            else:
                print("Position is already occupied")
                continue
            
            # Switching the players
            if player == 'X':
                player = 'O'
            elif player == 'O':
                player = 'X'
        
        print("Do you want to play again? [Y]es No[Any Button]")
        ans = input().lower()
        if ans == 'y':
            continue
        else:
            running = False

if __name__ == "__main__":
    game()
