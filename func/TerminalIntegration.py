'''
Groups all the function relative to terminal integration of the Hangman game

27/09/2020
by Loïc (Pyrrha) TOCQUET

'''

from classes.GameState import GameState
from func.GameFileIO import getWordFromFile, getHighScoreFromFile, writeNewHighScore

#starts and initializes the game for a terminal use
def startGame(gameState = None):
  word = getWordFromFile("wordsList.txt")
  highScoreData = getHighScoreFromFile("scores.txt")
  if gameState == None :
    newGameState = GameState(word, highScoreData[0], int(highScoreData[1]))
  else:
    newGameState = GameState(word, highScoreData[0], int(highScoreData[1]), gameState.winsInARow)
  print("Let's play the Hangman game !\n")
  print("High score : ", newGameState.highScore)
  print("Best Player :", newGameState.highScorePlayer)
  print("Your Score :", newGameState.winsInARow)

  newTry(newGameState)

#displays in the terminal the try information
def displayTryInfo(gameState):
  print("-----------------------------------\n")
  print("Number of tries left : ", gameState.triesLeft, "\n")
  displayHiddenWord(gameState)
  
#handles the hangman game tries
def newTry(gameState):
  displayTryInfo(gameState)
  inputTry(gameState)

  if not gameState.hasWon():
    gameState.triesLeft -=1
    if gameState.triesLeft > 0:
      newTry(gameState)
      return 0
  endGame(gameState)

#checks if the string entered is valid for the hangman game
def checkValidity(letter):
  if (len(letter) == 1 and letter in "abcdefghijklmnopqrstuvwxyzéèùêïûà"):
    return True
  else:
    return False

#Handles the terminal input for a try
def inputTry(gameState):
  letter = "2"
  while(not checkValidity(letter)):
    letter = input("Please input a letter\n").lower()
  gameState.letterAttempt(letter)

#handles the end of the game
def endGame(gameState):
  if gameState.hasWon():
    print("Congratulation ! You won")
    gameState.winsInARow += 1
    if gameState.winsInARow > gameState.highScore:
      newHighScore(gameState)
  else:
    print("You lost !")
    gameState.winsInARow = 0
  if input("Do you want to play again ? (y/n)") == "y":
    startGame(gameState)

#displays the hidden word
def displayHiddenWord(gameState):
  displayedStr = ""
  for i, letter in enumerate(gameState.word):
    if gameState.revealedList[i]:
      displayedStr += letter + " "
    else:
      displayedStr += "_ "
  displayedStr+="\n"
  print(displayedStr)

#Handles when the highscore is beaten
def newHighScore(gameState):
  name = input("You're our new champion ! What's you name ?\n")
  gameState.highScorePlayer = name
  gameState.highScore = gameState.winsInARow
  writeNewHighScore(gameState.highScorePlayer, gameState.highScore, "scores.txt")
