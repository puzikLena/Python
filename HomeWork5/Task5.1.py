# 5.1[26]: 
# Напишите рекурсивную функцию для возведения числа a в степень b.
#  Разрешается использовать только операцию умножения. 
# Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16


def exponentiation_of_number(a, b):
    if b == 0:
        return 1
    else:
        return( a * exponentiation_of_number(a, b -1))
print(exponentiation_of_number(2, 0))
