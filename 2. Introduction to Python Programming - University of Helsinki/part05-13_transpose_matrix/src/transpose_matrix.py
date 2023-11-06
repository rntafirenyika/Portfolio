# Takes a two-dimensional integer array then transpose the matrix.
def transpose(matrix: list):
    new_matrix = []
    sublist = ""
    for i in range(len(matrix)):
        sublist = ""
        sublist = matrix[i]
        new_matrix.append(sublist[:])
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            if i <= j:
                matrix[i][j] = new_matrix[j][i]
                matrix[j][i] = new_matrix[i][j]