import pickle
import openpyxl
"""
Task 1
У файлі task1.txt знаходиться текст субтитрів взятий з відео на ютубі. Текст складається з  міток часу і репліки яка
була сказана в той момент часу.
Причому репліка знаходиться в наступному рядку після мітки часу.
Результатом виконнання завдання повинно бути:
1. словник елементами якого буде пара ключ:значення де ключ - мітка часу, значення - репліка в даний момент часу
"""

with open("task1.txt", "r") as file:
    r = file.readlines()
    r = [line.strip() for line in r]
    #print(r)
    dict_1 = {r[i]: r[i + 1] for i in range(0, len(r),2)}
    #print(dict_1)
"""
2. файл в якому знаходиться текст з якого видалені всі мітки часу. всі субтитри повинні мати вигляд простого тексту.
Це означає що окрім видалення міток часу, вам потрібно видалити переноси рядків"""
del r[0: len(r):2]
#print(r)

with open('task1_1.txt', 'w') as file_1:
    for v in r:
        file_1.write(f'{v}')
"""
Task 2
в файлі task2 збережений список, відкрийте цей файл, прочитайте вміст, і знайдіть середнє арифметичне чисел що 
знаходяться в списку
"""

with open('task2', 'rb') as task_2:
    read = task_2.read()
    lst = pickle.loads(read)
    sum_1 = sum(lst) / len(lst)
    #print(sum_1)

"""
Task 3
Використовуючи openpyxl (або будь-яку іншу зручну для вас бібліотеку), напишіть контекстний менеджер для роботи з ексель.
Даний менеджер повинен бути аналогом методу open()
"""


class NewXLS:
    def __init__(self, file_name):
        self.file_obj = openpyxl.load_workbook(file_name)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


with NewXLS("task_3_1.xlsx") as file:
    sheet = file.active
    sheet['A1'] = 46
    sheet['A2'] = 56

print(sheet['A1'].value)
print(sheet['A2'].value)

