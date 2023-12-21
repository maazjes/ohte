import itertools
import random
import copy
import time


class Sudoku:
    """
    Class representing a Sudoku game.

    Attributes:
        base: Base number of the Sudoku.
        Base * base is the actual length of the Sudoku. Default is 3.
        board: Current state of the Sudoku board.
        original_board: Original state of the Sudoku board for reference.
        empty_cells: Number of empty cells in the Sudoku.
        start: Start time of the game.
        moves: Number of moves made in the game.
    """

    def __init__(self) -> None:
        """
        Initializes a Sudoku game with a default base and generates a new random Sudoku.
        """
        self.base = 3
        self.board = self.generate_sudoku(3)
        self.original_board = copy.deepcopy(self.board)
        self.empty_cells = self.base**4 - self.base**3
        self.start = time.time()
        self.moves = 0
        self.set_empty_cells(self.empty_cells)

    def cell_is_valid(self, row: int, col: int, num: int) -> bool:
        """
        Checks if a given number in a given cell is valid according to Sudoku rules.

        Args:
            row: Row index of the cell.
            col: Column index of the cell.
            num: Number to check in the cell.

        Returns:
            True if the number is valid, False otherwise.
        """

        start_row, start_col = row - row % self.base, col - col % self.base

        for i in range(self.base**2):
            if num in (self.board[row][i], self.board[i][col]):
                return False

            grid_row, grid_col = start_row + (i // self.base), start_col + (
                i % self.base
            )
            if self.board[grid_row][grid_col] == num:
                return False

        return True

    def validate(self) -> bool:
        """
        Checks if the current state of the Sudoku board is valid.

        A Sudoku board is valid if each row, column, and base x base square contains
        all numbers from 1 to base^2 without repetition.

        Returns:
            True if the board is valid, False otherwise.
        """
        valid_sum = sum(range(self.base**2 + 1))
        bad_rows = [
            row for row in self.board if not sum(row) == sum(set(row)) == valid_sum
        ]
        cols: list[list[int]] = list(zip(*self.board))  # type: ignore

        bad_cols = [col for col in cols if not sum(col) == sum(set(col)) == valid_sum]
        squares = []

        for i in range(0, self.base**2, self.base):
            for j in range(0, self.base**2, self.base):
                square = list(
                    itertools.chain.from_iterable(
                        col[j : j + self.base] for col in cols[i : i + self.base]
                    )
                )
                squares.append(square)

        bad_squares = [
            square
            for square in squares
            if not sum(square) == sum(set(square)) == valid_sum
        ]

        return not (bad_rows or bad_cols or bad_squares)

    def generate_sudoku(self, base: int) -> list[list[int]]:
        """
        Generates a new Sudoku of a given base.

        Args:
            base: Base of the Sudoku to be generated.

        Returns:
            2D list representing the Sudoku.
        """

        def pattern(row: int, column: int, base: int) -> int:
            """
            Gives a number in range 1-9 for a given cell based on the rules of Sudoku.

            Args:
                row: Row index of the cell.
                column: Column index of the cell.
                base: Base of the Sudoku.

            Returns:
                Number in range 1-9.
            """
            return (base * (row % base) + row // base + column) % (base**2)

        def shuffle(s: range) -> list[int]:
            """
            Shuffles a given range into a list.

            Args:
                s: Range to shuffle.

            Returns:
                Shuffled list of the given range.
            """
            return random.sample(s, len(s))

        self.moves = 0
        self.start = time.time()

        r_base = range(base)

        rows = [g * base + r for g in shuffle(r_base) for r in shuffle(r_base)]
        cols = [g * base + c for g in shuffle(r_base) for c in shuffle(r_base)]
        nums = shuffle(range(1, base * base + 1))

        board = [[nums[pattern(r, c, base)] for c in cols] for r in rows]

        return board

    def insert_number(self, row: int, col: int, num: int) -> bool:
        """
        Inserts a number into the Sudoku board to a given cell.

        Args:
            row: Row index of the cell.
            col: Column index of the cell.
            num: Number to be inserted.

        Returns:
            True if the number inserted fits the Sudoku, False otherwise.
        """
        self.moves += 1
        self.board[row][col] = 0
        valid = self.cell_is_valid(row, col, num)
        self.board[row][col] = num
        return valid

    def set_base(self, base: int) -> None:
        """
        Sets a new random Sudoku of a given base as the current board.

        Args:
            base: Base of the Sudoku to set.
        """
        self.base = base
        self.set_random_sudoku()

    def set_empty_cells(self, empty_cells: int) -> None:
        """
        Sets a specified number of cells in the current board to be empty.

        Args:
            empty_cells: Amount of cells to empty.
        """
        self.empty_cells = empty_cells
        self.moves = 0
        emptied_cells = set()
        new_board = copy.deepcopy(self.original_board)

        for _ in range(empty_cells):
            row, col = random.randint(0, self.base**2 - 1), random.randint(
                0, self.base**2 - 1
            )

            while (row, col) in emptied_cells:
                row, col = random.randint(0, self.base**2 - 1), random.randint(
                    0, self.base**2 - 1
                )

            new_board[row][col] = 0
            emptied_cells.add((row, col))

        self.board = new_board

    def set_random_sudoku(self) -> None:
        """
        Sets a random sudoku as the current board.
        """
        self.board = self.generate_sudoku(self.base)
        self.original_board = copy.deepcopy(self.board)
        self.set_empty_cells(self.base**4 - self.base**3)

    def __str__(self) -> str:
        """
        Provides a string representation of the Sudoku board.

        Returns:
            String representation of the Sudoku board.
        """
        return "\n".join([str(self.board[i]) for i in range(len(self.board))])
