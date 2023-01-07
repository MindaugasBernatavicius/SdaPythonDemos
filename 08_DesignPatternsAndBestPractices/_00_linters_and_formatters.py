# def sum(lst):
#     pass
#
# class Adder:
#     def sum(self, lst):
#         pass
from dataclasses import dataclass

people_lst = [{"name": "", "age": 5},
              {"name": "", "age": 5},
              {"name": "", "age": 5},
              {"name": "", "age": 5},
              {"name": "", "age": 5}]

# for i in people_lst:
#     print(i)


# res = sum([1, 2, 3])
# print(res)
#
# res = sum([1, 2, 3])
# print(res)

# type hints
class Calculator:
    def add(self, i: int, j: int) -> int:
        """
        Function dedicated to adding numbers

        :param i: first number
        :param j: first number
        :return: resulting number after summation
        """
        return i + j

    def subtract(self, i: int, j: int) -> int:
        return i - j

    def division(self, i: int, j: int) -> float:
        return i / j


# print(Calculator().add("A", "B"))


# help(print)
# help(Calculator.add)


from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int


def is_person_permitted(person):
    return True if 18 < person.age < 65 else False


is_permitted = is_person_permitted(Person("Jonas", 17))

if is_permitted: # == True:
    print("Welcome to the job")
else:
    print("See you in a few years!")


domain = "https://delfi.ee"
print(domain[0:10] == "https://de")
print(domain.startswith("https://de"))

# # we use .startswith() and .endswith() instead of "slicing"
# name = input("Please introduce yourself: ")
#
# if name[0] == "M":
#     print("Hello")
#
# if name.startswith("M"):
#     print("Hello")






def add(i, j):
    """ Adds two numbers """
    pass


def subtract():
    pass
