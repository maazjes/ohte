import unittest
from helpers import generate_sudoku
from Sudoku import Sudoku

class TestHelpers(unittest.TestCase):
    def test_generate_sudoku_creates_valid_sudoku(self):
        sudoku = Sudoku(board=generate_sudoku(3, 10))
        self.assertFalse(sudoku.solve())