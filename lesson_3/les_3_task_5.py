# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
#  Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
#  Это два абсолютно разных значения.


import random

list_1 = [random.randrange(-10, 10) for i in range(15)]

print(list_1)
neg_list = []
for i in list_1:
    if i < 0:
        neg_list.append(i)

max_num = neg_list[0]
for i in neg_list[1:]:
    if i > max_num:
        max_num = i

print(f'Максимальное отрицательное {max_num}')
print(sorted(list_1))  # отсортировал чтобы показать где самое максимальное отрицательное
