from Sudoku import Sudoku
from helpers import generate_sudoku

sudoku = Sudoku(board=generate_sudoku(3, 10))
print(sudoku)
print(sudoku.solve())