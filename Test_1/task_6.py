# В строке “Иван Иванов” поменяйте местами слова.
# Может быть предоставлена любая строка с именем и фамилией.
# например
# “Петр Иванов” => “Иванов Петр”

s = ' '.join(input().split(' ')[::-1])
print(s)

