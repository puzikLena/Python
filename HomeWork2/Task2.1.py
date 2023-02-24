# 2.1[10]: 
# На столе лежат n монеток.
#  Некоторые из них лежат вверх решкой, а некоторые – гербом.
#   Определите минимальное число монеток, которые нужно перевернуть, 
#   чтобы все монетки были повернуты вверх одной и той же стороной. 
#   Выведите минимальное количество монет, которые нужно перевернуть.
#    Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.
# Примеры/Тесты:
# Введите кол-во монет>? 5
# Положение монеты 0: 0 или 1>? 1
# ...
# 1 0 1 1 0
# Кол-во монет, чтобы перевернуть: 2

num = int(input("Введите кол-во монет: "))
coin_side = []
for i in range(num):
    coin_side.append(int(input(f"Положение монеты {i} : 0 или 1>?")))

eagles = []
tails = []
for i in coin_side:
    if i == 1:
        eagles.append(i)
    else:
        tails.append(i)
if len(eagles) > len(tails):
    print(f"Кол-во монет, чтобы перевернуть: {len(tails)}")
if len(tails) > len(eagles):
    print(f"Кол-во монет, чтобы перевернуть: {len(eagles)}")