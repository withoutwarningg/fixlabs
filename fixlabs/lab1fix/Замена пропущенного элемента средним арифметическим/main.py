numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Вычисляем сумму всех чисел, включая пропуск
total = sum(x for x in numbers if x is not None)

# Вычисляем количество всех элементов, включая пропуск
count = len(numbers)

# Вычисляем среднее арифметическое всех чисел, включая пропуск
average = total / count

# Заменяем пропуск на среднее арифметическое
numbers = [average if x is None else x for x in numbers]

print("Измененный список:", numbers)