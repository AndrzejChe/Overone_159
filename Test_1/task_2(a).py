# Написать программу для вычисления значения выражений.
# Проверить правильность выполнения задания с помощью тестовых значений.

a = int(input("Тестовое значение: "))

y = (((1 + a + a ** 2) / 2 * a + a **2) + 2 - ((1 - a + a ** 2) / 2 * a - a)) ** -1 * (5 - 2 + a ** 2)
print(y)