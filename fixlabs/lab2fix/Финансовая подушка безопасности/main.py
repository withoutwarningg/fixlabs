money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0  # Инициализация счетчика месяцев

while money_capital > 0:  # Пока у нас есть деньги, продолжаем считать
    months += 1  # Увеличиваем счетчик месяцев
    money_capital = money_capital + salary - spend  # Рассчитываем оставшийся капитал после вычета трат
    spend = spend * (1 + increase)  # Увеличиваем траты из-за ежемесячного роста цен

print("Количество месяцев, которое можно протянуть без долгов:", months-1)  # Вычитаем 1, так как в последний месяц у нас уже не будет денег
