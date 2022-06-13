# Преобразовать текст в список слов с удалением знаков препинания
import string

str = input()
pri = ['.', ',', '!', '?', ':', ';', '(', ')']
a = str.split(' ')
print(a.remove(pri))

# for j in text:
#     if j[-1] in pri:
#         text[i] = j[:-1]
#         j = text[i]
#     if j[0] in pri:
#         text[i] = j[1:]
#     i += 1
# for i in str:
#     a
