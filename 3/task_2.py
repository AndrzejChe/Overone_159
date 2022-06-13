# Разделить строку “Apples, Oranges, Pears, Bananas, Berries” по запятым
# и вывести на экран.
# Затем объединить элементы с использованием пробела, чтобы программа вывела
# “Apples Oranges Pears Bananas Berries”.

s = "Apples, Oranges, Pears, Bananas, Berries"
print(s.split(','))
print("".join(['Apples', ' Oranges', ' Pears', ' Bananas', ' Berries']))