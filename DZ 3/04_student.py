# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

# TODO здесь ваш код
i = 1
expenses_sum = 0
expenses_rost = expenses
while i <= 10:
    expenses_rost = expenses_rost + (expenses_rost * 0.03)
    expenses_sum = expenses_sum + expenses_rost
    i += 1
summa_dohod = educational_grant * i
print(round(expenses_sum - summa_dohod,2) )
