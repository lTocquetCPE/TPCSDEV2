'''
Class containing all the variables for the core "Hangman" game to work, regardless of the output method

27/09/2020 by Loïc (Pyrrha) TOCQUET

'''
lettersWithAccents = ["a", "e", "i", "o", "u"]
lettersAccented = [["à", "â"], ["é", "è", "ê", "ë"], ["ï", "î"], ["ô"], ["û"]]

class GameState:
  #Instantiates the GameState object so that it's ready to use
  #word (string) : word hidden by the game that the user should try to find
  #highScorePlayer(string) :Name of best player
  #highScore (int) : Best score (games won in a row)
  def __init__(self, word, highScorePlayer, highScore, winsInARow = 0):
    self.word = word
    self.revealedList = [False] * len(self.word)
    self.triesLeft = 8
    self.revealedList[0] = True
    self.alreadyTriedLetters = ""
    self.winsInARow = winsInARow
    self.highScorePlayer = highScorePlayer
    self.highScore = highScore


  #handles the letter attempt and the reveal of the right letters in the displayword attribute. Displays if a latter has already been attempted
  def letterAttempt(self, attemptedLetter):
    if attemptedLetter in self.alreadyTriedLetters:
      print("You have already tried the ", attemptedLetter, " !\n")
      return
    self.alreadyTriedLetters += attemptedLetter
    for i, letter in enumerate(self.word):
      if letter == attemptedLetter:
        self.revealedList[i] = True
      if attemptedLetter in lettersWithAccents:
        for accents in lettersAccented[lettersWithAccents.index(attemptedLetter)]:
          if accents == letter:
            self.revealedList[i] = True


  #returns the state of the win condition
  def hasWon(self):
    return all(self.revealedList)