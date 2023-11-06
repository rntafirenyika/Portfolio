# Takes a two-dimensional array representing a sudoku grid as its argument.
# Determines whether the complete sudoku grid is filled in correctly.

# Check row
def row_correct(sudoku: list, row_num: int):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in nums:
        count = 0
        for i in sudoku[row_num]:
            if i == num:
                count += 1
        if count > 1:
            return False
    return True

# Check column
def column_correct(sudoku: list, column_no: int):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in nums:
        count = 0
        for i in range(len(sudoku)):
            if sudoku[i][column_no] == num:
                count += 1
        if count > 1:
            return False
    return True
    
# Check block    
def block_correct(sudoku: list, row_no: int, column_no: int):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in nums:
        count = 0
        for i in range(row_no, row_no + 3):
            for j in range(column_no, column_no + 3):
                if sudoku[i][j] == num:
                    count += 1
        if count > 1:
            return False
    return True

# Check grid
def sudoku_grid_correct(sudoku: list):
    indexes = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for index in indexes:
        if not block_correct(sudoku, index[0], index[1]) or not row_correct(sudoku, index[0]) or not column_correct(sudoku, index[1]):
            return False
    return True