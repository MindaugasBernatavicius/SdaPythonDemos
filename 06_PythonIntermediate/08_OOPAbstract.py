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


# 6. Class and static methods
# rect1 = Rectangle(10, 20)
# print(rect1.circuit()) # instance method / object method
#
#
# @dataclass
# class X:
#     example_class_var = "ABC"
#     object_counter = 0
#     def __init__(self, y):
#         self.y = y
#         X.object_counter += 1
#
#     @classmethod
#     def example_class_method(cls):
#         # return self.y # self is not passed to class methods, they are not able to operate on instance properties
#         return cls.example_class_var
#
#     @classmethod
#     def how_many_object_created(cls):
#         return cls.object_counter
#
#
# print(X.example_class_var) # here, we do not create a new object. We call the class, not an object (common way to call it)
# print(X(10).example_class_var) # this is where we create an object
# # print(X(10).example_class_var)
# print(X.how_many_object_created())


## ... more realistic example
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#
#
# class Student(Person):
#     def __init__(self, name, age, scholarship):
#         if self.is_name_correct(name):
#             Person.__init__(self, name, age)
#             self.scholarship = scholarship
#
#     def show_finance(self):
#         return self.scholarship
#
#     @classmethod
#     def create_from_string(cls, sentence):
#         """
#         Alternative constructor - first it prepares the variables from a string
#         ... then it calls the __init__() method of the student class
#         """
#         name, age, scholarship = sentence.split()
#         age, scholarship = int(age), float(scholarship)
#         if cls.is_name_correct(name):
#             return cls(name, age, scholarship)
#
#     @staticmethod
#     def is_name_correct(name):
#         if name[0].isupper() and len(name) > 3:
#             return True
#         return False
#
# # def is_name_correct(name):
# #     if name[0].isupper() and len(name) > 3:
# #         return True
# #     return False
#
# print(Student.is_name_correct("Mindaugas"))
# print(Student("M", 15, 15).is_name_correct("Mffdfd"))

# 7. Deep copy
# ... assignment does not create an independent copy
# lst1 = [1, 2]
# lst2 = lst1
# print(f"Before assignment")
# print(lst1)
# print(lst2)
# print(f"After assignment")
# lst1[0] = 11
# print(lst1)
# print(lst2)

# print(f"With copy module")
# from copy import deepcopy
# lst3 = [1, 2]
# lst4 = deepcopy(lst3)
# print(f"Before assignment")
# print(lst3)
# print(lst4)
# print(f"After assignment")
# lst3[0] = 11
# print(lst3)
# print(lst4)


# r1 = Rectangle(1, 1)
# print(f"{r1.a}")
# r2 = r1
# print(f"{r2.a}")
#
# r2.a = 2
# print(f"{r2.a}")
# print(f"{r1.a}")

import copy
print(f"-----")
r1 = Rectangle(1, 1)
r3 = copy.deepcopy(r1)
print(f"{r3.a}")
print(f"{r1.a}")

r3.a = 3
print(f"{r3.a}")
print(f"{r1.a}")








# Student homework

# # Class Employee sukuria objektą pagal atributus name ir employee_list.
# import json
# from tabulate import tabulate
#
#
# class Child:
#     def __init__(self, name, age):
#         pass
#
#
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         self.children = [] # List of Child objects
#
#     # def add_child(self, child_name, child_age):
#     #     pass
#
#     # ... another option is to accept a child object
#     def add_child(self, child: Child):
#         pass
#
#     def remote_child(self, name_of_child_to_remove: str):
#         pass
#
#     def set_salary(self, new_salary):
#         pass
#
#
# class EmployeeHandler(): # EmployeeManager
#     def __init__(self, list_of_employee_dicts):
#         self.employees = None # create a logic, that converts [{}, {}] --> [ Employee(name, salary), Employee(name, salary) ]
#
#
# class Employee:
#
#     def __init__(self, name, employee_list):
#         self.name = name
#         self.employee_list = employee_list
#
#     # find_person - metodas, kuris pagal sukutą objektą grąžina visą informaciją apie jį.
#     # Iš list of dict grąžinamas vienas dict pagal key=name
#     def find_person(self): # šiai funkcijai galima parašyti dekoratorių, kuris jei funkcijos reikšmė None grąžina pranešimą, kitų atveju gražina reikšmę
#         for person in self.employee_list:
#             if person['name'] == self.name:
#                 return person
#
#     # add_person - metodas, kuris iš nurodyto failo įrašo asmenį į pirminį asmenų sąrašą (primary_list)
#     def add_person(self, primary_list): #primary_list - a list to which a new employee will be added
#         if self.find_person():
#             person = self.find_person()
#             primary_list.append(person)
#             print(f'{self.name} has been added to the list.')
#         else:
#             print(f'Error during adding person: there is no such person {self.name} in a list.')
#         return
#
#     # remove_person - metodas, kuris pašalina asmenį iš nurodyto sąrašo
#     def remove_person(self):
#         if self.find_person():
#             person = self.find_person()
#             self.employee_list.remove(person)
#             print(f'{self.name} has been removed from the list.')
#         else:
#             print(f'Error during removing person: there is no such person {self.name} in a list.')
#         return
#
#     # update_salary - metodas, kuris atnaujina asmens salary pagal nurodytą parametrą salary
#     def update_salary(self, salary):
#         if self.find_person():
#             person = self.find_person()
#             person.update({'salary': salary})
#             print(f'Salary was updated for {self.name}: {salary}')
#         else:
#             print(f'Error during updating salary: there is no such person {self.name} in the list')
#         return
#
#     # add_child - metodas, kuris į asmens vaikų sąrašą prideda vaiką su nurodytu vardu child_name ir perskaičiuoja asmens vaikų skaičių no_child
#     def add_child(self, child_name):
#         if self.find_person():
#             person = self.find_person()
#             child_list = person['children_names']
#             no_child = len(child_list)
#             child_list.append(child_name)
#             person.update({'no_children': no_child + 1,'children_names': child_list})
#             print(f'A child {child_name} has been added to {self.name} children list.')
#         else:
#             print(f'Error during adding a child: there is no such person {self.name} in the list.')
#         return
#
#
#     def remove_child(self, child_name):
#         """
#         remove_child - metodas, kuris iš asmens vaikų sąrašo pašalina vaiką su nurodytu vardu child_name
#         ir perskaičiuoja asmens vaikų skaičių no_child
#
#         :param child_name: string of child name
#         :return: False if there is no child to remove, True if child was removed
#         """
#         if self.find_person():
#             person = self.find_person()
#             child_list = person['children_names']
#             no_child = len(child_list)
#             try:
#                 child_list.remove(child_name)
#                 person.update({'no_children': no_child - 1, 'children_names': child_list})
#                 print(f'A child {child_name} has been removed from {self.name} children list.')
#             except ValueError:
#                 print(f'Error during removing a child: {self.name} does not have child named {child_name}.')
#         else:
#             print(f'Error during removing a child: there is no such person {self.name} in the list.')
#         return
#
# # atidaromi du json failai. employee.json - pirminis sąrašas (primary list). new_employee.json - naujų (pridedamų) asmenų sąrašas.
# with open('employees.json', 'r') as employees_file, open('new_employees.json', 'r') as new_employees_file:
#     employees_file_data = json.load(employees_file)
#     new_employees_file_data = json.load(new_employees_file)
#     print(employees_file_data)
#     employee = Employee('Greta', employees_file_data)
#     new_employee = Employee('Ona', new_employees_file_data)
#     # print(employee.find_person()) #None. Padaryti, kad grąžintų ne None, bet pranešimą, kad tokio asmens neranda.
#     # print(new_employee.find_person())
#     employee.add_child('Marta')
#     new_employee.add_person(employees_file_data)
#     # new_employee.remove_child('Marta')
#     # employee.remove_person()
#     # employee.update_salary(1000)
#
# with open('updated_employees.json', 'r+') as updated_file:
#     json.dump(employees_file_data, updated_file, indent=2)
#     updated_file.seek(0) #grįžta į failo pradžią
#     updated_json_object = json.load(updated_file)
#
#     print(tabulate(updated_json_object, headers='keys', tablefmt='github'))