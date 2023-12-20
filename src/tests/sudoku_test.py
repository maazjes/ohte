import unittest
import copy
from sudoku import Sudoku

valid_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]


class TestSudoku(unittest.TestCase):
    def setUp(self) -> None:
        self.sudoku = Sudoku()

    def test_cell_is_valid(self) -> None:
        self.sudoku.board = copy.deepcopy(valid_board)
        self.sudoku.board[0][0] = 0
        self.assertTrue(self.sudoku.cell_is_valid(0, 0, 5))
        self.assertFalse(self.sudoku.cell_is_valid(0, 0, 2))

    def test_validate_with_valid_board(self) -> None:
        self.sudoku.set_empty_cells(0)
        self.assertTrue(self.sudoku.validate(), "Initial board should be valid")
        self.sudoku.board = valid_board
        self.assertTrue(self.sudoku.validate(), "Valid board should be valid")

    def test_validate_with_invalid_board(self) -> None:
        self.sudoku.set_empty_cells(0)
        self.sudoku.board[0][0] = self.sudoku.board[1][1]
        self.assertFalse(self.sudoku.validate(), "Modified board should be invalid")

    def test_insert_number(self) -> None:
        valid = self.sudoku.insert_number(0, 0, self.sudoku.board[0][1])
        self.assertEqual(
            self.sudoku.board[0][0],
            self.sudoku.board[0][1],
            "Number should be inserted correctly",
        )
        self.assertFalse(valid, "Inserted number should be invalid")

    def test_set_base(self) -> None:
        self.sudoku.set_base(4)
        self.assertEqual(
            len(self.sudoku.board), 16, "Board size should change with base"
        )
        self.assertEqual(
            len(self.sudoku.board[0]), 16, "Board size should change with base"
        )

    def test_generate_sudoku(self) -> None:
        new_sudoku = self.sudoku.generate_sudoku(4)
        self.assertEqual(len(new_sudoku), 16, "Amount of rows should be 16")
        self.assertEqual(len(new_sudoku[0]), 16, "Amount of columns should be 16")

    def test_set_empty_cells(self) -> None:
        self.sudoku.set_empty_cells(10)
        empty_cells = sum(row.count(0) for row in self.sudoku.board)
        self.assertEqual(empty_cells, 10, "There should be 10 empty cells")

    def test_str_method(self) -> None:
        self.sudoku.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        expected_output = "[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9]"
        actual_output = str(self.sudoku)

        self.assertEqual(
            actual_output,
            expected_output,
            "String representation of the board is not as expected",
        )
