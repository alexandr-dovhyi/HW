import logging
import time

"""
Task 1
Напишіть калькулятор в якого будуть реалізовані операції додавання, віднімання, множення, ділення, піднесення в
степінь,
взяття з під кореня, пошук відсотку від числа
Огорніть в конструкцію try... except... потенційно "небезпечні" місця, наприклад отримання числа і приведення до типу
даних
або інструкції математичних операцій
заповніть ваш скрипт логами
Логи здебільшого інформаційні (викликали таку функцію з такими аргументами)
+ логи з помилками
причому логи повинні записуватись у файл, тому що в консолі ви будете взаємодіяти з калькулятором,
лог файл завжди відкриваєтсья в режимі дозапису.
так як ви працюєте з файлом не забудьте про те що це потенційне місце поломки
"""
log_template = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, filename='log9.log', filemode='a', format=log_template)


logging.info('START!')
print('Hello in my Calculator!')
print('If You need percent of a number, first number must be % value, second number - number!')
while True:
    str_x = input("Enter first number: ")
    try:
        x = int(str_x)
    except ValueError:
        print("x is not a number")
        continue
    logging.info(f'Entered first number {x}')
    str_y = input("Enter second number: ")
    try:
        y = int(str_y)
    except ValueError:
        print("y is not a number")
        continue
    logging.info(f'Entered second number {y}')
    method = ["+", "-", "*", "/", "sqrt", "%", "**"]
    action = input('Enter action with numbers(+, -, *, /, sqrt, %, **): ')
    while action not in method:
        print(f'There is no such method {action}')
        action = input('Enter action with numbers(+, -, *, /, sqrt, %, **): ')
    logging.info('Checked action')

    def calc():
        if action == "+":
            return x + y
        elif action == "-":
            return x - y
        elif action == "**":
            return x ** y
        elif action == "*":
            return x * y
        elif action == "/":
            try:
                x / y
            except ZeroDivisionError:
                logging.error('ZeroDivisionError', exc_info=True)
                return 0
        elif action == "sqrt":
            return pow(x, .5)
        else:
            return x * y / 100
    logging.info(f'Choosed action {action}')
    c = calc()
    logging.info('Called function calc')
    print(f'Result is: {c}')
    logging.info(f'Printed result: {c}')
    logging.info('END!')
    break
"""
Task 2
Напишіть клас робота пилососа
в ініт приймається заряд батареї, заповненість сміттєбака і кількість води

реалізуйте функцію move() - нескінченний цикл який на кожній ітерації "замерзає" на 1 сек
окрім цього на кожній ітерації викликаються функції "wash" і "vacuum cleaner"
(в цих функціях повинні стояти прніти "wash" і "vacuum cleaner" відповідно),
також на кожній ітерації прінтиться "move"
+ на кожній ітерації цикла заряд батареї і кількість води зменшується на певну кількість
(задайте в статік аргументах класу як конфіг пилососа, або в окремому конфіг файлі),
а кількість сміття збільшується

Напишіть власні ексепшини які кидаються коли заряд батареї менше ніж 20%, заряд батареї 0%, кількість води - 0,
кількість сміття більша ніж певне число
опрацюйте ваші ексепшини (наприклад якщо заряд батареї менше 20% то цикл робить ще певну кількість ітерацій і
зупиняється,
якщо вода закінчилась то пилосос тепер не миє підлогу а тільки пилососить,
0 відсотків заряду - пилосос кричить щоб його занесли на зарядку бо сам доїхати не може)

можете придумати ще свої ексепшини і як їх опрацьовувати
"""


class LowWater(Exception):
    pass


class LowBattery(Exception):
    pass


class FullTank(Exception):
    pass


class WithoutWater(Exception):
    pass


class WithoutCharge(Exception):
    pass


class CleanTank(Exception):
    pass


class VacCleaner:
    def __init__(self, water, battery, tank):
        self.water = water
        self.battery = battery
        self.tank = tank

    def wash(self):
        if self.water == 0:
            raise WithoutWater
        else:
            self.water -= 1
            print(f'Washing...\n Water tank is {self.water}%')
            if 2 <= self.water <= 15:
                raise LowWater

    def perc_batt(self):
        if self.battery <= 0:
            raise WithoutCharge
        else:
            self.battery -= 1
            print(f'Moving...\n Battery is {self.battery}%.')
            if 1 <= self.battery <= 20:
                raise LowBattery

    def full_tank(self):
        if self.tank >= 100:
            raise FullTank
        else:
            self.tank += 1
            print(f'Cleaning...\n Tank is {self.tank}%.')
            if 99 >= self.tank >= 90:
                raise CleanTank


def move():
    vac_cleaner = VacCleaner(5, 50, 50)

    print(f'Level of water tank is {vac_cleaner.water}%.')
    print(f'Level of charge {vac_cleaner.battery}%.')
    print(f'Fullness of dust tank is {vac_cleaner.tank}%.')
    print('Start cleaning:')
    while True:
        try:
            vac_cleaner.perc_batt()
        except LowBattery:
            print(f'WARNING: level of battery {vac_cleaner.battery}%. \n Need charging.')
        except WithoutCharge:
            print(f'level of battery {vac_cleaner.battery}%. \n STOP!!!.')
            break

        try:
            vac_cleaner.wash()
        except LowWater:
            print(f'Water is {vac_cleaner.water}%. Need add.')
        except WithoutWater:
            print(f'Level of water {vac_cleaner.water}%, only cleaning ')

        try:
            vac_cleaner.full_tank()
        except CleanTank:
            print(f'WARNING: level of fullness tank is {vac_cleaner.tank}%. \n Need cleaning tank.')
        except FullTank:
            print(f'Dust tank is {vac_cleaner.tank}%, only washing!')
        time.sleep(1)


move()
