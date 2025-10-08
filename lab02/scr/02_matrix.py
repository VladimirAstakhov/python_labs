def is_rectangular(mat: list[list[float | int]]):
    if (len(mat) == 0):
        return -1
    row_size = len(mat[0])
    for row in mat:
        if (len(row) != row_size):
            return 0
    return 1


def transpose(mat: list[list[float | int]]):
    if (is_rectangular(mat) == -1):
        return mat
    if (is_rectangular(mat) == 0):
        return "ValueError"
    row_size = len(mat[0])
    column_size = len(mat)
    mat_transpose = [0] * row_size
    for i in range(0, row_size):
        row = [0] * column_size
        for j in range(0,column_size):
            row[j] = mat[j][i]
        mat_transpose[i] =  row
    return mat_transpose

def row_sums(mat: list[list[float | int]]):
    if (is_rectangular(mat) == -1):
        return mat
    if (is_rectangular(mat) == 0):
        return "ValueError"
    sums = []
    for row in mat:
        sum_in_row = 0
        for element in row:
            sum_in_row += element
        sums.append(sum_in_row)
    return sums
def col_sums(mat: list[list[float | int]]):
    if (is_rectangular(mat) == -1):
        return mat
    if (is_rectangular(mat) == 0):
        return "ValueError"
    column_size = len(mat)
    row_size = len(mat[0])
    sums = []
    for i in range (0, row_size):
        sum_in_column = 0
        for j in range(0, column_size):
            sum_in_column += mat[j][i]
        sums.append(sum_in_column)
    return sums

print("transpose tests")
test_transpose_1 = [[1, 2, 3]]
test_transpose_2 = [[1], [2], [3]]
test_transpose_3 = [[1, 2], [3, 4]]
test_transpose_4 = []
test_transpose_5 = [[1, 2], [3]]
print(transpose(test_transpose_1))
print(transpose(test_transpose_2))
print(transpose(test_transpose_3))
print(transpose(test_transpose_4))
print(transpose(test_transpose_5))

print("row_sums tests")
test_row_sums_1 = [[1, 2, 3], [4, 5, 6]]
test_row_sums_2 = [[-1, 1], [10, -10]]
test_row_sums_3 = [[0, 0], [0, 0]]
test_row_sums_4 = [[1, 2], [3]]
print(row_sums(test_row_sums_1))
print(row_sums(test_row_sums_2))
print(row_sums(test_row_sums_3))
print(row_sums(test_row_sums_4))

print("col_sums tests")
test_col_sums_1 = [[1, 2, 3], [4, 5, 6]]
test_col_sums_2 = [[-1, 1], [10, -10]]
test_col_sums_3 = [[0, 0], [0, 0]]
test_col_sums_4 = [[1, 2], [3]]
print(col_sums(test_col_sums_1))
print(col_sums(test_col_sums_2))
print(col_sums(test_col_sums_3))
print(col_sums(test_col_sums_4))




