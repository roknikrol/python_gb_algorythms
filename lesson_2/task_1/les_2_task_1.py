# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
# вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для
# вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если
# пользователь вводит неверный знак (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова
# запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его
# в качестве делителя.

print("Программа  сложения, умножения, вычитания и деления двух чисел.")
while True:
    cmd = input("Введите символ операции: \n"
                "+ для сложения;\n"
                "- для вычитания;\n"
                "* для умножения;\n"
                "/ для деления;\n"
                "0 для выхода из программы.\n")
    if cmd not in '+-*/0':
        print("неверный символ оператора, введите заново")
        continue
    if cmd == '0':
        print()
        print('Выход')
        exit()
    try:
        num_1 = int(input('Введите 1ое число: '))
        num_2 = int(input('Введите 2ое число: '))
    except ValueError:
        print('\nВведите число\n')
        continue
    if cmd == '+':
        result = num_1 + num_2
    elif cmd == '-':
        result = num_1 - num_2
    elif cmd == '*':
        result = num_1 * num_2
    elif cmd == '/':
        if num_2 == 0:
            print('Деление на ноль запрещено законом. Введите заново!')
            continue
        else:
            result = num_1 / num_2
    print(f'Ответ = {result}\n')

