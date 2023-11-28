import itertools
from helpers import generate_sudoku


class Sudoku:
    def __init__(self, base=3, empty_cells=0, board=None):
        self.base = base
        if board:
            self.board = board
        else:
            self.board = generate_sudoku(base, empty_cells)

    def validate(self):
        bad_rows = [row for row in self.board if not sum(row) == sum(set(row))]
        print(self)
        cols = list(zip(*self.board))
        bad_cols = [col for col in cols if not sum(col) == sum(set(col))]
        squares = []

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = list(itertools.chain(col[j:j+3] for col in cols[i:i+3]))
                squares.append(square)

        bad_squares = [square for square in squares if not sum(list(itertools.chain(*square))) == sum(set(itertools.chain(*square)))]

        return not (bad_rows or bad_cols or bad_squares)

    def __str__(self):
        return "\n".join([str(self.board[i]) for i in range(len(self.board))])
