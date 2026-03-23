def find_common_participants(group_1, group_2, splitter=","):
    # Чтобы получить из строки с фамилиями список, воспользуемся методом split
    list_group_1 = group_1.split(splitter)
    list_group_2 = group_2.split(splitter)

    # С помощью set() прерватим список в множество, а с помощью intersection() найдем общих участников обеих групп
    common_participants = list(set(list_group_1).intersection(list_group_2))  # Получаем список общих участников
    common_participants.sort()  # Сортируем список в алфавитном порядке

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверяем работу функции для разделителя, отличного от запятой
participants = find_common_participants(participants_first_group, participants_second_group, "|")
print(f"Общими участниками для обеих групп являются {participants}")
