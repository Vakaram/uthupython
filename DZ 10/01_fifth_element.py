# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем
#
# BRUCE_WILLIS = 42
#
# input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
# leeloo = int(input_data[4])
# result = BRUCE_WILLIS * leeloo
# print(f"- Leeloo Dallas! Multi-pass № {result}!")

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение

# нужно указывать конкретную ошибку
try:
    BRUCE_WILLIS = 42
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS / leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
except ValueError:
    print(f'Не удалось выполнить преобразование наверное вы ввели буквы')
except ZeroDivisionError:
    print('Вероятно вы ввели 0 , на ноль делить нельзя')
except NameError:
    print('Нет такой переменной, кто писал этот код?!')
except IndexError:
    print('Вероятно вы не ввели достаточное количество символов введите не менее 5')


# BRUCE_WILLIS = 42
# input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
# leeloo = int(input_data[4])
# result = BRUCE_WILLIS / leeloo
# print(f"- Leeloo Dallas! Multi-pass № {result}!")

# try:
#     i = 0
#     print(10 / i)
#     print('сделано')
# except ZeroDivisionError:  # указываем имя класса
#     print('нельзя делить на ноль!')
