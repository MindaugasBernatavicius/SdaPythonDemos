# Singleton
# class Person:
#     count_of_people = 0
#     def __init__(self, name):
#         Person.count_of_people += 1
#         self.name = name
#
#
# p1 = Person("Jonathan")
# print(Person.count_of_people)
# p2 = Person("Suzy")
# print(Person.count_of_people)
#
# p2.name = "Suzzana"
# print(p1.name)
#
# print(p1.count_of_people)
# print(p2.count_of_people)
# Person.count_of_people = 6
# print(p1.count_of_people)
# print(p2.count_of_people)
#
# print(p1.count_of_people is p2.count_of_people is Person.count_of_people)


class Singleton(object):
  _instances = {}
  def __new__(class_, *args, **kwargs):
    if class_ not in class_._instances:
        print(f"{class_}")
        class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
    return class_._instances[class_]

class Config(Singleton):
    pass


# # test the singleton
# x = Config()
# y = Config()
#
# print(x)
# print(y)
# print(x == y)
# print(x is y)
#
#
# class Person:
#     pass
#
# p1 = Person()
# p2 = Person()
# print(p1)
# print(p2)
# print(p1 == p2) # __eq__(self, other)
# print(p1 is p2)



class RealisticConfig(Singleton):
    # def __init__(self, file_name):
    #     with open(file_name, 'r') as f:
    #         self.__server = f.readline().split(" = ")[1]

    def set_config_file(self, file_name):
        with open(file_name, 'r') as f:
            self.__server = f.readline().split(" = ")[1]

    def get_headline(self):
        import requests
        print(self.__server)
        print(requests.get(f"https://{self.__server}").text[0:200])


rc = RealisticConfig()
rc.set_config_file('config.cfg')
rc.get_headline()

rc2 = RealisticConfig()
print(rc is rc2)



# Prototype is pretty simple
# Problem: how do I create copies of already created objects in the most efficient way
# Ref: https://refactoring.guru/design-patterns/prototype/python/example



# Dependency Injection
from abc import ABC

class Address(ABC):
    pass

class ShippingAddress(Address):
    def __init__(self, town, street, house_number):
        pass

class BillingAddress(Address):
    pass

class Person:
    # # 0. No dependency injection here
    # def __init__(self):
    #     self.age = 100
    #     self.name = 'Mike'
    #     self.address = ShippingAddress('Tallinn', 'Freedom', 15)

    # 1. (Constructor) dependency injection
    def __init__(self, age: int, name: str, address: Address):
        self.age = age
        self.name = name
        self.address = address

    # @property
    # def age(self):
    #     return self.age

    # @age.setter
    # def age(self, age):
    #     self.age = age

    # 2. (Setter) dependency injection
    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"{self.age} {self.name}"



# p = Person()
p = Person(22, "Jaone", ShippingAddress('Riga', 'Balsams', 15))
# Person(23, "Joana", BillingAddress())
print(p)

# In this example we connected:
# - OOP Composition
# - Design Pattern (Creational) - Dependency Injection
# - Design Principle from Solid - Dependency Inversion

# Dependency Injection, Dependency Inversion, Polymorphic composition enabled by Inheritence, Abstraction,