# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр.
# Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.

list = [15, 48, 'hello', 6, 19, 'world']
print(list)
print('Решение')
list.remove('hello')
list.remove('world')
print(list)
sum = 0
for i in list:
    if i % 2 == 0:
        sum += i
print("Сумма четных чисел: ", sum)
for i in list:
    if i % 2 != 0:
        nech = list.index(i)
        list[nech] = 1
print('Замена нечетных на 1:', list)
list2 = []
list2.append('hello')
list2.append('world')
s = " ".join(list2)
print(s)
vowels = 0
consonants = 0
for i in s:
    if i in 'aeiouy':
        vowels += 1
    else:
        consonants += 1
print("Гласных:", vowels, "Согласных:", consonants)