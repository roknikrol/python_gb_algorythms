# 4. Определить, какое число в массиве встречается чаще всего.

import random

list_1 = [random.randrange(1, 100) for i in range(100)]
print(list_1)
result_dic = {}
# создать словарь число: количество упоминаний
for i in list_1:
    if i not in result_dic:
        result_dic[i] = 1
    else:
        result_dic[i] += 1
# созданный словарь
print(result_dic)
# найти максимальное значение по счетчику упоминаний
max_num = list(result_dic.values())[0]
for i in list(result_dic.values()):
    if i > max_num:
        max_num = i
# вывести пару
for i,k in result_dic.items():
    if k == max_num:
        print(f'Число {i} встречается {k} раз')