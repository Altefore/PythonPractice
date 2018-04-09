#Jonathan Light
#Hangman game
#hangman.py
#3/26/18
#this game will hopefully get me some practice with python, as well as incorporate a study 
#topic (undetermined) to prepare me for interviews

#body parts that will end up being used in the game
global head 
global shoulders
global leftArm
global rightArm
global torso
global leftLeg
global rightLeg
global livesLeft
global guessArray
global clueArray

def main():
  print("Start\n")
  menu()


def saveWordOrLetter(wordInput):
  wordInput = wordInput.upper()
  savedWord = ""
  acceptedCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
  for c in wordInput:
    if acceptedCharacters.find(c) != -1:
      savedWord += c
  return savedWord


def menu():
  menuInput = "NULL"
  print("Welcome to hangman!\n")
  while(menuInput != 0):
    print "MENU\n"
    print("1 : Single Player\n")
    print("2 : Multiplayer\n")
    print("3 : How To Play\n")
    print("0 : Exit Game\n")
    menuInput = input("Input : ")

    if menuInput == 1:
      singlePlayerGame()

    elif menuInput == 2:
      multiPlayerGame()

    elif menuInput == 3:
      printRules()

    elif menuInput == 0:
      print("Thanks For Playing!!\n")

    else:
      print("Please give a valid input.\n")

def singlePlayerGame():
  print("Sorry, but single player is currently disabled.\n")
  #single player menu
  #pull from csv file wordInput
  #grid
  #player guesses until dead or won

def multiPlayerGame():
#player1 wordInput
  global livesLeft
  global puzzle
  global guessArray
  global gameOver
  livesLeft = 7
  gameOver = False
  guessArray = ""

  try:
    wordInput = raw_input("Player 1 Input : ")
    puzzle = saveWordOrLetter(wordInput)
    for i in range(0,30):
      print ""
 
  except:
    print("An error occured when trying to save the word!\n")

  setBodyPartsToEmpty()
  createClueArray()

  while(gameOver != True):
    printGuessArray()
    printGrid()
    printClueArray()
    playerGuess()
    checkForGameOver()
    if livesLeft == 0:
      gameOver = True
      print "\n###################################"
      print "###### GUESSING PLAYER LOST #######"
      print "###################################\n"


  printGuessArray()
  printGrid()
  printClueArray()
  print "ANSWER: " + puzzle + "\n"
  #grid 
  #player guesses until dead or won

def setBodyPartsToEmpty():
  global head 
  global shoulders
  global leftArm
  global rightArm
  global torso
  global leftLeg
  global rightLeg
  head = " "
  shoulders = " "
  leftArm = " "
  rightArm = " "
  torso = " "
  leftLeg = " "
  rightLeg = " "

def loseLife():
  global livesLeft
  global head 
  global shoulders
  global leftArm
  global rightArm
  global torso
  global leftLeg
  global rightLeg
  livesLeft -= 1
  if livesLeft == 6:
    head = "O"
  if livesLeft == 5:
    shoulders = "|"
  if livesLeft == 4:
    leftArm = "\\"
  if livesLeft == 3:
    rightArm = "/"
  if livesLeft == 2:
    torso = "|"
  if livesLeft == 1:
    leftLeg = "/"
  if livesLeft == 0:
    rightLeg = "\\"
    # gameOver()


def printGrid():
  global livesLeft
  global head 
  global shoulders
  global leftArm
  global rightArm
  global torso
  global leftLeg
  global rightLeg
  print("_______")
  print("|     |")
  print("|     "+head)
  print("|    "+leftArm+shoulders+rightArm)
  print("|     "+torso)
  print("|    "+leftLeg+" "+rightLeg)
  print("|")
  print("|__________")

      
def printGuessArray():
  global guessArray
  print("PREVIOUS GUESSES : " + guessArray)

def createClueArray():
  global puzzle
  global clueArray
  clueArray = []
  for c in puzzle:
    if c != " ":
      clueArray += "_"
    else:
      clueArray += " "

def printClueArray():
  global clueArray
  clue = ""
  for c in clueArray:
    clue += c
  print "\nCLUE: " + clue + "\n"

def playerGuess():
  global guessArray
  try:
    guess = raw_input("GUESS: ")
  except:
    print("Something went wrong! Guess was not completed.")
  if len(guess) > 1:
    print "Your guess exceeded 1 character. Try again."
    playerGuess()
    return
  guess = saveWordOrLetter(guess)
  #potentially check for guess twice
  addGuessToGuessArray(guess)
  checkWordForLetter(guess)

def addGuessToGuessArray(guess):
  global guessArray
  guessArray += guess + " "


def checkWordForLetter(guess):
  global clueArray
  global puzzle
  fail = True
  for i in range(0,len(puzzle)):
    if puzzle[i] == guess:
      clueArray[i] = guess
      fail = False
  if fail:
    loseLife()

def checkForGameOver():
  global gameOver
  global clueArray
  for c in clueArray:
    if c == "_":
      gameOver = False
      break
    else: 
      gameOver = True
  if gameOver == True:
    print "\n###################################"
    print "###### GUESSING PLAYER WINS #######"
    print "###################################\n"



def printRules():
  print("The Rules Are Simple: DONT GET HUNG!!")
  print("You can do this by correctly guessing your oponents word.")
  print("One player will input a word or words totalling less than 50 characters.")
  print("The other player will guess letters one at a time to construct the word or phrase.")
  print("The guessing player wins by guessing the word before they are hung, ")
  print("and their oponent wins if they think of a word or phrase hard enough not to be guessed!")
  print("Good luck, and try not to lose your head :P")

if __name__ == "__main__":
    main() 
