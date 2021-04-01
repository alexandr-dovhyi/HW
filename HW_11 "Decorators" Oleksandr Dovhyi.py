from functools import wraps


# 1. double_result
# This decorator function should return the result of another function multiplied by two
def double_result(func):
    # return function result multiplied by two
    def inner(a, b):
        return func(a, b) * 2

    return inner


def add(a, b):
    return a + b


print(add(5, 5))  # 10


@double_result
def add(a, b):
    return a + b


print(add(5, 5))  # 20


# 2. only_odd_parameters
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise return the string "Please use only odd numbers!"

def only_odd_parameters(func):
    # if args passed to func are not odd - return "Please use only odd numbers!"
    def inner(*args):
        for el in args:
            if el % 2 == 0:
                return "Please use only odd numbers!"
            else:
                return func(*args)

    return inner


@only_odd_parameters
def add(a, b):
    return a + b


print(add(5, 5))  # 10


# print(add(4, 4))  # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


print(multiply(2, 3, 4, 5, 6))
print(multiply(3, 5, 7, 9, 1))


# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):


def logged(func):
    # log function arguments and its return value
    @wraps(func)
    def inner(*args, **kwargs):
        a_args = [repr(x) for x in args]
        k_kwargs = [f'{keys}={values}' for keys, values in kwargs.items()]
        signature = ', '.join(a_args + k_kwargs)
        print(f'Calling: {func.__name__}({signature})')
        print(f'The args is: {args}')
        print(f'The kwargs is: {kwargs}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} result: {result}')
        return result

    return inner


@logged
def func(*args, **kwargs):
    return 3 + len(args) + len(kwargs)


func(4, 4, 4)
func(four=4, five=5, six=6)
func([6, 9, 4], 5, 5, four=4, five=5)


# you called func(4, 4, 4)
# it returned 6

# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.

def type_check(correct_type):
    # put code here
    def check_decorator(func):
        @wraps(func)
        def inner(x):
            if isinstance(x, correct_type):
                return func(x)
            return f'Wrong Type: {type(x).__name__}, should be {correct_type.__name__}'

        return inner

    return check_decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(
    ['Not', 'A', 'String']))  # "Wrong Type: list" should be printed, since non-str passed to decorated function
