salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

safety_cushion = 0  # Инициализация подушки безопасности

for month in range(months):
    safety_cushion += spend - salary
    spend *= (1 + increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {safety_cushion:.2f}")
