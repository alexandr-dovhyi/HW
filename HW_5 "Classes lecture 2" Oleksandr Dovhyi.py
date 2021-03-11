# 1.
class Laptop:
    """
    Make the class with composition.
    """

    def __init__(self, percent_of_charge, speed_of_charging):
        self.speed_1 = Battery(speed_of_charging)
        self.percent_of_charge = percent_of_charge
        print(f'The % of charge is {percent_of_charge}')


class Battery:
    """
    Make the class with composition.
    """

    def __init__(self, speed_of_charging):
        self.speed_of_charging = speed_of_charging
        print(f'The speed of charging is {speed_of_charging}')


laptop = Laptop(15, 100)
print(laptop.percent_of_charge)



# 2.
class Guitar:
    """
    Make the class with aggregation
    """

    def __init__(self, mount_of_strings):
        self.mount_of_strings = mount_of_strings
        print(f'Mount of strings are {mount_of_strings}')

class GuitarString:
    """
    Make the class with aggregation
    """
    def __init__(self, active_string):
        self.active_string = active_string
        print(f'Active strings are {active_string}')


a_str = GuitarString(2)
guitar = Guitar(6)
guitar_1 = Guitar(a_str)


# 3
class Calc:
    """
    Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note: this method should not take instance as first parameter.
    """
    @staticmethod
    def add_nums(first, second, third):
        return first + second + third


print(Calc.add_nums(25, 11, 69))


# 4*.
class Pasta:
    """
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return Pasta(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return Pasta(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(["tomato", "cucumber"])
pasta_2 = Pasta.bolognaise()

print(pasta_1.ingredients)
print(pasta_2.ingredients)


# 5*.
class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self.visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, x):
        if x < self.max_visitors_num:
            self._visitors_count = x
        else:
            self._visitors_count = self.max_visitors_num


Concert.max_visitors_num = 50
concert = Concert(50)
concert.visitors_count = 1000
print(concert.visitors_count)  # 50

# 6.
import dataclasses


@dataclasses.dataclass
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
    """
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


book_data = AddressBookDataClass(25, 'Alex', '0464556', 'First street', 'example@i.ua', '01.01.01', 6)
print(book_data)
print(book_data.age)
# 7. Create the same class (6) but using NamedTuple
import collections

Book_data_1 = collections.namedtuple('AddressBookData',
                                     ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])
data_1 = Book_data_1(80, 'Alex', '0464556', 'First street', 'example@i.ua', '01.01.01', 6)
print(data_1)
print(data_1[5])
print(data_1.age)

# 8.
class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    """
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBook(key = {self.key}, name = {self.name}, phone_number = {self.phone_number}, ' \
               f'address = {self.address}, email = {self.email}, birthday = {self.birthday}, age = {self.age})'


address_book = AddressBook(16, 'Alex', '065564', 'Second street', '1@i.ua', '25.25.25', 18)
print(address_book)

# 9.


class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"


john = Person()
john.age = 18
print(john.age)

# 10.


class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(000, 'Alex')
setattr(student, 'email', '12321@i.ua')
student_email = student.email
#print(student.name)
print(getattr(student, 'email'))



# 11*.
class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def convert(self):
        return self._temperature * 1.8 + 32


# create an object
obj = Celsius(25)

print(obj.convert)