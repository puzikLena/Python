# №1.2[3]. 
# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Примеры/Тесты:
# 20 21 22(ввод чисел НЕ в одну строку) -> Общее кол-во парт будет 32
# 21 21 21(ввод чисел НЕ в одну строку) -> Общее кол-во парт будет 33
ych1 = int(input())
ych2 = int(input())
ych3 = int(input())
ych = ych1 + ych2 + ych3
# if ych % 2 == 0:
#     part = ych // 2
# else: 
#     part = ych // 2 + 1
# print(part)
# Тернарный оператор
part1 = ych1 // 2 if ych1 % 2 == 0 else ych1 // 2 + 1
part2 = ych2 // 2 if ych2 % 2 == 0 else ych2 // 2 + 1
part3 = ych3 // 2 if ych3 % 2 == 0 else ych3 // 2 + 1
sumpart = part1 + part2 + part3
print(sumpart)