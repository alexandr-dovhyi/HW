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
        if 2 < self.water <= 15:
            self.water -= 2
            raise LowWater
        elif 0 < self.water <= 2:
            self.water = 0
            raise LowWater
        elif self.water <= 0:
            raise WithoutWater
        else:
            self.water -= 2
            return f'Washing...\n Water tank is {self.water}%'

    def perc_batt(self):
        if 0 < self.battery <= 20:
            self.battery -= 1
            raise LowBattery
        elif self.battery <= 0:
            raise WithoutCharge
        else:
            self.battery -= 1
            return f'Mooving...\n Battery is {self.battery}%.'

    def full_tank(self):
        if self.tank >= 90:
            self.tank += 1
            raise CleanTank
        elif self.tank == 100:
            raise FullTank
        else:
            self.tank += 1
            return f'Cleaning...\n Tank is {self.tank}%.'


def move():
    value_water = 50
    value_batt = 50
    value_tank = 50

    test_w = VacCleaner(value_water, value_batt, value_tank).wash
    test_b = VacCleaner(value_water, value_batt, value_tank).perc_batt
    test_t = VacCleaner(value_water, value_batt, value_tank).full_tank

    print(f'Level of water tank is {value_water}%.')
    print(f'Level of charge {value_batt}%.')
    print(f'Fullness of dust tank is {value_tank}%.')
    print('Start cleaning:')
    while True:
        try:
            if value_water >= 0:
                print(test_w())
            else:
                break
        except LowWater:
            print(f'Water is {value_water}%. Need add.')
        try:
            if value_batt > 0:
                print(test_b())
            else:
                break
        except LowBattery:
            print(f'WARNING: level of battery {value_batt}%. \n Need charging.')
        try:
            if value_tank < 100:
                print(test_t())
            else:
                break
        except CleanTank:
            print(f'WARNING: level of fullness tank is {value_tank}%. \n Need cleaning tank.')

        value_water -= 2
        value_batt -= 1
        value_tank += 2
        time.sleep(1.5)


move()
