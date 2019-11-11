import re
print("Лабораторна робота№3, Стрельцов Ілля, КМ-93,завдання№1")
print("Введіть текст")
text = input()
print (re.sub(r'\s+', ' ', text))
print (re.sub(r"\d","",text))
text = re.sub(r'\s+', ' ', text)
text = re.sub(r"\d","",text)
print(text)
