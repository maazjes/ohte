from helpers import generate_sudoku

class Sudoku:
    def __init__(self, base = 3, empty_cells = 0, board = None):
        self.base = base
        if board:
            self.board = board
        else:
            self.board = generate_sudoku(base, empty_cells)

    def cell_is_valid(self, row, col, num):
        # Check if the number placed in the given row and column is valid
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num or self.board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True

    def solve(self):
        # Find an empty cell
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    # Try placing a number in the empty cell
                    for num in range(1, 10):
                        if self.cell_is_valid(i, j, num):
                            self.board[i][j] = num
                            # Recursively try to solve the rest of the sudoku
                            if self.solve():
                                return True
                            # If placing the number doesn't lead to a solution, backtrack
                            self.board[i][j] = 0
                    return False
        return True
    
    def __str__(self):
        return "\n".join([str(self.board[i]) for i in range(len(self.board))])