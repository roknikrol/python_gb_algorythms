# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

try:
    print("Считаем четные и нечетные цифры в числе:\n")
    num = input('Введите целое число: ')
    even = ''
    not_even = ''
    for i in num:
        if int(i) % 2 == 0:
            even += i
        else:
            not_even += i

    print('Четных: ', len(even))
    print('Нечетных: ', len(not_even))
except ValueError:
    print("Нужно ввести целое число, попробуйие вновь")
# if num % 2 == 0:
