#Задача 1 - легкая:
#Сформировать и заполнить массив случайным числами и вывести максимальное, минимальное и среднее значение.
#Для генерации случайного числа использовать метод Math.random(), который возвращает значение в промежутке [0, 1].

import random

n = int(input("Введите длину списка: "))
spisok = []

for i in range(n):
    random_num = random.random()
    spisok.append(random_num)

max_num = max(spisok)
min_num = min(spisok)
mid_num = sum(spisok) / n

print("Список:", spisok)
print("Максимальное значение:", max_num)
print("Минимальное значение:", min_num)
print("Среднее значение:", mid_num)
