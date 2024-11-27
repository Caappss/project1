def read_matrices_from_file(filename):
    matrices = []
    with open(filename, 'r') as file:
        current_matrix = []
        for line in file:
            line = line.strip()
            if line:  # если строка не пустая
                current_matrix.append(list(map(int, line.split())))
            else:  # если пустая строка, значит, заканчивается текущая матрица
                if current_matrix:
                    matrices.append(current_matrix)
                    current_matrix = []
        if current_matrix:  # добавляем последнюю матрицу, если она есть
            matrices.append(current_matrix)
    return matrices


def write_matrices_to_file(filename, matrices):
    with open(filename, 'w') as file:
        for matrix in matrices:
            for row in matrix:
                file.write(' '.join(map(str, row)) + '\n')
            file.write('\n')  # добавляем пустую строку между матрицами


def main():
    input_filename = 'ФИО_группа_vvod.txt'
    output_filename = 'ФИО_группа_vivod.txt'

    # Читаем матрицы из файла
    matrices = read_matrices_from_file(input_filename)

    # Записываем матрицы в выходной файл
    write_matrices_to_file(output_filename, matrices)


if __name__ == '__main__':
    main()
