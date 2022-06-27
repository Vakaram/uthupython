#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['grandf','i','grandm']
my_family.append('by')

# список списков приблизителного роста членов вашей семьи
my_family_height = [['grandf','190'],['i','180'],['grandm','150']
]
# Выведите на консоль рост отца в формате
#   Рост деда - ХХ см
print('Рост деда', my_family_height[0][1], 'cm')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
gf = int(my_family_height[0][1])
i = int(my_family_height[1][1])
gm = int(my_family_height[2][1])

sumrost = gf+i+gm
print('Общий рост семьи', sumrost, 'cm')
