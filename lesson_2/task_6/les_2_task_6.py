#6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.

import random

print('Guess a number, you have 10 tries')
num = int(input('Your guess: '))
rand_num = random.randrange(0, 100)
count = 10

while count != 1:
    if num == rand_num:
        print('You guessed!')
        exit()
    elif num > rand_num:
        print('Your number is bigger, try again')
    else:
        print('Your number is smaller, try again')
    count -= 1
    num = int(input(f'{count} tries left. Your guess: '))
print(' You lose  ')
