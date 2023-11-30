def find_common_participants(participants_first_group, participants_second_group, separator=','):
    set_first_group = set(participants_first_group.split(separator))
    set_second_group = set(participants_second_group.split(separator))
    common_participants = sorted(list(set_first_group.intersection(set_second_group)))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(f"Общие участники: {common_participants}")
