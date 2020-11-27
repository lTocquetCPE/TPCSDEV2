"""
groups all the functions related to fileIO with the file containing words.

27/09/20
by Loïc (Pyrrha) TOCQUET
"""
import random

#gets a random word from the wordFiles (Uses a lot of RAM for large files, prefer "Reservoir Sampling" for large scale files)
def getWordFromFile(path):
  file = open(path, "r")
  lines = file.readlines()
  randomLine = lines[random. randint(0,len(lines)-1)]
  if randomLine.endswith("\n"):
    randomLine = randomLine[0 : -1]
  file.close()
  return randomLine

#Gets the best player and best score data from a file
def getHighScoreFromFile(path):
  file = open(path, "r")
  lines = file.readlines()
  lines[0][0:-1]
  file.close()
  return lines
#Writes the new best player name and score in a file
def writeNewHighScore(player, score, path):
  file = open(path, "w")
  file.write(player+"\n")
  file.write(str(score))
  file.close()