# Takes a two-dimensional array of integers and a single integer value as its arguments.
# The function then counts how many elements within the matrix match the argument value.
def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for i in range(len(my_matrix)):
        for j in range(len(my_matrix[i])):
            if my_matrix[i][j] == element:
                count += 1
    return count