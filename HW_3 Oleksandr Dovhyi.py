# 1. Define the id of next variables:

int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a), id(str_b), id(set_c), id(lst_d), id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.

lst_d.append(4)
lst_d.append(5)
print(id(lst_d))

#3. Define the type of each object from step 1.

print(type(int_a), type(str_b), type(set_c), type(lst_d), type(dict_e))

#4*. Check the type of the objects by using isinstance.

print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

# String formatting:
# Replace the placeholders with a value:
#"Anna has ___ apples and ___ peaches."


#5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(8, 4))

#6. By passing index numbers into the curly braces.
print("Anna has {0} apples and {1} peaches.".format(4, 8))

#7. By using keyword arguments into the curly braces.
print("Anna has {apples} apples and {peaches} peaches".format(apples = 8, peaches = 4))

#8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {0:5} apples and {1:3} peaches.".format(8, 4))
print('Anna has {0:5} apples and {1:3} peaches.'.format('five', 3))!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#9. With f-strings and variables
apples = 15
peaches = 2
print(f"Anna has {apples} apples and {peaches} peaches.")

#10. With % operator
print("Anna has %s apples and %s peaches." % (apples, peaches))

#11*. With variable substitutions by name (hint: by using dict)

dict_1 = {'a': apples, 'p': peaches}
print("Anna has %(a)s apples and %(p)s peaches." % dict_1)

# Comprehensions:
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
#
# #(2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]


#12. Convert (1) to list comprehension
list_compr_1 = [num **2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_compr_1)

#13. Convert (2) to regular for with if-else
list_1 = []
for num in range(10):
    if num % 2 == 0:
        list_1.append(num // 2)
    else:
        list_1.append(num * 10)
print(list_1)

#14. Convert (3) to dict comprehension.
# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
d_1 = {num: num ** 2 for num in range(1,11) if num % 2 == 1 }
print(d_1)

#15*. Convert (4) to dict comprehension.
# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)

d_2 = {num: num ** 2 if num %2 == 1 else num // 0.5 for num in range (1, 11) }
print(d_2)

#16. Convert (5) to regular for with if.
# (5)
#dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}

dict_comprehension_1 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension_1[x] = x**3
print(dict_comprehension_1)


#17*. Convert (6) to regular for with if-else.
# (6)
#dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}

dict_comprehension_2 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension_2[x] = x ** 3
    else:
        dict_comprehension_2[x] = x
print(dict_comprehension_2)

#18. Convert (7) to lambda function
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
foo = lambda x, y: x if x < y else y

#19*. Convert (8) to regular function
# (8)
# foo = lambda x, y, z: z if y < x and x > z else y

def foo_1(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
#20. Sort lst_to_sort from min to max
lst_to_sort.sort()
print(lst_to_sort)

#21. Sort lst_to_sort from max to min
lst_to_sort.sort(reverse=True)
print(lst_to_sort)

#22. Use map and lambda to update the lst_to_sort by multiply each element by 2
lst_to_sort_1 = list(map(lambda x: x * 2, lst_to_sort))
print(lst_to_sort_1)

# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
new_list = list(map(pow, list_A, list_B))
print(new_list)

#24. Use reduce and lambda to compute the numbers of a lst_to_sort.
#lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
from functools import reduce
lst_reduce = reduce(lambda a, b: a + b, lst_to_sort)
print(lst_reduce)

#25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
lst_filer = list(filter(lambda a: (a % 2 == 1), lst_to_sort))
print(lst_filer)

#26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b = range(-10, 10)
foo_filter = list(filter(lambda a: a < 0, b))
print(foo_filter)

#27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
list_3 = list(filter(lambda x: x in list_1, list_2))
print(list_3)
