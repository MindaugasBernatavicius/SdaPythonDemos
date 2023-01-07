# Encapsulation
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1 = Person("John", 55)
# print(p1.name)
# p1.name = ""
# print(f">> {p1.name}")


class Person:
    def __init__(self, name, age):
        if name == "":
            raise ValueError("Name can not be empty")
        self.__name = name # public, private, protected
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, new_value):
        if new_value == "":
            raise ValueError("Name can not be empty")
        self.__name = new_value

    # @property # getter, accessor
    # def age(self):
    #     return self.__age
    #
    # @age.setter # setter, mutator
    # def age(self, age):
    #     if age <= 0 or age >= 150:
    #         raise Exception("Invalid value for age property")
    #     self.__age = age

    def __str__(self) -> str:
        # return str({ "name": self.name , "age": self.age })
        obj_dict = { "name": self.__name, "age": self.__age }
        return f"{obj_dict}"
        # return "{\"name\": \"" + self.name + "\", \"age\": " + str(self.age) +" }"



p1 = Person("John", 55)
print(p1)

# print(p1.get_name())
p1.set_name("Peter")
# p1.set_name("")
# print(p1.get_name())

print(p1)

# Does this representation (dict) have any way to encapsulate the data? --> NO.
# Do other representations (list of list) have encapsulation? --> NO.
person = {
    "name": "Max",
    "age": 55
}

print(person)
person["age"] = 1000
print(person)

def validate_person_dict(p):
    pass

# Inheritence, D.R.Y
class Test: pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

class Student(Person): pass
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age


class Employee(Person): pass
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age


# t1 = Test("A")
p1 = Employee("Jon", 55)
s1 = Student("Jon Jr.", 25)


# print(p1.name, s1.name)


# ... in order to create a new class we ussually need a reason,
# ... that reason needs to answer the question: why. We will create
# ... Employee and Student classes - why? Because we will hold specific information for the represented object, role and grades

class Employee(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.__role = role

    def __str__(self) -> str:
        # return f"{self.name}, {self.age}, {self.__role}"
        # return super(Employee, self).__str__()
        return f"{{ { super(Employee, self).__str__()  }, 'role': '{self.__role}' }}"



class Student(Person):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.__grades = grades # []

print("-------------")
e = Employee("Janett", 44, "Janitor")
print(e)

s = Student("Peter", 44, [5, 9])
print(s)



# Polymorphism - the ability to interchange parent objects and child objects (polymorphic collections, polymorphic parameters to functions)
# ... related overriding - child can provide a specif version of a method that the parent has
class Shape:
    pass

# Triangle is-a shape? YES!
class Triangle(Shape):
    pass

class Square(Shape):
    pass

class ShapeCalculator:
    def calculate_area(self, shape: Shape) -> None:
        # ... this is where the area is calculated
        # shape.get_width()
        return None

shape_cal = ShapeCalculator()
# shape_cal.calculate_area("dsdvsdvsd")
# shape_cal.calculate_area(Shape())
shape_cal.calculate_area(Triangle()) # polymorphism
shape_cal.calculate_area(Square()) # polymorphism

# ... in collections
lst: list[Person] = []
# lst.append(Triangle())




# Composition
class Engine:
    def __init__(self, brand, hp):
        self.brand = brand
        self.hp = hp


class Car:
    def __init__(self, brand: str, engine: Engine):
        self.brand = brand
        self.engine = engine

Car("Audi", Engine("China Corp.", 150))


class Fullname:
    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname
        self.initials = firstname[0] + '.' + lastname[0]

    def __str__(self) -> str:
        return f"{self.firstname} : { self.lastname} : {self.initials}"


class Person:
    def __init__(self, age: int, fullname: Fullname): # bloodtype: BloodType
        self.age = age
        self.fullname = fullname

    def __str__(self) -> str:
        return f"{self.age} : {self.fullname}"

p = Person(42, Fullname("Robert", "Downey"))
print(p)