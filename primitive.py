print("=================")

# in Java, variable is a name of storage location!
# in Python, variable is a named reference => storage location;

count = 100
print("count: ", count, type)
print(f"the count: {count} and type: {type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print (result1, result2)
