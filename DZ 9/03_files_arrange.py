# -*- coding: utf-8 -*-



# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

#логика
#сначало заходим в папку, и начинаем смотреть каждый файл.
#У файла смотрим дату Далее смотрим другой файл и его дату , этот файл 2021.10.23 ищим папку года, если есть ,
#заходим в ниё и смотрим месяц если опять совпадение просто копируем файл в папу, если нет совпадений создаём
# папу месяца и туда копируем файл.
#если её нет то создаём папку 2021 и в ниё добавляем месяц соответствующий и копируем туда наш файл.
# и так для каждого файла по очереди.
#Мысли:думаю стоит считывать количество файлов, и принтовать на каком файле мы находимся сейчас из всех файлов
#типо если программа упадёт,то её востановить.с того файла
#Мысль выложить эту программу в сеть , глядишь кто и заданатит =)на ютюб начнём колотить своё портфолио
#


class FasovkaFilov:

    def __init__(self,folder): #файл по умолчанию в кодировке utf -8
        self.folder = folder

    def look_data(self):#смотрит дату у каждого файла построчно и смотрит или создаёт новую папку на выход
        from PIL import Image
        import os
        from datetime import datetime
        import shutil
        self.papka_open = os.listdir(self.folder)
        new_papka = 'C:\\sort_papka' # добавляем название папки
        # os.mkdir(new_papka)  # создаёт папку #наверное не нужна уже так как есть метод os.makedirs(add_papka)
        # print('мы создали папку ', new_papka)
        for file in self.papka_open:
            put_k_file = self.folder+'\\'+file #путь к файлу с файлом
            data_file = os.path.getctime(put_k_file)
            # data_g_m_d = datetime.fromtimestamp(data_file).strftime('%y.%m.%d')
            # data_g_m_d = datetime.fromtimestamp(data_file)
            # print(data_g_m_d)
            i = Image.getdata(data_file)
            print(i)
            # papka_year_proverka = new_papka+'\\'+datetime.fromtimestamp(data_file).strftime('%y')
            # add_papka = papka_year_proverka #создаём путь по первому файлу (пока год,потом месяц)
            # if os.path.exists(papka_year_proverka):
            #     print('такая папкаесть тут ничё не делаем')
            #     shutil.copy(put_k_file, new_papka)
            # else:
            #     os.makedirs(add_papka)
            #     print('мы создали папку', papka_year_proverka)

            # if os.path.exists('сюда путь ')
            # print(os.path.exists(papka_year_proverka)) #мы счиали дату каждого файла
            # print(self.folder+'\\'+file)
            # shutil.copy(put_k_file, new_papka) #копирует файл в раннее созданую папку
            #тут сейчас думаю как запускать код от имени администратора?

    def remainder(self):# остаток файлов ( 120 из 453) и принтовать как файл обработается
        pass

    def __str__(self):
        return f'{self.papka_open}'

# papka = FasovkaFilov(folder='C:\\Users\\admin\\Downloads\\Wallpapers-Assorti17') #для ноута
papka = FasovkaFilov(folder='C:\\Users\Vakaram\\Downloads\\Wallpapers-Assorti17') #для компа
papka.look_data()
print(papka)