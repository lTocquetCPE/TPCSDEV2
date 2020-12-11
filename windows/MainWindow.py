"""
class containing the display logic and the layout of the main window
Also manages the popups necessary to make the game work

11/12/20
by Loïc (Pyrrha) TOCQUET

"""

from tkinter import Tk, Label, Canvas, Button, Entry, Toplevel


class MainWindow(Tk):
    # init manages the layout of the window
    def __init__(self):
        Tk.__init__(self)

        self.currentImg = None

        # window options
        self.title("Jeu du Pendu")

        # Widgets
        self.hangmanCanvas = Canvas(self, width=300, height=300, bg='ivory')
        self.tryButton = Button(self, text="Proposer")
        self.letterEntry = Entry(self)
        self.currentWordLabel = Label(self, text="_ _ _ _ _ _ _")
        self.triesLeftLabel = Label(self, text="Essais restant : infini")
        self.currentScoreLabel = Label(self, text="Score :")

        # Packs
        self.tryButton.pack()
        self.letterEntry.pack()
        self.hangmanCanvas.pack()
        self.currentWordLabel.pack()
        self.triesLeftLabel.pack()
        self.currentScoreLabel.pack()

    # Opens a popup

    def alert(self, msg):
        popup = Toplevel()
        popup.title('Jeu du pendu')
        Label(popup, text=msg).pack()
        Button(popup, text='Quitter', command=popup.destroy).pack(
            padx=10, pady=10)
        popup.grab_set()

    # Clears the letter Entry
    def clearEntry(self):
        self.letterEntry.delete(0, 'end')

    # Handles the popup to restart the game

    def restartGamePopup(self, msg, startGame):
        popup = Toplevel()
        popup.title('Jeu du pendu')
        Label(popup, text=msg).pack()
        Button(popup, text='Rejouer', command=lambda: [popup.destroy(), startGame()]).pack(
            padx=10, pady=10)
        Button(popup, text='Quitter', command=lambda: exit()).pack(
            padx=10, pady=10)
        popup.grab_set()
