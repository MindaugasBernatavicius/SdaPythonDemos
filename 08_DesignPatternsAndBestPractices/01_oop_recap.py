# Alternative representations in json, xml, txt


# Alternative representations in python
class Product:
    def __init__(self, n, w, l):
        self.name = n
        self.weight_kg = w
        self.length_cm = l


p1 = Product("chair", 10, 100)
p2 = Product("adidas", 15, 12)
list_of_products = [p1, p2]


# alternative?

pd1 = { "name": "chair", "weight_kg": 15, "length_cm": 12 }
pd2 = { "name": "adidas", "weight_kg": 12, "length_cm": 959 }
listd_of_products = [pd1, pd2]

# single property item?

person1 = { "name": "Max"}
person2 = { "name": "Keith"}
people = ["Max", "Keith"] # we might not need property explicitly states


# Derive OOP from the simplest possible
# ... represent a person
# person_simple = "Max"

# ... a bunch properties
person_simple = { "name": "Max", "surname": "Maximilian" }
# person_simple = ["Max", "Maximilian"]


# EXERCISE
# ... what if I have a set of variables for certain property (student grades)?
# ... student is a list --> STUDENT:name,surname,grades
# ... student is a dict
# ... student is an object of class student


class Student:
    def __init__(self, name: str, surname:str, grades:list):
        self.name = name
        self.surname = surname
        self.grades = grades

s = Student('Mark','Markovich',[4, 3, 5, 5])

student_dict = {
    'name': 'Mark',
    'surname': 'Markovich',
    'grades': [4, 3, 5, 5]
}

student_list = ['Mark', 'Markovich', [4, 3, 5, 5]]





s1 = ["Max", "Dey", [8, 9]]
s2 = ["John", "Grate", [10, 9]]
s3 = ["Rita", "Chug", [9, 9]]

# stud_report = {
#     "names": ["Max", "John", "Rita"],
#     "surnames": ["Dey", "Grate", "Chug"],
#     "english_grades": [8, 10, 9],
#     "math_grades": [9, 9, 9]
# }

# print(
#     stud_report["names"][0],
#     stud_report["surnames"][0],
#     stud_report["english_grades"][0],
#     stud_report["math_grades"][0]
# )

stud_report = [
    {
        'name': 'Mark',
        'surname': 'Markovich',
        'grades': [4, 3, 5, 5]
    },
    {
        'name': 'Markus',
        'surname': 'Markusovich',
        'grades': [4, 10, 5, 5]
    }
]
print(stud_report[0])

# average of the first grade
# for student in stud_report:
#    print(sum(student['grades']) / len(student['grades']))

english_grade_idx = 1
grades_list = []
for student in stud_report:
    grades_list.append(student['grades'][english_grade_idx])
print(sum(grades_list) / len(grades_list))




# class StudentReport:
#     def __init__(self, name, surname, grade1, grade2):
#         self.name = name
#         self.surname = surname
#         self.grade1 = grade1
#         self.grade2 = grade2
#
# s1 = StudentReport("Max", "Dey", 8, 9)
# s2 = StudentReport("John", "Grate", 10, 9)
# s3 = StudentReport("John", "Grate", 9, 9)




