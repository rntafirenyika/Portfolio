# Takes an integer matrix as its argument.
# Adds a new element on each row in the matrix, which contains the sum of the other elements on that row.

def row_sums(my_matrix: list):
    for item in my_matrix:
        item.append(sum(item))
