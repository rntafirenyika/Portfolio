#Goes through the matrix in the file, and then returns the sum of the elements.
def matrix_sum():
    msum = 0
    with open("matrix.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            rows = line.split(",")
            for row in rows:
                row = int(row)
                msum += row
    return msum

#Goes through the matrix in the file, and then returns the element with the greatest value.
def matrix_max():
    mmax = []
    with open("matrix.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            rows = line.split(",")
            for row in rows:
                row = int(row)
                mmax.append(row)
    return max(mmax)

#Returns a list containing the sum of each row in the matrix.
def row_sums():
    rows_sums = []
    with open("matrix.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            rows = line.split(",")
            row_sum = 0
            for row in rows:
                row = int(row)
                row_sum += row
            rows_sums.append(row_sum)
    return rows_sums
