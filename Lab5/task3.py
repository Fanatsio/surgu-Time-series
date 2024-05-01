import numpy as np

def read_data(filename):
    """
    Чтение данных из файла и преобразование их в массив NumPy.

    Parameters:
    filename (str): Имя файла с данными.

    Returns:
    numpy.ndarray: Массив данных.
    """
    data = []
    with open(filename, 'r') as file:
        next(file)  # Пропускаем заголовок
        for line in file:
            row = line.strip().split(';')
            # Преобразуем строки в числа, пропуская пустые значения
            data.append([float(val) for val in row[1:] if val.strip()])
    return np.array(data)

def fft(data):
    """
    Реализация быстрого преобразования Фурье (БПФ).

    Parameters:
    data (numpy.ndarray): Входной массив данных.

    Returns:
    numpy.ndarray: Результат БПФ.
    """
    return np.fft.fft(data)

def ifft(data):
    """
    Реализация обратного быстрого преобразования Фурье (обратное БПФ).

    Parameters:
    data (numpy.ndarray): Входной массив данных.

    Returns:
    numpy.ndarray: Результат обратного БПФ.
    """
    return np.fft.ifft(data)

if __name__ == "__main__":
    filename = 'lab5_data4.txt'
    data = read_data(filename)

    fft_result = fft(data)
    print("Результат БПФ:")
    print(fft_result)

    ifft_result = ifft(fft_result)
    print("\nРезультат обратного БПФ:")
    print(ifft_result)
