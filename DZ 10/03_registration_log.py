# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

# TODO здесь ваш код

class NotNameError(Exception):
    pass

class NotEmailError(Exception):
    pass

def check(line):
    name, mail, age = line.split(' ')
    symbols = ('@', '.')
    age = int(age)
    if name.isalpha() is False:
        raise NotNameError
    elif age not in range(10,100):
        return ValueError()
    else:
        for char in symbols:
            if char not in mail:
                raise NotEmailError
    return line

with open('registrations.txt', mode='r', encoding='utf-8') as ff:
    for line in ff:
        line = line[:-1]
        try:
            string = check(line)
        except NotNameError:
            bad = open ('registration_bad.log', mode='a', encoding='utf-8')
            bad.write(line + 'Имя содержит цифры' + '\n')
            bad.close()
        except NotEmailError:
            bad = open ('registration_bad.log', mode='a', encoding='utf-8')
            bad.write(line + 'Некорректно указан E-mail' + '\n')
            bad.close()
        except ValueError:
            bad = open ('registration_bad.log', mode='a', encoding='utf-8')
            bad.write(line + 'Неверные данные' + '\n')
            bad.close()
        else:
            good = open('registraton_good.log', mode='a', encoding='utf-8')
            good.write(line + '\n')
            good.close()

ff.close()