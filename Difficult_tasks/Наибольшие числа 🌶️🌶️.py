#На вход программе подается натуральное число n, а затем n различных натуральных чисел последовательности, каждое на отдельной строке. 
# Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.

n = int(input())

max1, max2 = -1, -1

for _ in range(n):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num
        
print(max1)
print(max2)