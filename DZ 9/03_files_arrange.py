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




    def remainder(self):# остаток файлов ( 120 из 453) и принтовать счёт файлов
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