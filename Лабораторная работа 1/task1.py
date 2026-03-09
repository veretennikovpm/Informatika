numbers = [
    2, -93, -2, 8, None, -44, -1, -85, -14, 90,
    -22, -90, -100, -8, 38, -92, -45, 67, 53, 25
]

index_of_none = 4  # Находим индекс пропущенного элемента
# Создаем список чисел без пропущенного элемента
numbers_without_none = numbers[:index_of_none] + numbers[index_of_none + 1:]

# Находим сумму чисел списка за исключением пропуска
sum_of_numbers = sum(numbers_without_none)
# Находим количество элементов с учетом пропуска
count_of_numbers = len(numbers)

# Находим среднее арифметическое элементов списка
average_numbers = sum_of_numbers / count_of_numbers
# Заменяем пропущенный элемент списка на найденное среднее арифметическое
numbers[index_of_none] = average_numbers

print("Измененный список:", numbers)
