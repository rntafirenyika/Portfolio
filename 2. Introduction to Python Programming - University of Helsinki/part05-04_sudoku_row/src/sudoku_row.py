# Takes a two-dimensional array representing a sudoku grid, and an integer referring to a single row, as its arguments.
# Returns True or False, depending on whether the row is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.
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