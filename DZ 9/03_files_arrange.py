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
        import exif
        from exif import Image
        import os
        import shutil
        import sys
        from PIL import Image
        from PIL.ExifTags import TAGS
        from datetime import datetime
        self.papka_open = os.listdir(self.folder)
        new_papka = 'C:\\sort_papka' # добавляем название папки
        # os.mkdir(new_papka)  # создаёт папку #наверное не нужна уже так как есть метод os.makedirs(add_papka)
        # print('мы создали папку ', new_papka)
        for file in self.papka_open:
            self.put_k_file = self.folder+'\\'+file #путь к файлу с файлом .jpeg
            self.data_create_def()
            papka_year_proverka = new_papka+'\\'+self.data_sozdaniya_year
            papka_year_mounth_proverka = papka_year_proverka+'\\'+self.data_sozdaniya_mounth
            if not os.path.exists(papka_year_mounth_proverka):
                os.makedirs(papka_year_mounth_proverka) #создаём папку по го и месяц если такой нет
            shutil.copy(self.put_k_file, papka_year_mounth_proverka) #копируем файл в новую директорию
            # if os.path.exists(papka_year_mounth_proverka):
            #         print('такой путь уже есть и я просто копирую в него файл')
            #         shutil.copy(self.put_k_file, papka_year_mounth_proverka)#копируем файл в существующию директорию
            # else:
            #         print('мы не обнаружили не го не месяц,поэтому создаём папку месяц и туда копируем файл')
            #         os.makedirs(papka_year_mounth_proverka) #создаём папку по го и месяц если такой нет
            #         shutil.copy(self.put_k_file, papka_year_mounth_proverka) #копируем файл в новую директорию




    def remainder(self):# остаток файлов ( 120 из 453) и принтовать как файл обработается
        pass

    def data_create_def(self):
        from PIL import Image
        from PIL.ExifTags import TAGS
        imagename = self.put_k_file
        image = Image.open(imagename)
        exifData = image.getexif()
        for tag_id in exifData:
            tag = TAGS.get(tag_id,tag_id)
            data = exifData.get(tag_id)
            if isinstance(data, bytes):
                data = data.decode()
            vremen_dict ={}
            vremen_dict[tag] = data
            if 'DateTime' in vremen_dict: #потому что первый словарь не содержит дататиме и ломается прога
                data_sozdaniya = vremen_dict['DateTime']
                self.data_sozdaniya_year = data_sozdaniya[:4]
                self.data_sozdaniya_mounth = data_sozdaniya[5:7]
                print(self.data_sozdaniya_year)
                print(self.data_sozdaniya_mounth)


    def __str__(self):
        return f'{self.papka_open}'

# papka = FasovkaFilov(folder='C:\\Users\\admin\\Downloads\\Wallpapers-Assorti17') #для ноута
papka = FasovkaFilov(folder='C:\\Users\Vakaram\\Downloads\\Wallpapers-Assorti17') #для компа
papka.look_data()
print(papka)