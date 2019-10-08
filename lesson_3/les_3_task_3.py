#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

import random

list_1 = [random.randrange(1, 100) for i in range(10)]

# найти максимальное  и минимальное значение
min_num = max_num = list_1[0]
for i in list_1[1:]:
    if i < min_num:
        min_num = i
    elif i > max_num:
            max_num = i


print(list_1)
print(max_num)
print(min_num)
# смена мест не получилась
new_list = []
for i, item in enumerate(list_1[:]):
    if item == max_num:
        list_1.remove(item)
        new_list = list_1[:i] + [min_num] + list_1[i:]
for i, item in enumerate(list_1[:]):
    if item == min_num:
        list_1.remove(item)
        new_list = list_1[:i] + [max_num] + list_1[i:]

print(new_list)
