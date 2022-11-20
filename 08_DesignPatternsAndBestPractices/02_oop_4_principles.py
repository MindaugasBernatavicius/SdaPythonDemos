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



p1 = Person("John", 55)
p1.age = 78
print(p1.age)

# Does this representation (dict) have any way to encapsulate the data? --> NO.
# Do other representations (list of list) have encapsulation? --> NO.
person = {
    "name": "Max",
    "age": 55
}


def validate_person_dict(p):
    pass


class Employee(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.__role = role

    def __str__(self) -> str:
        super_str = super(Employee, self).__str__()[:-1] + rf", role: '{self.__role}' }}"
        return super_str


class Student(Person):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.__grades = []


e = Employee("Janett", 44, "Janitor")
print(e)