import unittest
from sudoku import Sudoku


class TestSudoku(unittest.TestCase):
    def setUp(self) -> None:
        self.sudoku = Sudoku()

    def test_validate_with_valid_board(self) -> None:
        self.assertTrue(self.sudoku.validate(), "Initial board should be valid")

    def test_validate_with_invalid_board(self) -> None:
        self.sudoku.set_empty_cells(0)
        self.sudoku.board[0][0] = self.sudoku.board[1][1]
        self.assertFalse(self.sudoku.validate(), "Modified board should be invalid")

    def test_insert_number(self) -> None:
        self.sudoku.insert_number(0, 0, 5)
        self.assertEqual(
            self.sudoku.board[0][0], 5, "Number should be inserted correctly"
        )

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
        self.assertEqual(len(new_sudoku), 16)
        self.assertEqual(len(new_sudoku[0]), 16)

    def test_set_empty_cells(self) -> None:
        self.sudoku.set_empty_cells(10)
        empty_cells = sum(row.count(0) for row in self.sudoku.board)
        self.assertEqual(empty_cells, 10)

    def test_str_method(self) -> None:
        self.sudoku.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        expected_output = "[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9]"
        actual_output = str(self.sudoku)

        self.assertEqual(
            actual_output,
            expected_output,
            "String representation of the board is not as expected",
        )
