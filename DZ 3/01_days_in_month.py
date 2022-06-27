# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
# if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
# if moutn == (1,3,5,7,8,10,12):
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print('Дней в этом месяце 31')
elif month == 4 or month == 6 or month == 9 or month == 11:
    print ('Дней в этом месяце 30')
elif month == 2:
    print('Дней в этом месяце 28 (29 в високосном)' )
else:
    print('Warning Input tolko int and diapazon 1-12')
