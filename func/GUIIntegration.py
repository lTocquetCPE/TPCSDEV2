"""
File containing the function necessary for the GUI integration of the hangman game. Manages the gameplay and user interaction

11/12/20
by Loïc (Pyrrha) TOCQUET

"""
from windows.MainWindow import MainWindow
from classes.GameState import GameState
from func.GameFileIO import getWordFromFile, getHighScoreFromFile, writeNewHighScore
from tkinter import PhotoImage

# Starts the game


def startGame(mainWindow=None, prevGameState=None):
    if mainWindow == None:
        mainWindow = MainWindow()

    word = getWordFromFile("wordsList.txt")
    highScoreData = getHighScoreFromFile("scores.txt")
    if prevGameState == None:
        gameState = GameState(word, highScoreData[0], int(highScoreData[1]))
    else:
        gameState = GameState(word, highScoreData[0], int(
            highScoreData[1]), prevGameState.winsInARow)

    mainWindow.tryButton.configure(
        command=lambda: tryLetter(mainWindow, gameState))

    updateWidgets(mainWindow, gameState)

    mainWindow.bind_all(
        '<Return>', lambda event: tryLetter(mainWindow, gameState))
    mainWindow.mainloop()


# Checks if an entry input is valid for the game
def checkInput(mainWindow):
    letter = mainWindow.letterEntry.get()

    if len(letter) != 1:
        mainWindow.alert("Veuillez entrer une seule lettre")
        return False

    if letter not in "abcdefghijklmnopqrstuvwxyz":
        mainWindow.alert(
            "Utilisez des lettres simples de l'alphabet (abcdefghijklmnopqrstwxyz)")
        return False
    return True

# callback for the tryButton, handles the game logic behind a try


def tryLetter(mainWindow, gameState):

    if checkInput(mainWindow):

        if gameState.letterAttempt(mainWindow.letterEntry.get()):
            if gameState.hasWon():
                triggerEndGame(mainWindow, gameState, 1)
                return

            gameState.triesLeft -= 1
            if gameState.triesLeft <= 0:
                triggerEndGame(mainWindow, gameState, 0)
                return
            updateWidgets(mainWindow, gameState)
            mainWindow.clearEntry()

        else:
            mainWindow.alert("Ce caractère a déjà été joué")
            mainWindow.clearEntry()
    else:
        mainWindow.clearEntry()


# Makes the hidden word string
def getHiddenWord(gameState):
    displayedStr = ""
    for i, letter in enumerate(gameState.word):
        if gameState.revealedList[i]:
            displayedStr += letter + " "
        else:
            displayedStr += "_ "
    return displayedStr

# Updates the widget to match de gameState


def updateWidgets(mainWindow, gameState):
    mainWindow.currentWordLabel.config(text=getHiddenWord(gameState))
    mainWindow.triesLeftLabel.config(
        text=str(gameState.triesLeft) + " essai(s) restant(s)")

    mainWindow.currentImg = PhotoImage(
        file="ressources/bonhomme" + str(9 - gameState.triesLeft) + ".gif")
    mainWindow.hangmanCanvas.create_image(
        0, 0, anchor="nw", image=mainWindow.currentImg)

    mainWindow.currentScoreLabel.config(
        text="Score : " + str(gameState.winsInARow))

# Handles the end of the game and the restart possibilities


def triggerEndGame(mainWindow, gameState, victoryValue):
    mainWindow.clearEntry()
    if victoryValue:
        gameState.winsInARow += 1
        mainWindow.restartGamePopup(
            "Vicoire ! \nSouhaitez-vous améliorer votre score ?", lambda: startGame(mainWindow, gameState))

    else:
        gameState.winsInARow = 0
        mainWindow.restartGamePopup(
            "Dommage vous avez perdu ! \nSouhaitez-vous retenter votre chance ?", lambda: startGame(mainWindow))
