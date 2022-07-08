# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self, food=100, dirt=0, money = 100,food_cat = 30):
        self.food_cat = food_cat
        self.food = food
        self.dirt = dirt
        self.money = money

    def __str__(self):
        return f'Еды в доме {self.food}, грязи в доме {self.dirt}, денег в доме {self.money}'

class People:

    def __init__(self, name, house, hunger=100, happy=100):
        self.name = name
        self.house = house
        self.hunger = hunger
        self.happy = happy

    def __str__(self):
        return 'Имя {}, сытость {}, счатье {} '.format(self.name, self.hunger, self.happy)

    #попробую тут записать фунцию для всех людей для глажки кота =)
    def gladit_cota(self):
        self.happy += 5

class Husband(People):

    def __init__(self, name, house, hunger=100, happy=100):
        super().__init__(name, house, hunger=100, happy=100)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.house.dirt >90:
            self.happy -= 10
        self.happy -= 10 #добавил что каждый день падает настроение

        if self.hunger == 0:
            print('Персонаж {} умер'.format(self.name))
        elif self.happy <=10:
            self.wot()
        elif self.hunger <= 30:
            self.eat()
        elif self.house.money <= 600 :
              self.job()



    def eat(self):
        self.hunger += 30
        self.house.food -= 30

    def wot(self):
        self.hunger -= 10
        self.happy += 20

    def job(self):
        self.hunger -= 10
        self.house.money += 150

class Wife(People):

    def __init__(self, name, house, hunger=100, happy=100,shuba = 0):
        super().__init__(name, house, hunger=100, happy=100)
        self.shuba = shuba

    def __str__(self):
        a = super().__str__()
        return a + f' шубы = {self.shuba}'

    def act(self):
        self.house.dirt += 5 #добавляю что кажлый день происходи прибавка
        self.happy -= 10
        if self.house.dirt >90:
            self.happy -= 10

        chislo = randint(1,6)
        if  self.hunger <= 30:
            self.eat()
        elif self.happy <= 50 and self.house.money >= 350:
            self.buy_shuba()
        elif self.house.food <= 0 and self.house.money >= 150 :
            self.buy_food()
        elif self.house.dirt >= 90:
            self.uborka()
        else:
            pass #отдыхала



    def eat(self):
        self.hunger += 30
        self.house.food -= 30

    def uborka(self):
        self.hunger -= 10
        self.house.dirt -= self.house.dirt

    def buy_food (self):
        self.hunger -= 10
        self.house.money -= 60
        self.house.food += 60

    def buy_shuba(self):
        self.hunger -= 10
        self.happy += 60
        self.shuba += 1
        self.house.money -=350

class HomeAnimals:

    def __init__(self,name,house,sitost_cat = 30):
        self.house = house
        self.sitost_cat = sitost_cat
        self.name = name

    def __str__(self):
        return 'Имя {}, сытость {} '.format(self.name, self.sitost_cat)


class Cat(HomeAnimals):

    def __init__(self,name,house,sitost_cat=30):
        # super(HomeAnimals,self).__init__(self,name,house,sitost_cat = 30)
        self.name = name
        self.house = house
        self.sitost_cat = sitost_cat

    def __str__(self):
        return super().__str__()


    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def drat_oboi(self):
        pass


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
murka = Cat(name='Мурка', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    murka.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')
    cprint(murka, color='cyan')
    if serge.happy <= 10 or serge.hunger < 0:
        print(serge.name , 'умер')
        break
    elif masha.happy <= 10 or masha.hunger < 0:
        print(masha.name , 'умерла')
        break


# print( 'Самый нижний принт серега', serge )

# ODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов
#
#
# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass
#
# # пробую пушить в новую ветку
# ######################################################## Часть вторая бис
# #
# # После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
# #
# # Ребенок может:
# #   есть,
# #   спать,
# #
# # отличия от взрослых - кушает максимум 10 единиц еды,
# # степень счастья  - не меняется, всегда ==100 ;)
#
# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#
# # TOO после реализации второй части - отдать на проверку учителем две ветки
#
#
# ######################################################## Часть третья
# #
# # после подтверждения учителем второй части (обоих веток)
# # влить в мастер все коммиты из ветки develop и разрешить все конфликты
# # отправить на проверку учителем.
#
#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')
#
#
# # Усложненное задание (делать по желанию)
# #
# # Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# # Коты должны выжить вместе с семьей!
# #
# # Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# # Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
# #
# # Дополнительно вносить некий хаос в жизнь семьи
# # - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# # - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# # Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
# #   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
# #
# # в итоге должен получится приблизительно такой код экспериментов
# # for food_incidents in range(6):
# #   for money_incidents in range(6):
# #       life = Simulation(money_incidents, food_incidents)
# #       for salary in range(50, 401, 50):
# #           max_cats = life.experiment(salary)
# #           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
#
