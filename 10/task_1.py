# Найти самое длинное слово в строке.
string = input()
text = string.split()
id_0 = 0
c = 0
for i in text:
    if len(text) < len(text[c]):
        id_0 = c
    c += 1
print(text[id_0])
