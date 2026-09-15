''' Objects
 (1) What is object
 (2) Iterable objects  & Range
 (3) Dictionary 
 (4) Error handling system
'''

import array  # package
import math
from math import ceil
print("===== What is Object =====")
# An object has state and method properties
# Everything is object in python
print(type("Hello World"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

print(math.ceil(97.7))
print(math.ceil(98.7))


print("===== Error Handling =====")
car_dict = dict(model="Toyota", year=2026, electro=True)

try:
    print("passed here")
    a = car_dict.speed
    print(f"result: {car_dict['origin']}")
except KeyError and AttributeError as err:
    print("Error occured: ", err)
else:
    print("If try works properly we overflow except and print else together with try")
finally:
    print("Finally always work no metter how was the result above")
