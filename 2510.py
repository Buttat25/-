# 1. Ввод размеров первой матрицы А
rows_A = int(input("Введите количество строк матрицы А: "))
cols_A = int(input("Введите количество столбцов матрицы А: "))

print("Заполнение матрицы А:")
matrix_A = []
for i in range(rows_A):
    row = []
    for j in range(cols_A):
        element = int(input(f"Элемент [{i}][{j}]: "))
        row.append(element)
    matrix_A.append(row)

# 2. Ввод размеров второй матрицы Б
rows_B = int(input("\nВведите количество строк матрицы Б: "))
cols_B = int(input("Введите количество столбцов матрицы Б: "))

print("Заполнение матрицы Б:")
matrix_B = []
for i in range(rows_B):
    row = []
    for j in range(cols_B):
        element = int(input(f"Элемент [{i}][{j}]: "))
        row.append(element)
    matrix_B.append(row)


# Переменная-флаг, чтобы узнать, подошла ли хоть какая-то операция
any_operation_done = False


# 3. НЕЗАВИСИМАЯ ПРОВЕРКА НА СЛОЖЕНИЕ
if rows_A == rows_B and cols_A == cols_B:
    any_operation_done = True
    print("\n=== РЕЗУЛЬТАТ СЛОЖЕНИЯ ===")
    
    sum_result = []
    for i in range(rows_A):
        row = []
        for j in range(cols_A):
            row.append(matrix_A[i][j] + matrix_B[i][j])
        sum_result.append(row)
    
    for row in sum_result:
        print(row)
else:
    print("\n[Сложение невозможно]: Размеры матриц отличаются.")


# 4. НЕЗАВИСИМАЯ ПРОВЕРКА НА УМНОЖЕНИЕ
if cols_A == rows_B:
    any_operation_done = True
    print("\n=== РЕЗУЛЬТАТ УМНОЖЕНИЯ ===")
    
    # Создаем матрицу из нулей нужного размера (строки А на столбцы Б)
    mult_result = []
    for i in range(rows_A):
        row = []
        for j in range(cols_B):
            row.append(0)
        mult_result.append(row)
    
    # Считаем умножение
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                mult_result[i][j] += matrix_A[i][k] * matrix_B[k][j]
    
    for row in mult_result:
        print(row)
else:
    print("\n[Умножение невозможно]: Количество столбцов А не равно количеству строк Б.")


# 5. Если вообще ничего не подошло
if not any_operation_done:
    print("\n[Ошибка]: Эти матрицы нельзя ни сложить, ни перемножить.")
