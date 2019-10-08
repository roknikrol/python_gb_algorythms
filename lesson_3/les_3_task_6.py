# 6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным
# элементами. Сами минимальный и максимальный
# элементы в сумму не включать.

import random

list_1 = [random.randrange(1, 10) for i in range(10)]

print(list_1)

min_num = max_num = list_1[0]
for i in list_1[1:]:
    if i < min_num:
        min_num = i
    elif i > max_num:
            max_num = i
max_mix_list = [min_num, max_num]
result = 0

for i in list_1:
    if i not in max_mix_list:
        result += i

print('Сумма чисел не max/min:', result)
