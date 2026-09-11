print("======== Number =========")

# in Java, variable is a name of storage location!
# in Python, variable is a named reference => storage location;

count = 100
print("count: ", count, type)
print(f"the count: {count} and type: {type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)

print("======== String =========")
# Methods: upper(), lower(), title(), find(), replace();

course = "AI Python FullStack"
res = type(course)
print(f"the result: {res}")

res = course.title()
print(f"the result: {res}")

res = course.upper()
print(f"the result: {res}")

res = course.replace("FullStack", "MasterClass")
print(f"the result: {res}")

print("======== Boolean =========")
# functions: => type(), input(), bool(), int(), str()
y = input("Give your value for Y: ")
print("value of Y: ", y)

res1 = y.isnumeric()
print(f"the input value is numeric: {res1}")

# TRUSY vs FALSY value
# TRUSY: True, 100, -100, "MIT"
# FALSY: False, 0, "", None

test_falsy = "" or False or None or 100
print("The test_falsy: ", bool(test_falsy))

test_trusy= " MIR " 
print("The test_trusy: ", bool(test_trusy))
 