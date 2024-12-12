def task1(matrix):
    n = len(matrix)  # Размер матрицы
    max_in_rows = [max(row) for row in matrix]
    min_in_columns = [min(matrix[i][j] for i in range(n)) for j in range(n)]

    print("Максимальные элементы в строках:", max_in_rows)
    print("Минимальные элементы в столбцах:", min_in_columns)