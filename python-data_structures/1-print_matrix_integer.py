def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print(' '.join('{:d}'.format(j)for j in i))
        """  if matrix is None:
        print("")
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print("{:d}".format(matrix[i][j]), end="")
                if j != len(matrix[i]) - 1:
                    print(" ", end="")
                    print("") """
    """ for row in matrix:
        for column in row:
            if column == row[-1]:
                print('{:d}'.format(column), end=' ')
            else:
                print('{:d}'.format(column), end=' ')
        print() """