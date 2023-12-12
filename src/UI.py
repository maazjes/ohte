import tkinter as tk
from tkinter import ttk
from Sudoku import Sudoku

class UI(tk.Frame):
    """
    A class representing the User Interface (UI) for the Sudoku game.

    This class is responsible for creating and managing the graphical user interface
    components of the Sudoku game.

    Attributes:
        root (tk.Tk): The root window of the application.
        sudoku (Sudoku): The Sudoku game logic.
        control_values (list): List of settings to change.
        cells (dict): Dictionary of cells in the Sudoku grid.
        border_frames (list): List of frames used for boldened grid borders.
        user_resized (bool): Flag indicating whether the user has resized the window.
        resize_timer (int): Timer for resize event handling.
        controls_window (tk.Toplevel): The controls (settings) window.
    """
    def __init__(self, root, sudoku: Sudoku):
        """
        Initializes the UI for the Sudoku game.

        Args:
            root (tk.Tk): The root window of the application.
            sudoku (Sudoku): The Sudoku game logic instance.
        """
        tk.Frame.__init__(self, root)
        self.root = root
        self.sudoku = sudoku
        self.control_values = [tk.StringVar(), tk.StringVar()]
        self.cells: dict[tuple[int, int], tk.Entry] = {}
        self.border_frames = []
        self.user_resized = False
        self.resize_timer = None
        self.controls_window = None
        self.update_grid()
        self.create_menu()
        self.bind('<Configure>', self.on_window_resize)
        self.user_resized = True

    def update_grid(self):
        """
        Updates the visual representation of the Sudoku grid on the UI.

        This method refreshes the grid to reflect the current state of the Sudoku game.
        It also updates the values in each cell based on the Sudoku puzzle's current configuration.
        """

        self.entry_values = [[tk.StringVar(
            value=self.sudoku.board[row][col] if self.sudoku.board[row][col] != 0 else '')
            for col in range(self.sudoku.base ** 2)] for row in range(self.sudoku.base ** 2)]

        for frame in self.border_frames:
            frame.destroy()

        for entry in self.cells.values():
            entry.destroy()

        self.border_frames.clear()
        self.cells.clear()
        self.create_grid()
        self.update()

    def create_controls(self):
        """
        Creates a settings window with additional settings for the Sudoku game.

        This method initializes and positions UI elements such as labels, entries, 
        and buttons for configuring game settings like base size and number of empty cells.
        """

        self.controls_window = tk.Toplevel(self)
        self.controls_window.title("Controls")

        vcmd = self.register(self.validate_empty_cells)

        label1 = ttk.Label(self.controls_window, text="Base", font=('Arial', 12))
        label1.grid(row=0, column=0, padx=5, pady=5)

        base_options = [2, 3, 4, 5]
        combobox_base = ttk.Combobox(self.controls_window,
            values=base_options, width=2, font=('Arial', 15))
        combobox_base.set(3)
        combobox_base.bind("<<ComboboxSelected>>", self.on_base_change)
        combobox_base.grid(row=0, column=1, padx=5, pady=5)

        label2 = ttk.Label(self.controls_window, text="Empty cells", font=('Arial', 12))
        label2.grid(row=1, column=0, padx=5, pady=5)

        entry2 = ttk.Entry(self.controls_window, textvariable=self.control_values[1],
            validate='all', validatecommand=(vcmd, '%P'), justify='center',
            width=3, font=('Arial', 15))
        entry2.bind('<KeyRelease>', self.on_empty_cells_change)
        entry2.grid(row=1, column=1, padx=5, pady=5)

        self.controls_window.resizable(False, False)
        self.root.update_idletasks()
        self.root.overrideredirect(False)
        self.controls_window.lift()

    def create_menu(self):
        """
        Creates the main menu for the application.

        This method sets up menu items such as 'New Sudoku' and 'Settings', 
        attaching relevant commands to these menu options.
        """
        menu_bar = tk.Menu(self.root, bg='green')
        self.root.config(menu=menu_bar)
        menu_bar.add_command(label="New sudoku", command=self.on_generate_button_press)
        menu_bar.add_command(label="Settings", command=self.open_controls)

    def open_controls(self):
        if not self.controls_window or not tk.Toplevel.winfo_exists(self.controls_window):
            self.create_controls()
        else:
            self.controls_window.lift()

    def create_grid(self):
        vcmd = self.register(self.validate_entry)

        border_thickness = 2

        for i in range(self.sudoku.base ** 2):
            for j in range(self.sudoku.base ** 2):
                entry = ttk.Entry(
                    self, textvariable=self.entry_values[i][j], validate='all',
                    validatecommand=(vcmd, '%P'), justify='center', width=2, font=('Arial', 25))
                entry.bind('<KeyRelease>',
                           lambda event, row=i, col=j: self.on_entry_change(event, row, col))
                entry.grid(row=i*2, column=j*2, sticky='nsew')
                self.cells[(i, j)] = entry

                if i < self.sudoku.base ** 2 - 1 and i % self.sudoku.base == self.sudoku.base - 1:
                    frame = tk.Frame(self, height=border_thickness, bg='black', bd=0)
                    frame.grid(row=i*2+1, column=j*2, columnspan=2, sticky='ew')
                    self.border_frames.append(frame)

                if j < self.sudoku.base ** 2 - 1 and j % self.sudoku.base == self.sudoku.base - 1:
                    frame = tk.Frame(self, width=border_thickness, bg='black', bd=0)
                    frame.grid(row=i*2, column=j*2+1, rowspan=2, sticky='ns')
                    self.border_frames.append(frame)

        for i in range(self.sudoku.base ** 2 * 2):
            self.grid_rowconfigure(i, weight=1 if i % 2 == 0 else 0)
            self.grid_columnconfigure(i, weight=1 if i % 2 == 0 else 0)

    def on_window_resize(self, event):
        if not self.user_resized:
            return

        if self.resize_timer is not None:
            self.after_cancel(self.resize_timer)

        self.resize_timer = self.after(500, lambda: self.window_resize_action(event))

    def window_resize_action(self, event):
        font_size = min(event.height // 15, event.width // 15) * 9 // self.sudoku.base ** 2

        for i in range(self.sudoku.base ** 2):
            for j in range(self.sudoku.base ** 2):
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
            self.show_custom_messagebox("Validation", "Solution is valid!")
        else:
            self.show_custom_messagebox("Validation", "Solution is invalid!")

    def on_base_change(self, event: tk.Event):
        base = int(event.widget.get())
        self.sudoku.set_base(base)
        self.update_grid()

    def on_empty_cells_change(self, event):
        empty_cells_amount = 0

        if event.widget.get() != '':
            empty_cells_amount = int(event.widget.get())

        if empty_cells_amount > self.sudoku.base ** 4:
            return

        self.sudoku.set_empty_cells(empty_cells_amount)

        for i in range(self.sudoku.base ** 2):
            for j in range(self.sudoku.base ** 2):
                self.entry_values[i][j].set(
                    '' if self.sudoku.board[i][j] == 0 else self.sudoku.board[i][j])

    def show_custom_messagebox(self, title, message):
        dialog = tk.Toplevel(self)
        dialog.title(title)
        dialog.transient(self.root)
        dialog.grab_set()

        tk.Label(dialog, text=message, font=('Arial', 13)).pack(padx=20, pady=10)

        button = tk.Button(dialog, text="OK", command=dialog.destroy, width=10)
        button.pack(pady=5)

        self.root.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - dialog.winfo_reqwidth()) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - dialog.winfo_reqheight()) // 2
        dialog.geometry(f"+{x}+{y}")

        self.root.wait_window(dialog)

    def on_generate_button_press(self, *_):
        self.sudoku.set_random_sudoku()
        self.update_grid()

    def validate_entry(self, p):
        return (str.isdigit(p) and 1 <= int(p) <= self.sudoku.base ** 2) or p == ""

    def validate_empty_cells(self, p):
        return (str.isdigit(p) and 0 <= int(p) <= self.sudoku.base ** 4) or p == ""
