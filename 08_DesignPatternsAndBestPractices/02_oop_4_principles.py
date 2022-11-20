# Encapsulation
class Person:
    def __init__(self, name, age):
        self.__name = name # public, private, protected
        self.__age = age

    @property # getter, accessor
    def age(self):
        return self.__age

    @age.setter # setter, mutator
    def age(self, age):
        if age <= 0 or age >= 150:
            raise Exception("Invalid value for age property")
        self.__age = age

    def __str__(self) -> str:
        # return str({ "name": self.name , "age": self.age })
        obj_dict = {"name": self.__name, "age": self.__age}
        return f"{obj_dict}"
        # return "{\"name\": \"" + self.name + "\", \"age\": " + str(self.age) +" }"



# p1 = Person("John", 55)
# p1.age = 78
# print(p1.age)

# Does this representation (dict) have any way to encapsulate the data? --> NO.
# Do other representations (list of list) have encapsulation? --> NO.
person = {
    "name": "Max",
    "age": 55
}


def validate_person_dict(p):
    pass

# Inheritence
class Employee(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.__role = role

    def __str__(self) -> str:
        # super_str = super(Employee, self).__str__()
        super_str = super(Employee, self).__str__()[:-1] + rf", 'role': '{self.__role}' }}"
        return super_str


class Student(Person):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.__grades = []


e = Employee("Janett", 44, "Janitor")
print(e)



# Polymorphism
class Shape:
    pass

class Triangle(Shape):
    pass

class Square(Shape):
    pass

class ShapeCalculator:
    def calculate_area(self, shape: Shape) -> None:
        pass

shape_cal = ShapeCalculator()
shape_cal.calculate_area("dsdvsdvsd")
shape_cal.calculate_area(Shape())
shape_cal.calculate_area(Triangle()) # polymorphism


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
    def __init__(self, firstname: str, middlename: str, lastname: str):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname

    def create_initials(self):
        return f"{self.firstname[0] + self.lastname[1]}"


class Person:
    def __init__(self, age: int, fullname: Fullname): # bloodtype: BloodType
        self.age = age
        self.fullname = fullname


Person(42, Fullname("Robert", "Jr.", "Downey"))