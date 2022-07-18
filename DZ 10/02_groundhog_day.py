# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint
ENLIGHTENMENT_CARMA_LEVEL = 777
def one_day(carma_now=0):
    ENLIGHTENMENT_CARMA_LEVEL = 777
    all_day = 0
    list_random = ['IamGodError','DrunkError','CarCrashError','GluttonyError','DepressionError','SuicideError',]
    while carma_now <= ENLIGHTENMENT_CARMA_LEVEL:
        add_karm = randint(1, 7)
        carma_now += add_karm
        print(f'Карма прибавилась на {add_karm} и стала {carma_now}')
        all_day += 1
        dice = randint(1,13)
        if dice == 1:#или любое число чтобы была вероятность 1 к 13
            try:
                now_error = list_random[randint(0,5)] #выбираем рандомно наше исключение если выпало число 1
                raise Exception(now_error)
            except Exception as exc:
                peremennaya_error = f'{exc.args}\n'
                print(f'Наше исключение {peremennaya_error}')
                file_log = open('logirovanie.txt','a',encoding= 'utf-8')
                file_log.write(peremennaya_error)
    else:
        print(f'Мы выбрались из дня сурка кармы стало {carma_now}')
        print(f'Дней затрачено {all_day}')
day_surka = one_day()
print(day_surka)
