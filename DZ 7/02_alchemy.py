# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава





# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# # TODO здесь ваш код
#
# class Water:
#     'Element'
#
#     def __init__(self,second = second ):
#         self.stalo = [water, ]
#         if second == Air:
#             self.stalo.append(second)
#
# class Water:
#     'Вода'
#
#
# class Air:
#     'Воздух'
#
#
# class Storm:
#     'Шторм'
#
#
# class Steam:
#     'Пар'
#
#
# class Dirt:
#     'Грязь'
#
#
# class Lightning:
#     'Молния'
#
#
# class Dust:
#     'Пыль'
#
#
# class Lava:
#     'Лава'
#

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.







class Toyota:

    color = 0

    def __init__(self,name):
        self.name = "Tayota"

    def colort(self):
        print(self, ' Зелёный')

    def __str__(self):
        return str(self.name)

    def __repr__(self):


my_car = Toyota

print(Toyota.colort)

