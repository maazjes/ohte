import tkinter as tk
from tkinter import ttk
from typing import Any
from sudoku import Sudoku
from database import Database
import time


class UI(tk.Frame):
    """
    A class representing the User Interface (UI) for the Sudoku game.

    This class is responsible for creating and managing the graphical user interface
    components of the Sudoku game.

    Attributes:
        root (tk.Tk): The root window of the application.
        sudoku (Sudoku): The Sudoku game logic.
        database: Reference to the database object for game data storage.
        cells (dict): Dictionary of cells in the Sudoku grid.
        border_frames (list): List of frames used for boldened grid borders.
        user_resized (bool): Flag indicating whether the user has resized the window.
        resize_timer (int): Timer for resize event handling.
        settings_window (tk.Toplevel): The settings window.
        stats_window: Window displaying game statistics.
    """

    def __init__(self, root: tk.Tk, sudoku: Sudoku, database: Database) -> None:
        """
        Initializes the UI for the Sudoku game.

        Args:
            root (tk.Tk): The root window of the application.
            sudoku (Sudoku): The Sudoku game logic instance.
        """
        tk.Frame.__init__(self, root)
        self.root = root
        self.sudoku = sudoku
        self.database = database
        self.cells: dict[tuple[int, int], tk.Entry] = {}
        self.border_frames: list[tk.Frame] = []
        self.user_resized = False
        self.resize_timer = ""
        self.settings_window: tk.Toplevel | None = None
        self.stats_window: tk.Toplevel | None = None
        self.update_grid()
        self.create_menu()
        self.bind("<Configure>", self.on_window_resize)

    def update_grid(self) -> None:
        """
        Updates the visual representation of the Sudoku grid on the UI.

        This method refreshes the grid to reflect the current state of the Sudoku game.
        It also updates the values in each cell based on the Sudoku puzzle's current configuration.
        """
        self.cell_values = [
            [
                tk.StringVar(
                    value=str(self.sudoku.board[row][col])
                    if self.sudoku.board[row][col] != 0
                    else ""
                )
                for col in range(self.sudoku.base**2)
            ]
            for row in range(self.sudoku.base**2)
        ]

        for frame in self.border_frames:
            frame.destroy()

        for cell in self.cells.values():
            cell.destroy()

        self.border_frames.clear()
        self.cells.clear()
        self.create_grid()
        self.update()

    def create_settings(self) -> None:
        """
        Creates a settings window with additional settings for the Sudoku game.

        This method initializes and positions UI elements such as labels, entries,
        and buttons for configuring game settings like base size and number of empty cells.
        """

        def validate_empty_cells_label(p: str) -> bool:
            """
            Validates the input for the number of empty cells in the Sudoku puzzle.

            Args:
                p: The input value to validate.

            Returns:
                bool: True if the input is valid, False otherwise.
            """
            return (str.isdigit(p) and 0 <= int(p) <= self.sudoku.base**4) or p == ""

        self.settings_window = tk.Toplevel(self)
        self.settings_window.title("Settings")

        vcmd = self.register(validate_empty_cells_label)

        base_label = ttk.Label(self.settings_window, text="Base", font=("Arial", 12))
        base_label.grid(row=0, column=0, padx=5, pady=5)
        base_options = ["2", "3", "4", "5"]

        base_combobox = ttk.Combobox(
            self.settings_window, values=base_options, width=2, font=("Arial", 15)
        )
        base_combobox.set(3)
        base_combobox.bind("<<ComboboxSelected>>", self.on_base_change)
        base_combobox.grid(row=0, column=1, padx=5, pady=5)

        empty_cells_label = ttk.Label(
            self.settings_window, text="Empty cells", font=("Arial", 12)
        )
        empty_cells_label.grid(row=1, column=0, padx=5, pady=5)

        empty_cells_entry = ttk.Entry(
            self.settings_window,
            validate="all",
            validatecommand=(vcmd, "%P"),
            justify="center",
            width=3,
            font=("Arial", 15),
        )
        empty_cells_entry.bind("<KeyRelease>", self.on_empty_cells_change)
        empty_cells_entry.grid(row=1, column=1, padx=5, pady=5)

        self.settings_window.resizable(False, False)
        self.root.update_idletasks()
        self.root.overrideredirect(False)
        self.settings_window.lift()

    def create_menu(self) -> None:
        """
        Creates the main menu for the application.

        This method sets up menu items such as 'New Sudoku' and 'Settings',
        attaching relevant commands to these menu options.
        """
        menu_bar = tk.Menu(self.root, bg="green")
        self.root.config(menu=menu_bar)
        menu_bar.add_command(label="New sudoku", command=self.on_generate_button_press)
        menu_bar.add_command(label="Stats", command=self.open_stats)
        menu_bar.add_command(label="Settings", command=self.open_settings)

    def create_grid(self) -> None:
        """
        Sets up the visual representation of the Sudoku grid in the UI,
        which involves creating and positioning cell widgets according to the Sudoku layout.
        """

        def validate_entry(p: str) -> bool:
            """
            Ensures correct entry in Sudoku cells.

            Args:
                p: The input value in a Sudoku cell to validate.

            Returns:
                bool: True if the input is valid, False otherwise.
            """
            return (str.isdigit(p) and 1 <= int(p) <= self.sudoku.base**2) or p == ""

        vcmd = self.register(validate_entry)

        border_thickness = 2

        for row in range(self.sudoku.base**2):
            for col in range(self.sudoku.base**2):

                def on_key_release(
                    event: tk.Event, row: int = row, col: int = col
                ) -> None:
                    self.on_cell_change(event, row, col)

                cell = ttk.Entry(
                    self,
                    textvariable=self.cell_values[row][col],
                    validate="all",
                    validatecommand=(vcmd, "%P"),
                    justify="center",
                    width=2,
                    font=("Arial", 25),
                )
                cell.bind(
                    "<KeyRelease>",
                    on_key_release,
                )
                cell.grid(row=row * 2, column=col * 2, sticky="nsew")
                self.cells[(row, col)] = cell

                if (
                    row < self.sudoku.base**2 - 1
                    and row % self.sudoku.base == self.sudoku.base - 1
                ):
                    frame = tk.Frame(self, height=border_thickness, bg="black", bd=0)
                    frame.grid(
                        row=row * 2 + 1, column=col * 2, columnspan=2, sticky="ew"
                    )
                    self.border_frames.append(frame)

                if (
                    col < self.sudoku.base**2 - 1
                    and col % self.sudoku.base == self.sudoku.base - 1
                ):
                    frame = tk.Frame(self, width=border_thickness, bg="black", bd=0)
                    frame.grid(row=row * 2, column=col * 2 + 1, rowspan=2, sticky="ns")
                    self.border_frames.append(frame)

        for i in range(self.sudoku.base**2 * 2):
            self.grid_rowconfigure(i, weight=1 if i % 2 == 0 else 0)
            self.grid_columnconfigure(i, weight=1 if i % 2 == 0 else 0)

    def create_stats(self) -> None:
        """
        Creates the statistics window for the application.

        This method constructs a window that displays various game statistics,
        like the games' average completion time, moves etc.
        """
        self.stats_window = tk.Toplevel(self)
        self.stats_window.title("Stats")

        tree = ttk.Treeview(self.stats_window)
        tree["columns"] = ("Time", "Moves", "Empty cells")
        tree.column("#0", width=0, stretch=tk.NO)
        tree.heading("#0", text="", anchor=tk.W)

        for col in tree["columns"]:
            tree.column(col, anchor=tk.CENTER)
            tree.heading(col, text=col, anchor=tk.CENTER)

        games = self.database.get_games()

        for game in games:
            tree.insert("", tk.END, values=(game[1], game[2], game[3]))

        scrollbar = ttk.Scrollbar(
            self.stats_window, orient="vertical", command=tree.yview
        )

        tree.configure(yscrollcommand=scrollbar.set)
        tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.stats_window.grid_columnconfigure(0, weight=1)
        self.stats_window.grid_rowconfigure(0, weight=1)

    def open_settings(self) -> None:
        """
        Opens the settings window for the application.
        """
        if not self.settings_window or not tk.Toplevel.winfo_exists(
            self.settings_window
        ):
            self.create_settings()
        else:
            self.settings_window.lift()

    def open_stats(self) -> None:
        """
        Opens the window that displays game statistics.
        """
        if not self.stats_window or not tk.Toplevel.winfo_exists(self.stats_window):
            self.create_stats()
        else:
            self.stats_window.lift()

    def on_window_resize(self, event: tk.Event) -> None:
        """
        Handles window resize events for the application.

        Args:
            event: The event object associated with the window resize action.
        """
        if not self.user_resized:
            return

        if self.resize_timer is not None:
            self.after_cancel(self.resize_timer)

        self.resize_timer = self.after(500, lambda: self.window_resize_action(event))

    def window_resize_action(self, event: tk.Event) -> None:
        """
        Executes actions related to window resizing.
        """
        font_size = (
            min(event.height // 15, event.width // 15) * 9 // self.sudoku.base**2
        )

        for row in range(self.sudoku.base**2):
            for col in range(self.sudoku.base**2):
                self.cells[(row, col)].config(font=("Arial", font_size))

    def on_cell_change(self, _: tk.Event, row: int, col: int) -> None:
        """
        Responds to changes in individual cells of the Sudoku grid.

        Args:
            _: The event object triggering the cell change.
            row: The row index of the changed cell.
            col: The column index of the changed cell.
        """
        cell_value = self.cell_values[row][col].get()

        if cell_value == "":
            self.sudoku.insert_number(row, col, 0)
        else:
            self.sudoku.insert_number(row, col, int(self.cell_values[row][col].get()))

        for cell_row in self.cell_values:
            for val in cell_row:
                if val.get() == "":
                    return

        if self.sudoku.validate():
            self.show_message("Validation", "Solution is valid!")
            seconds = int(time.time() - self.sudoku.start)
            self.database.insert_game(
                seconds, self.sudoku.moves, self.sudoku.empty_cells
            )
        else:
            self.show_message("Validation", "Solution is invalid!")

    def on_base_change(self, event: tk.Event) -> None:
        """
        Handles modifications to the base setting of the Sudoku.
        """
        base = int(event.widget.get())
        self.sudoku.set_base(base)
        self.update_grid()

    def on_empty_cells_change(self, event: tk.Event) -> None:
        """
        Handles changes to the number of empty cells in the Sudoku puzzle.

        Args:
            event: The event object containing information about the change in empty cells.
        """
        empty_cells = 0

        if event.widget.get() != "":
            empty_cells = int(event.widget.get())

        if empty_cells > self.sudoku.base**4:
            return

        self.sudoku.set_empty_cells(empty_cells)

        for row in range(self.sudoku.base**2):
            for col in range(self.sudoku.base**2):
                val = (
                    ""
                    if self.sudoku.board[row][col] == 0
                    else str(self.sudoku.board[row][col])
                )
                self.cell_values[row][col].set(val)

    def show_message(self, title: str, message: str) -> None:
        """
        Presents a message dialog to the user.
        """
        dialog = tk.Toplevel(self)
        dialog.title(title)
        dialog.transient(self.root)
        dialog.grab_set()

        tk.Label(dialog, text=message, font=("Arial", 13)).pack(padx=20, pady=10)

        button = tk.Button(dialog, text="OK", command=dialog.destroy, width=10)
        button.pack(pady=5)

        self.root.update_idletasks()
        x = (
            self.root.winfo_x()
            + (self.root.winfo_width() - dialog.winfo_reqwidth()) // 2
        )
        y = (
            self.root.winfo_y()
            + (self.root.winfo_height() - dialog.winfo_reqheight()) // 2
        )
        dialog.geometry(f"+{x}+{y}")

        self.root.wait_window(dialog)

    def on_generate_button_press(self, *_: tuple[Any]) -> None:
        """
        Triggers the generation of a new Sudoku puzzle.

        Args:
            event: The event object associated with pressing the generate button.
        """
        self.sudoku.set_random_sudoku()
        self.update_grid()
