def read_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of cols: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter the element of row {i}: ").split()))
        matrix.append(row)
    return matrix


def print_matrix(matrix_name, matrix):
    print(f"{matrix_name}:")
    for row in matrix:
        print(' '.join(map(str, row)))
    print("--------------------")


def add_matrix(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result


# Main code
matrix1 = read_matrix()
print_matrix("matrix_1", matrix1)

matrix2 = read_matrix()
print_matrix("matrix_2", matrix2)

# Check size compatibility
if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
    matrix_sum = add_matrix(matrix1, matrix2)
    print_matrix("matrix_sum", matrix_sum)
else:
    print("Error! Matrices are not the same size")
    print("--------------------")
