import random
# ввод
n = int(input("Введите размер списка:\n"))
A = []  # создание пустого списка
for i in range(n):
    a = random.random()     # генерация случайного числа
    A.append(a)             # добавление числа в список
# вывод
for i in range(n):
    print(A[i])
