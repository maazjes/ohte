import unittest
from Sudoku import Sudoku


class TestHelpers(unittest.TestCase):
    def setUp(self):
        self.sudoku = Sudoku()

    def test_generate_sudoku_creates_valid_sudoku(self):
        self.assertTrue(self.sudoku.validate())

    def test_generate_sudoku(self):
        new_sudoku = self.sudoku.generate_sudoku(4)
        self.assertEqual(len(new_sudoku), 16)
        self.assertEqual(len(new_sudoku[0]), 16)

    def test_set_empty_cells(self):
        self.sudoku.set_empty_cells(10)
        empty_cells = sum(row.count(0) for row in self.sudoku.board)
        self.assertEqual(empty_cells, 10)
