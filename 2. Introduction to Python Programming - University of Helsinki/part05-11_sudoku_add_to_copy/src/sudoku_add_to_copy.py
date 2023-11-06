# Returns a copy of the original grid with the new digit added in the correct location.
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = []
    sublist = ""
    for i in range(len(sudoku)):
        sublist = ""
        sublist = sudoku[i]
        new_sudoku.append(sublist[:])
    new_sudoku[row_no][column_no] = number
    return new_sudoku