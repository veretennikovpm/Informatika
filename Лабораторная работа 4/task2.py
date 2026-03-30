import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Откроем файл с входными данными (в режиме чтения по умолчанию)
    with open(INPUT_FILENAME) as input_file:
        # Воспользуемся DictReader, чтобы прочитать значения из CSV файла и вернуть Python словари
        # Используем List Comprehension, чтобы добавить каждый словарь в список
        dictionaries = [dictionary for dictionary in csv.DictReader(input_file)]

    # Откроем файл для полученных данных в режиме записи
    with open(OUTPUT_FILENAME, 'w') as output_file:
        # Воспльзуемся методом dump, чтобы сериализовать данные и записать их в файл
        # Методу dump зададим доп. аргумент indent=4, отвечающий за отступы в 4 пробела
        json.dump(dictionaries, output_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
