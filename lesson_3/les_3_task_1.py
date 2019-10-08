# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

list_big = [i for i in range(2, 100)]
list_small = [i for i in range(2, 10)]
result = []
for i in list_big:
    for k in list_small:
        if i % k == 0:
            result.append(i)

print(list_big)
print(list_small)
print('Список кратных числе: ',list(set(result)))

print('Количество кратных: ',len(set(result))) # ответ
