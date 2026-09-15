''' Class
(1) What is class
(2) ordinary and static properties
(3) special methods
'''

print("===== What is class =====")
# Class => bu Object yasovchi shablon
# Class structure => state, constructor, method


class Person():
    # state:
    message = "static state property"

    # constructor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} how are you?")

    def say_age(self):
        print(f"I am {self.age} years old")

    @classmethod
    def explain(cls):
        print("This is static method from Person class")


person1 = Person("Xushnid", 21)
person2 = Person("Declan", 22)

person1.introduce()
person2.say_age()

print("======static State=====")
# bu static stateni chaqirish
print(Person.message)
# static method
Person.explain()


print("===== Python Magic methos =====")
#  __init__, __new__, __eq__, __str__, __call__, __getitem__, __len__


class Car():
    defination = "This is car class's static state"

    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        print("bu __init__ dunder")
        self.name = name
        self.year = year

    def start_engine(self):
        print(f"{self.name} engine is activated")

    def stop_engine(self):
        print(f"{self.name} engine is stopped")

    def __str__(self):
        return f"the car name {self.name} and its year {self.year}"
    
    def __call__(self, *args, **kwds):
        print("Object called as function")


car_obj = Car("Ferrari", 2025)
car_obj.start_engine()
car_obj.stop_engine()
print("------")
carByd = Car("Byd", 2021)
print(carByd)
carByd()
