#
from random import randint
# class Lion:
# #     def __init__(self,name):
# #         self.name = name
# #
# #     def __repr__(self):
# #         return f"Этот обект Lion - {self.name}"
# #
# #     def __str__(self):
# #         return f"Это Lion с именем  - {self.name}"
# #
# #
# #
# # w = Lion('Вася')
# #
# # print(w)
# # Тут я поучил __STR__ - Это чтобы имя выводилось правильно
# # Repr чтобы выводилось правильно название объекта,
# # а точнее было А144324А__324324 а станет если пропишим в return "Это объект такой то"
#
# # a = [4,5,34]
# # s = 'asd'
#
# # print(type(a))
#
# # print(isinstance(4,int))
#
# #Классы - например лист
# #создадим класс кар обяательно с большойбуквы
#
#
# # class Car:
# #     model = 'BMW'
# #     engine = 1,6
# #
# # a = Car()
# # b = Car()
# # c = Car()
# # print(c)
# # print(a  ,'and', b,  )
#
# import pprint
# #Урок 2
# # class Person:
# #     name = 'Ivan'
# #     age = 30
# #
# # Person.name = 'Misha'
# #
# # print(Person.name)
#
#  # Урок 4
#
# # class Car:
# #     model  = 'BMW'
# #     engine = 1.5
# #
# #     def drive():
# #         print('Поехали')
# #
# # a = Car
# #
# # print( a.drive())
#
# # Урок 5-6
#
# class Cat:
#     breed = 'pers'
#
#     def __init__(self, name , breed = 'persids' , age = 1 , color = 'white'):
#         print('Hello new object is ' , self ,name , breed , age , color)
#         self.name = name
#         self.age = age
#         self.breed = breed
#         self.color = color
#
#     def __str__(self):
#         return (f'Hello new object is , {self.name} ')
#
#
#
# kelly = Cat(name='Kally',age = 222)
#
# print(kelly.name)



# class Toyota:
#
#     def __init__(self):
#         self.color = "Бордовый металлик"
#         self.price = "1 000 000 руб"
#         self.max_velocity = "200 км/ч"
#         self.current_velocity = "0 км/ч"
#         self.engine_rpm = 0
#
#     def start(self):
#         self.engine_rpm = 5000
#
#     def go(self):
#         self.current_velocity = "20 км/ч"

import  pprint

# class TankRus:
#
#     def __init__(self,name ):
#         self.name = name
#         self.color = 'цвет : Маскировка'
#         self.price = 'цена:' + str(randint(124, 1234)) + ' милионов рублей'
#         self.maxgun = 'Прицельный выстрел ' + str(randint(110,600)) + 'км'
#         self.speed_max = 'Макс скорость ' + str(randint(100,180)) + 'км/час'
#         self.speed_now = 0
#         self.taxometr = 0
#
#     def maxspeed(self):
#         self.speed_now = 120
#         self.taxometr = 8000
#
#     def star(self):
#         self.taxometr = 1300
#
#     def __str__(self):
#         return f'Перед вами такн - {self.name , self.color, self.price ,self.maxgun, self.speed_max} , у него ' \
#                f'характеристики.' f'Текущая скорость - {self.speed_now} ,его обороты - { self.taxometr} '
#
# t90 = TankRus(name= 't900' )
# t90.maxspeed()
# print(t90)



# Класс - это как лекало для производства объектов.
# produced, plan = 0, 10000
# stock = []
# while produced < plan:
#     new_car = Toyota()
#     stock.append(new_car)
#     produced += 1

#
#
# now, plan = 0 , 5
# garage = []
# while now < plan:
#     newname = 't-' + str(randint(1, 400))
#     tank = TankRus(name = newname)
#     garage.append(tank)
#     now += 1
#     print(TankRus(name = newname))
import self as self

from random import randint


class ManFisik:

    def __init__(self, name):
        self.name = name
        self.hangri = 50
        self.food = 50
        self.mani = 100

    def eat (self):
        if self.food >= 10:
            print('{} поел'.format(self.name))
            self.food -= 10
            self.hangri += 10
        else:
            print('{} нет еды'.format(self.name))

    def work (self):
        print('{} сходил на работу'.format(self.name))
        self.mani += 1
        self.hangri -= 10

    def game (self):
        print('{} играл в Доту2'.format(self.name))
        self.hangri -=10

    def shopping(self):
        if self.mani >= 50:
            print('{} пошёл купить еды'.format(self.name))
            self.food += 50
            self.mani -= 50
        else:
            print('{} нет денег купить еду, денег осталось {}'.format(self.name,self.mani))

    def action (self):
        if self.hangri <=0:
            print('{} умер голодной смертью'.format(self.name))
            return
        kubik = randint(1,6)
        if self.hangri <= 20:
            self.eat()
        elif self.food <= 10:
            self.shopping()
        elif self.mani <= 50:
             self.work()
        elif kubik == 1:
            self.work()
        elif kubik == 3:
            self.eat()
        else:
            self.game()

    def __str__(self):
        return '{}, сейчас еды {},голод {},деньги {}'.format(self.name,self.food,self.hangri,self.mani)

menone = ManFisik(name='Anton')

for day in range(1,360):
    print('===================== день {} ================='.format(day))
    menone.action()
    print(menone)






















