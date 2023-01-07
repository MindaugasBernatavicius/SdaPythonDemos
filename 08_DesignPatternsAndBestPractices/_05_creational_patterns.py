# Singleton

class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

class Config(Singleton):
    pass

# test the singleton
x = Config()
y = Config()

print(x)
print(y)
print(x == y)
print(x is y)


class Person:
    pass

p1 = Person()
p2 = Person()
print(p1)
print(p2)
print(p1 == p2)
print(p1 is p2)


# Dependency Injection
from abc import ABC

class Address(ABC):
    pass

class ShippingAddress(Address):
    pass

class BillingAddress(Address):
    pass

class Person:
    # # 0. No dependency injection here
    # def __init__(self):
    #     self.age = 100
    #     self.name = 'Mike'
    #     self.address = ShippingAddress()

    # 1. (Constructor) dependency injection
    def __init__(self, age: int, name: str, address: Address):
        self.age = age
        self.name = name
        self.address = address

    # 2. (Setter) dependency injection
    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name


# p = Person()
p = Person(22, "Jaone", ShippingAddress())
# Person(23, "Joana", BillingAddress())

# In this example we connected:
# - OOP Composition
# - Design Pattern (Creational) - Dependency Injection
# - Design Principle from Solid - Dependency Inversion
