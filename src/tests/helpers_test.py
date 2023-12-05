import unittest
from Sudoku import Sudoku


class TestHelpers(unittest.TestCase):
    def test_generate_sudoku_creates_valid_sudoku(self):
        sudoku = Sudoku()
        self.assertTrue(sudoku.validate())
