#На числовой прямой даны два отрезка: [a1;b1] и [𝑎2;𝑏2]
#Напишите программу, которая находит их пересечение.
#Пересечением двух отрезков может быть:
#отрезок:
#точка:
#пустое множество:

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a1 <= a2 < b1 <= b2:
    print(a2, b1)
elif a2 <= a1 < b2 <= b1:
    print(a1, b2)
elif a2 < a1 and b1 < b2:
    print(a1, b1)
elif a1 < a2 and b2 < b1:
    print(a2, b2)
elif a1 == a2:
    print(a1)
elif b1 == b2:
    print(b1)
elif a1 == b2:
    print(a1)
elif b1 == a2:
    print(b1)
else:
    print('пустое множество')