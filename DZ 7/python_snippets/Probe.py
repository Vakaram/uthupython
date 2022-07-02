from random import random ,randint

name_all = []
chislo = 0
while chislo < 20:
    newname = 't-' +str(randint(1, 999))
    name_all.append(newname)
    chislo += 1
print(name_all)