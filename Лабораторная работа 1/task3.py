players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Находим общее количество игроков в списке
len_of_players = len(players)
# Находим индекс середины для слайсирования
player_middle_index = len_of_players // 2

# При слайсировании слева направо индексация начинается с 0
# При слайсировании не включается правая граница
first_team = players[:player_middle_index]
second_team = players[player_middle_index:]

print(first_team)
print(second_team)
