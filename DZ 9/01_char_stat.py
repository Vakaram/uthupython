# # -*- coding: utf-8 -*-
#
# # Подсчитать статистику по буквам в романе Война и Мир.
# # Входные параметры: файл для сканирования
# # Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
# #
# # Вывести на консоль упорядоченную статистику в виде
# # +---------+----------+
# # |  буква  | частота  |
# # +---------+----------+
# # |    А    |   77777  |
# # |    Б    |   55555  |
# # |   ...   |   .....  |
# # |    a    |   33333  |
# # |    б    |   11111  |
# # |   ...   |   .....  |
# # +---------+----------+
# # |  итого  | 9999999  |
# # +---------+----------+
# #
# # Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# # Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
#
# #  здесь ваш код
#
# unicl_znch = []
# with open(voina_i_mir, 'r',encoding='utf-8') as file:
#     for line in file:
#         for i in line:
#             if i in unicl_znch:
#                 pass
#             else:
#                 unicl_znch.append(i)
# # print('уникальные значения = ' , unicl_znch)

# # # После выполнения первого этапа нужно сделать упорядочивание статистики
# #  - по частоте по возрастанию
# #  - по алфавиту по возрастанию
# #  - по алфавиту по убыванию
# # Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
#
# stat = {}
# count_bukv = 0
# bukvas = 0
# with open(voina_i_mir, 'r',encoding='utf-8') as file:
#     for line in file:
#         for i in unicl_znch:
#             bukvas = i
#             for i in line:
#               if bukvas == i:
#                     count_bukv += 1
#         stat[bukvas] = count_bukv
#
# with open(voina_i_mir, 'r',encoding='utf-8') as file:
#     text = file.read()
#
#     array = {}
#     for i in text:
#         if not i in array:
#             array[i] = 0
#         else:
#             array[i] += 1
#
# if '\n' in array: del array['\n']
# print(array)
import re
voina_i_mir ='voina-i-mir.txt'

stat ={}
with open(voina_i_mir, 'r',encoding='utf-8') as file:
    for line in file:
        for i in line:
            if i.isalpha():
                if not i in stat:
                   stat[i] = 0
                else:
                    stat[i] += 1
#считали сколько всего повторяются буквы
print('+----------+----------+')
print('|  буква   |  частота |')
print('+----------+----------+')
stat_sortA = {}
#сортируем словарь по А-Я
for i in sorted(stat):
    if re.search(r'[А-Я]',i):
        stat_sortA[i]=stat[i]
#принтуем словарь в красивом виде А-Я
for bukva,count in stat_sortA.items():
    print(f'|{bukva:^10}|{count:^10}|'.format(bukva=bukva,count=count))
#сортируем словарь по а-я
print('+----------+----------+')
stat_sorta = {}
for i in sorted(stat):
    if re.search(r'[а-я]',i):
        stat_sorta[i]=stat[i]

#принтуем словарь в красивом виде А-Я
for bukva,count in stat_sorta.items():
    print(f'|{bukva:^10}|{count:^10}|'.format(bukva=bukva,count=count))

itogo = 0
for i in stat_sortA:
    itogo = itogo + stat_sortA[i]
for i in stat_sorta:
    itogo = itogo + stat_sorta[i]

print('+----------+----------+')
print('|   итого  |{itogo:^10}|'.format(itogo = itogo))
print('+----------+----------+')




























