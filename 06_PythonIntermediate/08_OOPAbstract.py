# 0. Simple object
# class Person:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#
#     def is_legal_age(self):
#         return True if self.age > 18 else False
#
#
# p1 = Person(20, "Jonas")
# p2 = Person(30, "Petras")
#
# print(p1.age)
#
# # ... alternative representations
# p1_age = 20
# p1_name = 'Jonas'
#
# p2_age = 30
# p2_name = 'Petras'
#
# p1_dict = { 'age': 20, 'name': 'Jonas' }
# p2_dict = { 'age': 30, 'name': 'Petras' }
#
# # ...
#
# print(p1.is_legal_age())
#
# employees = [p1, p2]


# 1. Inheritence - keep your classes DRY!
# class SalesPerson:
#     def __init__(self, badge_id, age, name, salary):
#         self.badge_id = badge_id
#         self.age = age
#         self.name = name
#         self.salary = salary
#
# class Janitor:
#     def __init__(self, badge_id, age, name, salary):
#         self.badge_id = badge_id
#         self.age = age
#         self.name = name
#         self.salary = salary
#
# class SoftwareEngineer:
#     def __init__(self, badge_id, age, name, salary):
#         self.badge_id = badge_id
#         self.age = age
#         self.name = name
#         self.salary = salary

# class Employee:
#     def __init__(self, badge_id, age, name, salary):
#         self.badge_id = badge_id
#         self.age = age
#         self.name = name
#         self.salary = salary
#
# class SalesPerson(Employee):
#     def __init__(self, badge_id, age, name, salary, sales_commission_rate):
#         super(SalesPerson, self).__init__(badge_id, age, name, salary)
#         self.sales_commission_rate = sales_commission_rate
#
# # class SalesPerson(Employee):
# #     def __init__(self, employee, sales_commission_rate):
# #         super(SalesPerson, self).__init__(employee.badge_id, employee.age, employee.name, employee.salary)
# #         self.sales_commission_rate = sales_commission_rate
#
# class Janitor(Employee):
#     def __init__(self, badge_id, age, name, salary):
#         super(Janitor, self).__init__(badge_id, age, name, salary)
#
# class SoftwareEngineer:
#     def __init__(self, badge_id, age, name, salary):
#         super(SoftwareEngineer, self).__init__(badge_id, age, name, salary)
#
#
# e1 = SalesPerson(12233, 23, "Marytė", 500, 10)
# # e = Employee(12233, 23, "Marytė", 500)
# # e1 = SalesPerson(e, 10)
# print(e1.name)
# print(e1) # <__main__.SalesPerson object at 0x000001D28035E7C0>
#
# # ... inheriting methods / logic
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#
#
# class Employee(Person):
#     def __init__(self, name, age, rate, num_of_hours):
#         # print('Employee%s' % super().__init__)
#         super().__init__(name, age)
#         self.rate = rate
#         self.num_of_hours = num_of_hours
#
#     def show_finance(self):
#         return self.rate * self.num_of_hours
#
#
# class Student(Person):
#     def __init__(self, name, age, scholarship):
#         super().__init__(name, age)
#         self.scholarship = scholarship
#
#     def show_finance(self):
#         return self.scholarship


# print(Person("Jonas", 60))
# print(Employee("Petras", 50, 15, 42))
# print(Student("Jurgis", 20, 150))
#
#
# class MechanicalApparatus:
#     def __init__(self, length, material):
#         self.length = length
#         self.material = material
#
# class Engine(MechanicalApparatus):
#     def __init__(self, length, material, power):
#         super().__init__(length, material)
#         self.power = power
#
# class RocketEngine(Engine):
#     def __init__(self, length, material, power, operating_temperature):
#         super().__init__(length, material, power)
#         self.operating_temperature = operating_temperature


# 2. Multiple inheritance
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#
# class Employee(Person):
#     def __init__(self, name, age, rate, num_of_hours):
#         Person.__init__(self, name, age)
#         self.rate = rate
#         self.num_of_hours = num_of_hours
#
#     def show_finance(self):
#         return self.rate * self.num_of_hours
#
#
# class Student(Person):
#     def __init__(self, name, age, scholarship):
#         Person.__init__(self, name, age)
#         self.scholarship = scholarship
#
#     def show_finance(self):
#         return self.scholarship
#
#
# class WorkingStudent(Employee, Student):
#     def __init__(self, name, age, rate, num_of_hour, scholarship):
#         Employee.__init__(self, name, age, rate, num_of_hour)
#         Student.__init__(self, name, age, scholarship)
#
#     def show_finance(self):
#         return self.rate * self.num_of_hour + self.scholarship
#
#
#
#
# print(WorkingStudent.__mro__)
# os4 = WorkingStudent("Monica", 24, 9.5, 70, 500)
# # # print(os1)
# # # print(os2)
# # # print(os3)
# print(os4)
#
#
# # 3. Polymorphism
# os1 = Person("John", 54)
# os2 = Employee("Jack", 36, 20, 160)
# os3 = Student("Agatha", 22, 1000)
#
# # ... this method, in order to work,
# # ... must receive an obj that has a method
# # ... .show_finance() implemented. Otherwise - error!
# def check_finance(obj: Employee):
#     print(obj.show_finance())
#
# # check_finance("[]") # AttributeError: 'str' object has no attribute 'show_finance'
# # check_finance(os2)  # an instance of the Employee class
# check_finance(os3)  # an instance of the Student class -> Expected type 'Employee', got 'Student' instead
#
# os4 = WorkingStudent("Monica", 24, 9.5, 70, 500)
# check_finance(os4)


# 4. Abstract class
from abc import ABC, abstractmethod
from math import pi

class Figure(ABC):
    @abstractmethod
    def circuit(self):
        pass

    @abstractmethod
    def area(self):
        pass

# ... try to create an object
# f = Figure() # TypeError: Can't instantiate abstract class Figure with abstract methods area, circuit

# class Rectangle(Figure):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return f"Rectangle {self.a} x {self.b}"
#
# r = Rectangle(10, 20)
# print(r)

# TypeError: Can't instantiate abstract class Rectangle with abstract methods area, circuit
# ... if an child class does not implement (override) abstract methods the class itself will be
# ... treated as abstract class.

# class Rectangle(Figure):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def circuit(self):
#         return 2 * (self.a + self.b)
#
#     def area(self):
#         return self.a * self.b
#
#     def __str__(self):
#         return f"Figure {self.a} x {self.b}"
#
#
# class Circle(Figure):
#     def __init__(self, r):
#         self.r = r
#
#     def circuit(self):
#         return 2 * self.r * pi
#
#     def area(self):
#         return pi * self.r ** 2
#
#
# r = Rectangle(10, 20)
# print(r)
#
# def do_something_with_geometric_figures(fig: Figure):
#     return fig.area()


# 5. Dataclass decorator
# class Rectangle(Figure):
#     def __init__(self, a: int, b: int):
#         self.a = a
#         self.b = b
#
#     def __repr__(self) -> str:
#         return f"Rectangle(a={self.a}, b={self.b})"
#
#     def __eq__(self, other) -> bool:
#         return isinstance(other, Rectangle) and (self.a, self.b) == (other.a, other.b)
#
#     def circuit(self) -> float:
#         return 2 * (self.a + self.b)
#
#     def area(self) -> float:
#         return self.a * self.b
#
# # ... __repr__
# print(Rectangle(10, 20))
# print(Rectangle(800, 500))


from dataclasses import dataclass

@dataclass
class Rectangle(Figure):
    a: int
    b: int

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

print(Rectangle(10, 20))
print(Rectangle(800, 500))