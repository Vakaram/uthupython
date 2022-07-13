# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

#  здесь ваш код

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

class Logi:
    def __init__(self,name_file,encoding = 'utf-8'): #файл по умолчанию в кодировке utf -8
        self.name_file = name_file
        self.encoding = encoding

    def min(self):  # считает статистику
        count = 1
        with open(self.name_file, 'r', encoding=self.encoding) as file:
            for line in file:
                log_minut = line[:17]
                for line in file:
                    if "NOK" in line:
                        vremenaya = line[:17]
                        if log_minut == vremenaya:
                            count = count + 1
                        elif log_minut != vremenaya:
                            print(log_minut,']', count,'раз(а)')
                            count = 1
                            log_minut = line[:17]

    def hour(self):  # считает статистику
        count = 1
        with open(self.name_file, 'r', encoding=self.encoding) as file:
            for line in file:
                log_minut = line[:14]
                for line in file:
                    if "NOK" in line:
                        vremenaya = line[:14]
                        if log_minut == vremenaya:
                            count = count + 1
                        elif log_minut != vremenaya:
                            print(log_minut,']', count,'раз(а)')
                            count = 1
                            log_minut = line[:14]

    def day(self):  # считает статистику
        count = 1
        with open(self.name_file, 'r', encoding=self.encoding) as file:
            for line in file:
                log_minut = line[:11]
                for line in file:
                    if "NOK" in line:
                        vremenaya = line[:11]
                        if log_minut == vremenaya:
                            count = count + 1
                        elif log_minut != vremenaya:
                            print(log_minut,']', count,'раз(а)')
                            count = 1
                            log_minut = line[:11]

    def __str__(self):
        return f'Вы проверяете документ {self.name_file}\n' \
               f'в кодирове {self.encoding} по умолчанию,если ошибка поменяйте кодировку\n' \

events = Logi(name_file= 'events.txt')
events.day()
print(events)