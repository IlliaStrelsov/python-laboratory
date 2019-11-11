print("Лабораторна робота№4, Стрельцов Ілля, КМ-93,завдання№1")
def binary_code(n,b):
    while n>0:
        b = str(n % 2) + b
        n = n//2
    return b
def octal_system(n,b):
    while n>0:
        b = str(n % 8) + b
        n = n//8
    return b
i = 1
while(i > 0):
    print("Введіть число в десятковій системі числення ")
    n = int(input())
    b = ""
    print(binary_code(n,b))
    print(octal_system(n,b))

    print("Щоб повторити програму введіть 1 , щоб завершити введіть 0")
    i = int(input())