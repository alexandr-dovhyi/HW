#1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
# v = Vehicle(100, 12500 )
# print(v.mileage)
# print(v.max_speed)
#2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have seating_capacity own method
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity
# b= Bus(100, 150000, 40)
# print(b.max_speed)
# print(b.mileage)
# print(b.seating_capacity)
#3. Determine which class a given Bus object belongs to (Check type of an object)

a = Bus(40, 80, 120)
print(type(a))
print(isinstance(a, Bus))

# 4. Determine if School_bus is also an instance of the Vehicle class
# не розумію звідки взялось School_bus, буде помилка, - перевіряю належність об"єкта "а" до класу Vehicle,
# згідно (моєї)логіки постановки завдання
print(isinstance(a, Vehicle))

#5. Create a new class School with get_school_id and number_of_students instance attributes

class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students
school = School(135, 800)
# print(school.get_school_id)
# print(school.number_of_students)
#6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own - bus_school_color
class SchoolBus(School, Bus):
    def __int__(self,get_school_id, max_speed, mileage, seating_capacity, number_of_students, bus_school_color):
        #super().__int__(get_school_id, number_of_students, max_speed, mileage, seating_capacity)
        School.__init__(get_school_id, number_of_students)
        Bus.__init__(max_speed, mileage, seating_capacity)
        self.bus_school_color = bus_school_color
s_b = SchoolBus(186, 300)
print(s_b.get_school_id)
print(s_b.number_of_students)
print(s_b.bus_school_color('Yellow'))!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#7. Polymorphism:  Create two instances, one of Bear and one of Wolf,
#make a tuple of it and by using for call their action using the same method.
#Create two classes: Bear, Wolf. Both of them should have make_sound method.
class Bear:
    def __init__(self, sound):
        self.sound = sound
    def make_sound(self):
        print(f"I'm a Bear, and I say {self.sound}")

class Wolf:
    def __init__(self, sound):
        self.sound = sound
    def make_sound(self):
        print(f"I'm a Wolf, and I say {self.sound}")
be = Bear("BUUUUUU")
wo = Wolf("AUUUUUUUU")

animals = (be, wo)

for animal in animals:
    animal.make_sound()
#Magic methods:
#8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
#otherwise return message: "Your city is too small".
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
    def __new__(cls, name, population):
        instance = super(City, cls).__new__(cls)
        if population > 1500:
            return instance
        else:
            print("Your city is too small")
# city = City('Kyiv', 1600)
# city_1 = City('Kyiv', 100)
# print(city)
# print(city_1)
#9. Override a printable string representation of the City class and return: The population of the city {name} is {population}
    def __str__(self):
        return f'The population of the city {self.name} is {self.population}'
descr = City('Kyiv', 3000)
print(descr)

#10*. Override magic method __add__() to perform the additional action as 'multiply'
# (*) the value which is greater than 10. And perform this add (+) of two instances.
class Count:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        if self.count and other.count < 10:
            total_count = self.count + other.count
        else:
            total_count = self.count * other.count
        return Count(total_count)

    def __str__(self):
        return f'Count: {self.count}'

count_1 = Count(7)
count_2 = Count(11)
count_3 = count_1 + count_2
print(count_3)
#11. The __call__ method enables Python programmers to write classes where the instances behave like functions
# and can be called like a function.
#Create a new class with __call__ method and define this call to return sum.

class Call:
    def __call__(self, a, b, c, d):
        sum_1 = a + b + c + d
        return sum_1

call_1 = Call()
print(call_1(2, 6, 8, 10))
#12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the
# length of the cart list is non-zero.
# e.g.:
# order_1 = MyOrder(['a', 'b', 'c'], 'd')
# order_2 = MyOrder([], 'a')
# bool(order_1)
# True
# bool(order_2)
# False
class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer
    def __bool__(self):
        if len(self.cart) > 0:
            return True
        else:
            return False
order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
print(bool (order_2))





























