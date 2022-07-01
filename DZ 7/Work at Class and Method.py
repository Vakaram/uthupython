# class Lion:
#     def __init__(self,name):
#         self.name = name
#
#     def __repr__(self):
#         return f"Этот обект Lion - {self.name}"
#
#     def __str__(self):
#         return f"Это Lion с именем  - {self.name}"
#
#
#
# w = Lion('Вася')
#
# print(w)
# Тут я поучил __STR__ - Это чтобы имя выводилось правильно
# Repr чтобы выводилось правильно название объекта,
# а точнее было А144324А__324324 а станет если пропишим в return "Это объект такой то"

a = [4,5,34]
s = 'asd'

# print(type(a))

# print(isinstance(4,int))

#Классы - например лист
#создадим класс кар обяательно с большойбуквы


# class Car:
#     model = 'BMW'
#     engine = 1,6
#
# a = Car()
# b = Car()
# c = Car()
# print(c)
# print(a  ,'and', b,  )

import pprint
#Урок 2
class Person:
    name = 'Ivan'
    age = 30

Person.name = 'Misha'

print(Person.name)