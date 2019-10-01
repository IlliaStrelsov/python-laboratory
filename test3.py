import math
print("Лабораторна робота №1 Стрельцов Ілля КМ-93,завдання №3")
print("Введіть значення x")
x = float(input())

if x > 0:
    print(math.log1p(x) + 9)
else:
    print(-x / (x**2 - 7))