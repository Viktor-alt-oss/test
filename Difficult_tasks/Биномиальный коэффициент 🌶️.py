# Напишите функцию compute_binom(n, k), которая принимает в качестве аргументов два натуральных числа n и k и 
# возвращает значение биномиального коэффициента, равного 𝑛! / 𝑘!(𝑛 − 𝑘)!.

# объявление функции
from math import factorial
def compute_binom(n, k):
    return round(factorial(n) / (factorial(k) * factorial(n - k)))

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))