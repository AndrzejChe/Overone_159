# На вход программе подается натуральное число n. Напишите программу, которая выводит числа
# от 1 до n включительно за исключением:
# чисел от 6 до 11 включительно; чисел от 15 до 25 включительно; чисел от 32 до 39 включительно.

n = int(input("Введите число: "))
el = []
for i in range(1,n):
    el.append (i)
del el[5:11]
del el[14:25]
print(el)

