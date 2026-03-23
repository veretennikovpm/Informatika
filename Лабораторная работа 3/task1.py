def index_founder(products, item):
    for index in range(len(products)):  # Перебираем индексы элементов списка products
        if products[index] == item:  # Сравниваем элемент, имеющий данный индекс, с искомым товаром
            return index  # Возвращаем индекс первого вхождения и останавливаем работу функции
    # Если товар не найден в списке, функция автоматически вернет None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = index_founder(items_list, find_item)  # Вызываем функцию
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
