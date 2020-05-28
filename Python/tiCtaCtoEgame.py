count=0
winC={"X":0,"O":0,"Tie:":0}
board = [" " for x in range(9)]

def printBoard():
    for x in range(0,7,3):
        print("{}|{}|{}".format(board[x],board[x+1],board[x+2]))

def checkBoard():
    if((board[0]==board[4] and board[4]==board[8])or(board[2]==board[4] and board[4]==board[6])):
            return board[4]
    for x in range(0,7,3):
        if(board[x]==board[x+1] and board[x+1]==board[x+2]):
            return board[x]
    for x in range(0,3):
        if(board[x]==board[x+3] and board[x+3]==board[x+6]):
            return board[x]
    return 0    

def fillBoard():
    global count
    while True:
        a=0
        a = input("Enter board position to fill(1-9): ").strip()
        if(a.isdigit()):
            a=int(a)
            if(a in range(1,10) and board[a-1]==" "):
                board[a-1]="X" if (count%2==0) else "O"
                count+=1
                break
            elif(a in range(1,10) and board[a-1]!=" "):
                print("{} is filled".format(a))
        else:
            print("Invalid Entry")
            
def logicFlow():
    global board,count
    board = [" " for x in range(9)]
    count=0
    while True:
        printBoard()
        bc=checkBoard()
        if(bc== 'X' or bc== 'O'):
            print("{} Wins :)".format(bc))
            winC[bc]+=1
            break
        elif(count==9):
            print("Its a TIE xD")
            winC[Tie]+=1
            break
        fillBoard()


def Results():
    print("Number of Games {0} won = {1}".format("X",winC['X']))
    print("Number of Games {0} won = {1}".format("O",winC['O']))
    print("Number of Games Tie = {0}".format(winC['Tie']))
    

while True:
    logicFlow()
    cont=(input("Do u want to continue?(y/n)").strip()).lower()
    while(cont != 'y' and cont != 'n'):
        print("Invalid Entry")
        cont=(input("Do u want to continue?(y/n)").strip()).lower()
    if(cont=='y'):
        continue
    else:
        Results()
        break
            
      
