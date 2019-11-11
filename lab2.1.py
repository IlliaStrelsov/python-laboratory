print("Лабораторна робота №2 Стрельцов Ілля КМ-93,завдання №1")
print("Введіть значення n")
n = int(input())
print("Введіть значення x")
x = int(input())

while x == 1:
    print("x != 1")
    x = int(input())

result = 0
for i in range(n):
    result += ((x + 2) ** (i + 1)) / (x - 1)
print(result)
