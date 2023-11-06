# Takes a two-dimensional array representing a sudoku grid, and two integers referring to the row and column indexes of a single square, as its arguments.
# Returns True or False depending on whether the 3 by 3 block to the right and down from the given indexes is filled in correctly.
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