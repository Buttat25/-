# 1. Запрос размера матриц
N = int(input("Введите размер квадратных матриц (например, 3, 4): "))

# 2. Ручной ввод матрицы A
print(f"\nВведите матрицу A ({N} строки, по {N} чисел через пробел):")
A = []
for i in range(N):
    line = input(f"Строка {i+1}: ").split()
    row = []
    for item in line:
        row.append(float(item))
    A.append(row)

# 3. Ручной ввод матрицы B
print(f"\nВведите матрицу B ({N} строки, по {N} чисел через пробел):")
B = []
for i in range(N):
    line = input(f"Строка {i+1}: ").split()
    row = []
    for item in line:
        row.append(float(item))
    B.append(row)


print("\n=== ВЫЧИСЛЕНИЕ ОПРЕДЕЛИТЕЛЕЙ (Метод Гаусса) ===")

# --- Определитель матрицы A ---
# Создаем копию матрицы A, чтобы не испортить оригинал
A_copy = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(A[i][j])
    A_copy.append(row)

det_A = 1.0
for i in range(N):
    pivot = i
    for j in range(i + 1, N):
        # Самодельный аналог abs() для поиска максимального элемента
        val1 = A_copy[j][i]
        if val1 < 0: val1 = -val1
        val2 = A_copy[pivot][i]
        if val2 < 0: val2 = -val2
        
        if val1 > val2:
            pivot = j
            
    if pivot != i:
        A_copy[i], A_copy[pivot] = A_copy[pivot], A_copy[i]
        det_A *= -1
        
    if A_copy[i][i] == 0:
        det_A = 0.0
        break
        
    det_A *= A_copy[i][i]
    
    for j in range(i + 1, N):
        factor = A_copy[j][i] / A_copy[i][i]
        for k in range(i, N):
            A_copy[j][k] -= factor * A_copy[i][k]

print(f"Определитель матрицы A: {det_A}")


# --- Определитель матрицы B ---
# Создаем копию матрицы B
B_copy = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(B[i][j])
    B_copy.append(row)

det_B = 1.0
for i in range(N):
    pivot = i
    for j in range(i + 1, N):
        val1 = B_copy[j][i]
        if val1 < 0: val1 = -val1
        val2 = B_copy[pivot][i]
        if val2 < 0: val2 = -val2
        
        if val1 > val2:
            pivot = j
            
    if pivot != i:
        B_copy[i], B_copy[pivot] = B_copy[pivot], B_copy[i]
        det_B *= -1
        
    if B_copy[i][i] == 0:
        det_B = 0.0
        break
        
    det_B *= B_copy[i][i]
    
    for j in range(i + 1, N):
        factor = B_copy[j][i] / B_copy[i][i]
        for k in range(i, N):
            B_copy[j][k] -= factor * B_copy[i][k]

print(f"Определитель матрицы B: {det_B}")


print("\n=== ОПЕРАЦИИ С МАТРИЦАМИ ===")

# 4. Сложение матриц
matrix_sum = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(A[i][j] + B[i][j])
    matrix_sum.append(row)

print("Сумма матриц (A + B):")
for row in matrix_sum:
    print(row)

# 5. Перемножение матриц
matrix_mul = []
for i in range(N):
    row = []
    for j in range(N):
        cell_value = 0
        for k in range(N):
            cell_value += A[i][k] * B[k][j]
        row.append(cell_value)
    matrix_mul.append(row)

print("\nПроизведение матриц (A * B):")
for row in matrix_mul:
    print(row)


print("\n=== ВЕКТОРЫ И ИХ ПРОИЗВЕДЕНИЯ ===")

# 6. Разложение первой матрицы по строкам
vectors_A = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(A[i][j])
    vectors_A.append(row)

# 7. Разложение второй матрицы по столбцам
vectors_B = []
for j in range(N):
    col = []
    for i in range(N):
        col.append(B[i][j])
    vectors_B.append(col)

# 8. Попарное вычисление скалярного и векторного (тензорного) произведения
for i in range(N):
    vA = vectors_A[i]
    vB = vectors_B[i]
    
    # --- Скалярное произведение вручную ---
    dot_product = 0
    for k in range(N):
        dot_product += vA[k] * vB[k]
        
    print(f"\nПара {i+1} (Строка {i+1} из A и Столбец {i+1} из B):")
    print(f"  Вектор строки A:  {vA}")
    print(f"  Вектор столбца B: {vB}")
    print(f"  Скалярное произведение: {dot_product}")
    
    # --- Векторное (тензорное/внешнее) произведение вручную ---
    # Оно работает для ЛЮБОГО размера N (3, 4, 5 и больше)
    cross_matrix = []
    for r in range(N):
        outer_row = []
        for c in range(N):
            # Перемножаем каждый элемент строки A с каждым элементом столбца B
            outer_row.append(vA[r] * vB[c])
        cross_matrix.append(outer_row)
        
    print("  Векторное (тензорное) произведение (матрица NxN):")
    for row in cross_matrix:
        print(row)
