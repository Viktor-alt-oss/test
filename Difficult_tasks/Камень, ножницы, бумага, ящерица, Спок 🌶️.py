# Проиграв 10 раз Тимуру, Руслан понял, что так дело дальше не пойдет, и решил усложнить игру. 
# Теперь Тимур и Руслан играют в игру Камень, ножницы, бумага, ящерица, Спок. 
# Помогите ребятам вновь бросить честный жребий и определить, кто будет делать следующий модуль в новом курсе.

# Формат входных данных
# На вход программе подаются две строки текста, содержащие по одному слову из перечня "камень", "ножницы", "бумага", "ящерица" или "Спок". 
# На первой строке записан выбор Тимура, на второй – выбор Руслана.

options = ["камень", "ящерица", "Спок", "ножницы", "бумага"]
results = ["ничья", "Руслан", "Тимур", "Руслан", "Тимур"]

timur_move = input()
ruslan_move = input()

case = options.index(timur_move) - options.index(ruslan_move)
res = results[case]

print(res)
