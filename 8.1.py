def is_magic_square(matrix):
    n = len(matrix)
    magic_sum = sum(matrix[0])  # Сумма первой строки

    # Проверка сумм строк
    for row in matrix:
        if sum(row) != magic_sum:
            return False

    # Проверка сумм столбцов
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != magic_sum:
            return False

    return True

# Пример использования
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("Это магический квадрат.")
else:
    print("Это не магический квадрат.")
