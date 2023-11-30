list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Определяем общее количество игроков
total_players = len(list_players)

# Разделяем игроков на две равные команды
team1 = list_players[:total_players // 2]
team2 = list_players[total_players // 2:]

# Выводим каждую команду участников на отдельной строке
print(team1)
print(team2)
