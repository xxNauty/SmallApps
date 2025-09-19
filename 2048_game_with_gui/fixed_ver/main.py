import tkinter as tk

from gui import game, game_history, main_menu, records, results

if __name__ == "__main__":
    root = tk.Tk()
    gameboard = game.GameGUI(master=root)
    gameboard.mainloop()