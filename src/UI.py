import tkinter as tk
from tkinter import ttk
from Sudoku import Sudoku

class UI(tk.Frame):
    def __init__(self, root, sudoku: Sudoku):
        tk.Frame.__init__(self, root)
        self.root = root
        self.sudoku = sudoku
        self.entry_values = [[tk.StringVar(
            value=self.sudoku.board[row][col] if self.sudoku.board[row][col] != 0 else '')
            for col in range(9)] for row in range(9)]
        self.control_values = [tk.StringVar(), tk.StringVar()]
        self.cells: dict[tuple[int, int], tk.Entry] = {}
        self.create_grid()
        self.bind('<Configure>', self.on_window_resize)
        self.user_resized = False
        self.create_controls()

    def create_controls(self):
        controls_window = tk.Toplevel(self)
        controls_window.title("Controls")

        # Add controls to the new window
        vcmd = self.register(self.validate_entry)

        label1 = ttk.Label(controls_window, text="Base", font=('Arial', 12))
        label1.grid(row=0, column=0, padx=5, pady=5)

        entry1 = ttk.Entry(controls_window, textvariable=self.control_values[0], validate='all',
            validatecommand=(vcmd, '%P'), justify='center', width=5, font=('Arial', 15))
        entry1.grid(row=0, column=1, padx=5, pady=5)

        label2 = ttk.Label(controls_window, text="Empty cells", font=('Arial', 12))
        label2.grid(row=1, column=0, padx=5, pady=5)

        entry2 = ttk.Entry(controls_window, textvariable=self.control_values[1], validate='all',
            validatecommand=(vcmd, '%P'), justify='center', width=5, font=('Arial', 15))
        self.control_values[1].trace("w", self.on_empty_cells_change)
        entry2.grid(row=1, column=1, padx=5, pady=5)

        self.root.update_idletasks()
        self.root.overrideredirect(False)
        controls_window.lift()

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                entry = ttk.Entry(
                    self, textvariable=self.entry_values[i][j],
                    justify='center', width=2, font=('Arial', 25))
                entry.bind('<KeyRelease>',
                           lambda event, row=i, col=j: self.on_entry_change(event, row, col))
                entry.grid(row=i, column=j, sticky='nsew')
                self.cells[(i, j)] = entry

        for i in range(9):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_window_resize(self, event):
        if not self.user_resized:
            self.user_resized = True
            return

        font_size = min(event.height // 20, event.width // 20)

        for i in range(9):
            for j in range(9):
                self.cells[(i, j)].config(font=('Arial', font_size))

    def on_entry_change(self, _, row, col):
        entry_value = self.entry_values[row][col].get()

        if entry_value == '':
            self.sudoku.board[row][col] = 0
        else:
            self.sudoku.board[row][col] = int(self.entry_values[row][col].get())

        for row in self.entry_values:
            for val in row:
                if val.get() == "":
                    return

        if self.sudoku.validate():
            print("Solution is valid")
        else:
            print("Solution is invalid")

    def on_empty_cells_change(self, *_):
        empty_cells_amount = 0

        if self.control_values[1].get() != '':
            empty_cells_amount = int(self.control_values[1].get())

        if empty_cells_amount > self.sudoku.base ** 4:
            return

        self.sudoku.set_empty_cells(empty_cells_amount)

        for i in range(self.sudoku.base ** 2):
            for j in range(self.sudoku.base ** 2):
                self.entry_values[i][j].set(
                    '' if self.sudoku.board[i][j] == 0 else self.sudoku.board[i][j])

    def validate_entry(self, p):
        return str.isdigit(p) or p == ""
