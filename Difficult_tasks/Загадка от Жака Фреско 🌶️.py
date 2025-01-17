# Однажды Жака Фреско спросили: "Если ты такой умный, почему не богатый?" 
# Жак не стал отвечать на столь провокационный вопрос, вместо этого он задал загадку спрашивающему:

# "Были разноцветные козлы. Сколько?"

# "Сколько чего?"

# "Сколько из них составляет более 7% от общего количества козлов?"

# Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS, далее идет список всех возможных цветов козлов. Затем идет строка со словом GOATS, и далее непосредственно перечисление козлов разных цветов. Перечень козлов включает только строки из первого списка.

# Напишите программу создания файла answer.txt и вывода в него списка козлов, которые удовлетворяют условию загадки от Жака Фреско.

with open('goats.txt') as inp, open('answer.txt', 'w') as out:
    x = inp.read().split('GOATS')
    colours = x[0].split('\n')[1:]
    goats = x[1].split('\n')
    for line in colours:
        if goats.count(line) > len(goats) * 0.07:
            out.write(line + '\n')