# 2.3[14]: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
# Примеры/Тесты:
# 10 ->
# 1
# 2
# 4
# 8
# (*) Усложнение. Вывод оформить в одну строку: числа выводить через запятую. 
# Для этого воспользоваться параметрами функции print
# Примеры/Тесты:
# 10     -> 1,2,4,8,
# 10000  -> 1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,

n = int(input("Введите число: "))
i = 0
while pow(2,i) < n:
    print(pow(2,i))
    i += 1
    