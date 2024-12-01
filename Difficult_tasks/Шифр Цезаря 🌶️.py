# Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям и использует шифр Цезаря.
# Это их и подвело, ведь данный шифр очень простой. 
# Однако в постапокалипсисе люди плохо знают все тонкости довоенного мира, поэтому ученые из НКР не могут понять, 
# как именно нужно декодировать данные сообщения. Напишите программу для декодирования этого шифра.

n = int(input())
s = input()
for c in s:
    k = ord(c) - n
    if k < 97:
        k += 26
    print(chr(k), end='')