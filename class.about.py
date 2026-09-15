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
