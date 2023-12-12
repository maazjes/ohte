import tkinter as tk
from Sudoku import Sudoku
from UI import UI

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sudoku")
    ui = UI(root, Sudoku())
    ui.pack(expand=True, fill='both')
    root.mainloop()
