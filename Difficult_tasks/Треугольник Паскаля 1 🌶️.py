# Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. 
# В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.

# 0:      1
# 1:     1 1
# 2:    1 2 1
# 3:   1 3 3 1
# 4:  1 4 6 4 1
#       .....
# На вход программе подается число 𝑛. Напишите программу, которая возвращает указанную строку треугольника Паскаля в виде списка 
# (нумерация строк начинается с нуля).

from math import factorial 
li = []
n = int(input())
for i in range(n + 1):
    li.append(int(factorial(n) / (factorial(i) * factorial(n - i))))
print(li)

