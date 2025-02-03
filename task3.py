# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)

attempts = 10

for attempt in range(1, attempts + 1):
    guess = int(input(f"Попытка {attempt}: Введите число: "))
    
    if guess < num:
        print("Больше")
    elif guess > num:
        print("Меньше")
    else:
        print(f"Вы угадали число {num} с {attempt}-й попытки.")
        break
else:
    print(f"Вы исчерпали 10 попыток. Загаданное число было {num}.")
