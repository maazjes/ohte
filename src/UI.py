import tkinter as tk
from tkinter import ttk
from Sudoku import Sudoku


class UI(tk.Frame):
    def __init__(self, master, logic: Sudoku):
        tk.Frame.__init__(self, master)
        self.logic = logic
        self.entry_values = [[tk.StringVar(
            value=self.logic.board[i][j] if self.logic.board[i][j] != 0 else '') for i in range(9)] for j in range(9)]
        self.cells = {}
        self.create_grid()
        self.bind('<Configure>', self.on_window_resize)
        self.user_resized = False

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                entry = ttk.Entry(
                    self, textvariable=self.entry_values[i][j], justify='center', width=2)
                entry.bind('<KeyRelease>',
                           lambda event, row=i, col=j: self.on_entry_change(event, row, col))
                entry.grid(row=i, column=j, sticky='nsew')
                self.cells[(i, j)] = entry

        for i in range(9):
            self.grid_rowconfigure(i, weight=1, minsize=50)
            self.grid_columnconfigure(i, weight=1, minsize=50)

    def on_window_resize(self, event):
        if not self.user_resized:
            self.user_resized = True
            return

        font_size = min(event.height // 20, event.width // 20)

        for i in range(9):
            for j in range(9):
                self.cells[(i, j)].config(font=('Arial', font_size))

    def on_entry_change(self, _, row, col):
        self.logic.board[row][col] = int(self.entry_values[row][col].get())
        for row in self.entry_values:
            for val in row:
                if val.get() == "":
                    return

        if self.logic.validate():
            print("Solution is valid")
        else:
            print("Solution is invalid")
