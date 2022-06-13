# Написать программу для вычисления значения выражений.
# # Проверить правильность выполнения задания с помощью тестовых значений.
import math

a = int(input("a: "))
b = int(input("b: "))
y = int(input("y: "))
x1 = a + b - y
x2 = b + y - a
x3 = y + a - b
x4 = a + b + y
Y = (1 / 4) * (math.sin(x1) + math.sin(x2) + math.sin(x2) - math.sin(x4))
print(Y)