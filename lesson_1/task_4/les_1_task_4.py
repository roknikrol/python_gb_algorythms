# 	4. Пользователь вводит две буквы.
# 	Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

print('Опеделяем позиции букв в алфавите\n'
      'Только латинские строчные')
x = input('Введите букву 1: ')
y = input('Введите букву 2: ')

x_pos = int(ord(x))-96
y_pos = ord(y)-96

print(f'Буква {x} {x_pos} в алфавите')
print(f'Буква {y} {y_pos} в алфавите')
print(f'Между буквами {y_pos - x_pos} букв')