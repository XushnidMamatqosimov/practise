''' FUNCTIONS
 (1) DEFINE and CALL
 (2) Parametr and Argument
 (3) Keyword & default arguments 
 (4) Scope
'''

print("===== Define(parameter) and Call(argument) =====")
# build in function > print() type()
# Function - reusable block of code!
# Instead of block {} in Java, Python uses indentation!

# Define - build
def greet(a):
    print(f"How do you do, {a}")  
    
def greeting(b): 
    print("greeting is executed")
    return f"Hi {b}"
    
# Call     
result1 = greet("Martin")
print("result1: ", result1);

result2 = greeting("Justin")
print("result2: ", result2)


print("===== Keyword & default arguments =====")
def give_greet(name, age = 22): #default argument (age = 22)
    print("give_greet is executed")
    return f"Hi {name} you are {age} years old!"

res = give_greet(name = "Justin", age = 28)  #keyword argument (name = "Justin", age =28)
print("res: ", res)

res = give_greet(name = "Martin")  #keyword argument
print("res: ", res)


print("===== Scopes =====")
b = 100 # 3

def calculate(a , b): #2
    c = a * b # 1
    print(f"c value: {c}")
    
    
calculate(5,2)

