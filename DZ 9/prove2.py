import re
voina_i_mir ='voyna-i-mir.txt'
stat ={}
with open(voina_i_mir, 'r',encoding='cp1251') as file:
    for line in file:
        for i in line:
            if i.isalpha():
                if not i in stat:
                   stat[i] = 0
                else:
                    stat[i] += 1
#считали сколько всего повторяются буквы
print('+----------+----------+')
print('|  буква   |  частота |')
print('+----------+----------+')
stat_sortA = {}
#сортируем словарь по А-Я
for i in sorted(stat):
    if re.search(r'[А-Я]',i):
        stat_sortA[i]=stat[i]
#принтуем словарь в красивом виде А-Я
for bukva,count in stat_sortA.items():
    print(f'|{bukva:^10}|{count:^10}|'.format(bukva=bukva,count=count))
#сортируем словарь по а-я
print('+----------+----------+')
stat_sorta = {}
for i in sorted(stat):
    if re.search(r'[а-я]',i):
        stat_sorta[i]=stat[i]

#принтуем словарь в красивом виде А-Я
for bukva,count in stat_sorta.items():
    print(f'|{bukva:^10}|{count:^10}|'.format(bukva=bukva,count=count))

#Считаем итого
itogo = 0
for i in stat_sortA:
    itogo = itogo + stat_sortA[i]
for i in stat_sorta:
    itogo = itogo + stat_sorta[i]

print('+----------+----------+')
print('|   итого  |{itogo:^10}|'.format(itogo = itogo))
print('+----------+----------+')