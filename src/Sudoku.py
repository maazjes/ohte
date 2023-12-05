import itertools
import random
import copy

class Sudoku:
    def __init__(self):
        self.base = 3
        self.board = self.generate_sudoku(3, 0)
        self.original_board = copy.deepcopy(self.board)
        self.set_empty_cells(self.base ** 4 - self.base ** 3)

    def validate(self):
        bad_rows = [row for row in self.board if not sum(row) == sum(set(row))]
        cols = list(zip(*self.board))

        bad_cols = [col for col in cols if not sum(col) == sum(set(col))]
        squares = []

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = list(itertools.chain.from_iterable(col[j:j+3] for col in cols[i:i+3]))
                squares.append(square)

        bad_squares = [square for square in squares if not sum(square) == sum(set(square))]

        return not (bad_rows or bad_cols or bad_squares)

    # Generate a random sudoku of size base^2 * base^2
    def generate_sudoku(self, base, empty_cells):
        def pattern(row, column, base):
            return (base*(row % base)+row//base+column) % (base**2)

        def shuffle(s):
            return random.sample(s, len(s))

        r_base = range(base)
        # Shuffle rows and columns ensuring that no rules of sudoku are broken
        rows = [g*base + r for g in shuffle(r_base) for r in shuffle(r_base)]
        cols = [g*base + c for g in shuffle(r_base) for c in shuffle(r_base)]
        nums = shuffle(range(1, base*base+1))
        # Produce a board using randomized baseline pattern
        board = [[nums[pattern(r, c, base)] for c in cols] for r in rows]
        # Remove some numbers to create the puzzle
        emptied_cells = set()

        for _ in range(empty_cells):
            row, col = random.randint(
                0, base**2 - 1), random.randint(0, base**2 - 1)
            while (row, col) in emptied_cells:
                row, col = random.randint(
                    0, base**2 - 1), random.randint(0, base**2 - 1)
            board[row][col] = 0
            emptied_cells.add((row, col))
        return board

    def set_base(self, base):
        self.base = base

    def set_empty_cells(self, empty_cells):
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

    def __str__(self):
        return "\n".join([str(self.board[i]) for i in range(len(self.board))])
