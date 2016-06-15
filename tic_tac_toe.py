#Tic Tac Toe
#Jonathan Light
#Practice with Python

from sys import exit
import random

gameOver = False

class player():
    
    player_name = ''
    player_team = ''
    
    def __init__(self, name, team):
        self.player_name = name
        self.player_team = team
    
    
    def setTeam(self, string):
        self.player_team = string
    
    def getTeam(self):
        return self.player_team
    
    def setName(self,string):
        self.player_name = string
        
    def getName(self):
        return self.player_name
        
class computer():
    #TODO
    pass

def main():
    
    ready = ''
    #multiplayer = 'n'
    
    print("Hello! Welcome to Tic Tac Toe!")    
    print("In this game you will play against the computer.")
    print("Are you ready to start? (y/n):")
    
    ready = input()
    
    if ready.lower() == 'n':
        exit()
        
    elif ready.lower() == 'y':
        print("Great!")
        newGame()
        
    else:
        print("Not quite sure what you meant by that...")
        exit()
    
def newGame():
    
    player1 = player("Player 1","X")
    player2 = player("Player 2","O")
    board = ['.'] +[' '] * 9
    
    print("Player 1 is 'X', Player 2 is 'O'")
    
    if random.randint(1,2) == 1:
        print("%s goes first this time!" % player1.getName())
        gameLoop(board, player1, player2)
    
    else:
        print("%s goes first this time!" % player2.getName())
        gameLoop(board, player2, player1)
    

def markBoard(board, player, placement):
    board[placement] = player.getTeam()
    
def move(board, player):
        
        print("Enter 1-9 to place your mark on the board.")
        
        userInput = input()
        
        if isinstance(userInput,int):
            if 0 < userInput and userInput < 10:
                if board[userInput] == ' ':
                    board[userInput] = player.player_team
                    #return board
                else:
                    print("This spot is already taken. Try again...")
                    move(board,player)
            else:
                print("Please a number 1 through 9 inclusive...")
                move(board,player)
        else:
            print("Please enter an integer...")
            move(board,player)

def printBoard(board):
    
    print("")
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print("")
    
def checkForWinner(board, player):
    global gameOver
    team = player.getTeam()
    if not ' ' in board:
        print("Looks like theres no more places to go! Tie game!!")
        gameOver = True
        return
    if ((board[1] == team and board[4] == team and board[7] == team) or #first column
    (board[2] == team and board[5] == team and board[8] == team) or #second column 
    (board[3] == team and board[6] == team and board[9] == team) or #third column
    (board[1] == team and board[2] == team and board[3] == team) or
    (board[4] == team and board[5] == team and board[6] == team) or
    (board[7] == team and board[8] == team and board[9] == team) or
    (board[1] == team and board[5] == team and board[9] == team) or
    (board[7] == team and board[5] == team and board[3] == team)):
        print("%s wins!!" %player.getName())
        gameOver = True
    
    #TODO: Other conditions to win
        
def gameLoop(board, player1, player2):
    global gameOver
    while not gameOver:
        printBoard(board)
        move(board,player1)
        checkForWinner(board, player1)
        printBoard(board)
        move(board, player2)
        checkForWinner(board, player2)
    

if __name__ == "__main__":
    main()
