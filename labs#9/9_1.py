def task2(matrix):
    n = len(matrix)
    center = n // 2
    max_element = matrix[0][0]
    max_pos = (0, 0)
    for i in range(n):
        if matrix[i][i] > max_element:
            max_element = matrix[i][i]
            max_pos = (i, i)
        if matrix[i][n - i - 1] > max_element:
            max_element = matrix[i][n - i - 1]
            max_pos = (i, n - i - 1)
    matrix[max_pos[0]][max_pos[1]], matrix[center][center] = matrix[center][center], matrix[max_pos[0]][max_pos[1]]
    print("Изменённая матрица:")
    for row in matrix:
        print(row)
