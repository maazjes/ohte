import itertools
import random
import copy

class Sudoku:
    """
    A class to represent a Sudoku game.

    Attributes:
        base (int): The base number for the Sudoku grid
        size base * baseis the actual size of the Sudoku.
        board (list): The current state of the Sudoku board.
        original_board (list): The original state of the Sudoku board for reference.
    """

    def __init__(self):
        """
        Initializes a Sudoku game with a default base and generates a new random Sudoku.
        """

        self.base = 3
        self.board = self.generate_sudoku(3)
        self.original_board = copy.deepcopy(self.board)
        self.set_empty_cells(self.base ** 4 - self.base ** 3)

    def validate(self):
        """
        Checks if the current state of the Sudoku board is valid.

        A Sudoku board is valid if each row, column, and base x base square contains
        all numbers from 1 to base^2 without repetition.

        Returns:
            bool: True if the board is valid, False otherwise.
        """

        bad_rows = [row for row in self.board if not sum(row) == sum(set(row))]
        cols = list(zip(*self.board))

        bad_cols = [col for col in cols if not sum(col) == sum(set(col))]
        squares = []

        for i in range(0, self.base ** 2, self.base):
            for j in range(0, self.base ** 2, self.base):
                square = list(itertools.chain.from_iterable(
                    col[j:j+self.base] for col in cols[i:i+self.base]))
                squares.append(square)

        bad_squares = [square for square in squares if not sum(square) == sum(set(square))]

        return not (bad_rows or bad_cols or bad_squares)


    def generate_sudoku(self, base):
        """
        Generates a new Sudoku of a given base size.

        Args:
            base (int): The base size of the Sudoku.

        Returns:
            list: A 2D list representing the Sudoku.
        """

        def pattern(row, column, base):
            return (base*(row % base)+row//base+column) % (base**2)

        def shuffle(s):
            return random.sample(s, len(s))

        r_base = range(base)

        rows = [g*base + r for g in shuffle(r_base) for r in shuffle(r_base)]
        cols = [g*base + c for g in shuffle(r_base) for c in shuffle(r_base)]
        nums = shuffle(range(1, base*base+1))

        board = [[nums[pattern(r, c, base)] for c in cols] for r in rows]

        return board

    def set_base(self, base):
        """
        Sets a new random Sudoku of a given base size as the current board.

        Args:
            base (int): The base size of the Sudoku.
        """

        self.base = base
        self.set_random_sudoku()

    def set_empty_cells(self, empty_cells):
        """
        Sets a specified number of cells to be empty.

        Args:
            empty_cells (int): The amount of cells to empty.
        """

        emptied_cells = set()
        new_board = copy.deepcopy(self.original_board)

        for _ in range(empty_cells):
            row, col = random.randint(
                0, self.base**2 - 1), random.randint(0, self.base**2 - 1)

            while (row, col) in emptied_cells:
                row, col = random.randint(
                    0, self.base**2 - 1), random.randint(0, self.base**2 - 1)

            new_board[row][col] = 0
            emptied_cells.add((row, col))

        self.board = new_board

    def set_random_sudoku(self):
        """
        Sets a random sudoku as the current board.
        """

        self.board = self.generate_sudoku(self.base)
        self.original_board = copy.deepcopy(self.board)
        self.set_empty_cells(self.base ** 4 - self.base ** 3)

    def __str__(self):
        return "\n".join([str(self.board[i]) for i in range(len(self.board))])
