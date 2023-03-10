# №1.4[7]. 
# Дано натуральное число. 
# Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# В соответствии с григорианским календарем, год является високосным, если
# его номер кратен 4, но не кратен 100; или если он кратен 400.
# 1. Записать условие для високосного года в одну строку
# 2. Записать условие с использованием двух булевых переменных (по одной для каждой части условия)
# 3. Усложнение [*] Использовать тернарный оператор
# Примеры/Тесты:
# 1900 -> NO
# 2000 -> YES
# 2016 -> YES
# Решение 1
year = int(input("Введите год "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("YES")
else:     
    print("NO")
# Решение 2
print("YES" if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else "NO")
# Решение 3
condition1 = year % 4 == 0 and year % 100 != 0
condition2 = year % 400 == 0 
print("YES" if condition1 or condition2 else "NO")
