import tkinter as tk
from sudoku import Sudoku
from database import Database
from ui import UI

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sudoku")
    ui = UI(root, Sudoku(), Database())
    ui.pack(expand=True, fill="both")
    root.mainloop()
