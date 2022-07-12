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
#                 unicl_znch.append
#                 (i)
# # print('уникальные значения = ' , unicl_znch)

# # # После выполнения первого этапа нужно сделать упорядочивание статистики
# #  - по частоте по возрастанию
# #  - по алфавиту по возрастанию
# #  - по алфавиту по убыванию
# # Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
import re
# voina_i_mir ='voina-i-mir.txt'
# stat ={}
# with open(voina_i_mir, 'r',encoding='utf-8') as file:
#     for line in file:
#         for i in line:
#             if i.isalpha():
#                 if not i in stat:
#                    stat[i] = 0
#                 else:
#                     stat[i] += 1
# print(stat)
# #считали сколько всего повторяются буквы
# print('+----------+----------+')
# print('|  буква   |  частота |')
# print('+----------+----------+')
# stat_sortA = {}
# #сортируем словарь по А-Я
# for i in sorted(stat):
#     if re.search(r'[А-Я]',i):
#         stat_sortA[i]=stat[i]
# #принтуем словарь в красивом виде А-Я
# for bukva,count in stat_sortA.items():
#     print(f'|{bukva:^10}|{count:^10}|'.format(bukva=bukva,count=count))
# #сортируем словарь по а-я
# print('+----------+----------+')
# stat_sorta = {}
# for i in sorted(stat):
#     if re.search(r'[а-я]',i):
#         stat_sorta[i]=stat[i]
#
# #принтуем словарь в красивом виде А-Я
# for bukva,count in stat_sorta.items():
#     print(f'|{bukva:^10}|{count:^10}|'.format(bukva=bukva,count=count))
#
# #Считаем итого
# itogo = 0
# for i in stat_sortA:
#     itogo = itogo + stat_sortA[i]
# for i in stat_sorta:
#     itogo = itogo + stat_sorta[i]
#
# print('+----------+----------+')
# print('|   итого  |{itogo:^10}|'.format(itogo = itogo))
# print('+----------+----------+')


#___________________________________________



class ThisFile:
    import re
    def __init__(self,name_file,encoding = 'utf-8'): #файл по умолчанию
        self.name_file = name_file
        self.codirovka = encoding
        self.stat = {}

    def stat_count(self): #считает статистику
        with open(self.name_file , 'r',encoding = self.codirovka) as file:
            for line in file:
                for i in line:
                    if i.isalpha():
                        if not i in self.stat:
                            self.stat[i] = 0
                        else:
                            self.stat[i] += 1

    def __str__(self):
        return f'Вы проверяете документ {self.name_file}\n' \
               f'в кодирове {self.codirovka} по умолчанию,если ошибка поменяйте кодировку\n' \
               f'+----------+----------+\n'\
               f'|  буква   |  частота |\n' \
               f'+----------+----------+\n' \
               f'{self.bigrusbukv()}\n' \
               f'{self.smallrusbukv()}\n' \
               f'{self.countbukvrus()}\n' \

    def bigrusbukv(self):
        import re
        self.stat_sortA = {}
        for i in sorted(self.stat):
            if re.search(r'[А-Я]',i):
                self.stat_sortA[i]=self.stat[i]
            for bukva, count in self.stat_sortA.items():
                return f'|{bukva:^10}|{count:^10}|'.format(bukva=bukva,count=count)


    def smallrusbukv(self):
        import re
        self.stat_sorta = {}
        for i in sorted(self.stat):
            if re.search(r'[а-я]',i):
                self.stat_sorta[i]=self.stat[i]
            for bukva, count in self.stat_sorta.items():
                a = f'|{bukva:^10}|{count:^10}|'.format(bukva=bukva,count=count)
                return a

    def countbukvrus(self):
        itogo = 0
        for i in self.stat_sortA:
            itogo = itogo + self.stat_sortA[i]
        for i in self.stat_sorta:
            itogo = itogo + self.stat_sorta[i]
        return f'+----------+----------+\n|   итого  |{itogo:^10}|\n'\
               f'+----------+----------+'.format(itogo=itogo)



proverka_file = ThisFile(name_file='voina-i-mir.txt')
proverka_file.bigrusbukv()
proverka_file.smallrusbukv()
proverka_file.stat_count()
proverka_file.countbukvrus()

print(proverka_file)



























