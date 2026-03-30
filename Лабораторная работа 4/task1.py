import json


FILENAME = "input.json"


def task() -> float:
    # Откроем файл с исходными данными (в режиме чтения по умолчанию)
    with open(FILENAME) as file:
        # Выполним чтение данных и их десериализацию из json в объект Python
        data = json.load(file)

    # Циклом for пройдемся по каждому словарю и получим значения для умножения по ключам "score" и "weight"
    # Используем List Comprehension, чтобы получить список произведений (в одну строку)
    list_values = [(value["score"] * value["weight"]) for value in data]
    sum_list_values = sum(list_values)  # Находим сумму элементов списка произведений

    return round(sum_list_values, 3)  # Округляем значение до 3-х знаков


print(task())
