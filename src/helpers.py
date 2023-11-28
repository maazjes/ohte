import random

# Pattern that ensures that no rules of sudoku are broken when placing numbers by row and column


def pattern(row, column, base): return (
    base*(row % base)+row//base+column) % (base**2)

# Randomize rows, columns and numbers (of valid base pattern)


def shuffle(s): return random.sample(s, len(s))

# Generate a random sudoku of size base^2 * base^2


def generate_sudoku(base, empty_cells):
    rBase = range(base)
    # Shuffle rows and columns ensuring that no rules of sudoku are broken
    rows = [g*base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g*base + c for g in shuffle(rBase) for c in shuffle(rBase)]
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