# lst = [4, 3, 2, 1]
# print(f'Before sorting: {lst}')

# Step by step

# Non pythonic - swap
# a = 1
# b = 2
# print(f"Before: a={a}, b={b}")
# tmp = a
# a = b
# b = tmp
# print(f"After: a={a}, b={b}")

# Pythonic way - swap
# a = 1
# b = 2
# print(f"Before: a={a}, b={b}")
# a, b = b, a
# print(f"After: a={a}, b={b}")

# for i in range(0, len(lst)-1):
#     if lst[i] > lst[i+1]:
#         lst[i], lst[i+1] = lst[i+1], lst[i]

# ... is this enough?
# print(f'After sorting: {lst}')

# for i in range(0, len(lst)):
#     for j in range(0, len(lst)-1):
#         if lst[j] > lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
#
# print(f'After sorting: {lst}')

# def bubble_sort(lst):
#     for i in range(0, len(lst)):
#         for j in range(0, len(lst) - 1):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]

# Bubble sort'as yra nenaudotinas ir nenaudojamas realiame software engineering
# ... tai kam jį išvis jį rodyti / mokytis. 2-i priežastys:
# - paprastas būdas paaiškinti ką turi daryti visi sort algoritmai
# - egzistuoja net 2 paprastos, studentams atrandamos (performance) optimizacijos!


# 1-ma optimizacija - nereikia eiti iki galo visą laiką, nes po kiekvienos iteracijos
# ... didėja išrikiuotų narių particija (kuri yra gale) - reiškia reiktų anksčiau sustoti

# def bubble_sort(lst):
#     iter_counter, swap_counter = 0, 0
#     for i in range(0, len(lst)):
#         for j in range(0, len(lst) - 1):
#             iter_counter += 1
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#                 swap_counter += 1
#     print(f'Iterations: {iter_counter}, swaps: {swap_counter}')


# def bubble_sort_1_optimization(lst):
#     iter_counter, swap_counter = 0, 0
#     for i in range(0, len(lst)):
#         for j in range(0, len(lst) - 1 - i):
#             iter_counter += 1
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#                 swap_counter += 1
#     print(f'Iterations: {iter_counter}, swaps: {swap_counter}')

# lst = [4, 3, 2, 1]
# print(f'Before sorting: {lst}')
# bubble_sort_1_optimization(lst)
# print(f'After sorting: {lst}')

# 2-a optimizacija. Pažvelkime kaip veikia algoritmas
# ... jei paduotume beveik surikiuotą listą
# almost_sorted_lst = [1, 3, 2, 4]
# presorted_lst = [1, 2, 3, 4, 5, 6]

# def bubble_sort_2_optimizations(lst):
#     iter_counter, swap_counter = 0, 0
#     for i in range(0, len(lst)):
#         swapped = False
#         for j in range(0, len(lst) - 1 - i):
#             iter_counter += 1
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#                 swapped = True
#                 swap_counter += 1
#         if not swapped:
#             print(f'Iterations: {iter_counter}, swaps: {swap_counter}')
#             return
#     print(f'Iterations: {iter_counter}, swaps: {swap_counter}')


# print(f'Before sorting: {presorted_lst}')
# bubble_sort_1_optimization(presorted_lst)
# bubble_sort_2_optimizations(presorted_lst)
# print(f'After sorting: {presorted_lst}')

# Kiekvienas rikiavimo algoritmas turi:
# - pereiti narius (visus ar beveik visus)
# - palyginti narius, kad žinotų ar reikia apkeisti vietomis
# - apkeitimo operacija - swap


# Sort reverse, sort function with custom compare logic
# ... first option
# def bubble_sort(lst, reverse=False):
#     for i in range(0, len(lst)):
#         for j in range(0, len(lst) - 1):
#             if reverse: # reverse order (decreasing if numbers are used)
#                 if lst[j] < lst[j + 1]:
#                     lst[j], lst[j + 1] = lst[j + 1], lst[j]
#             else: # default order (increasing if numbers are used)
#                 if lst[j] > lst[j + 1]:
#                     lst[j], lst[j + 1] = lst[j + 1], lst[j]

# list_to_reverse = [1, 2, 3, 4, 5, 6]
# print(f'Before sorting: {list_to_reverse} w/ reverse')
# bubble_sort(list_to_reverse, reverse=True)
# print(f'After sorting: {list_to_reverse} w/ reverse')

# NOTE: sorting in reverse can only be defined if there is
# ... some standard / default sorting order. Is there such an order? YES
# ... for numbers the default is increasing order (min -> max), so the reverse is decreasing
# ... for letters / strings default is alphabetical order (a -> z), reverse - reverse alphabetical ordering (z - a)
# ... for dates default is chronological order and reverse is counter-chronological order
print("a" < "b")

# ... now let's try sorting objects
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{{name: {self.name}, age: {self.age}}}"

    def __gt__(self, other): # >
        if self.age > other.age:
            return True
        else:
            return False


class Item:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __repr__(self):
        return f"{{name: {self.title}, age: {self.price}}}"


list_of_employees = [
    Employee("Jonas", 51),
    Employee("Adelė", 20),
    Employee("Petras", 25),
    Employee("Adelė", 48),
    Employee("Pencas", 65),
]

list_of_items = [
    Item("Stalas", 21.99),
    Item("Kėdė", 9.99),
    Item("Suolas", 18.99),
]

# ATTENTION: we can not compare custom types
# ... like Employee by default Employee < Employee ???
# ... we need to define what it means for one employee to be
# ... more than the other

# def bubble_sort(lst, reverse=False):
#     for i in range(0, len(lst)):
#         for j in range(0, len(lst) - 1):
#             if reverse: # reverse order (decreasing if numbers are used)
#                 if lst[j].age < lst[j + 1].age:
#                     lst[j], lst[j + 1] = lst[j + 1], lst[j]
#             else: # default order (increasing if numbers are used)
#                 if lst[j].age > lst[j + 1].age:
#                     lst[j], lst[j + 1] = lst[j + 1], lst[j]

# ... passing compare logic dynamically
# def bubble_sort_with_dynamic_comparator(lst, compare):
#     for i in range(0, len(lst)):
#         for j in range(0, len(lst) - 1):
#             if compare(lst[j], lst[j + 1]):
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]


# print(f'Before sorting: {list_of_employees}')
# bubble_sort(list_of_employees)

# bubble_sort_with_dynamic_comparator(list_of_employees, lambda e1, e2: e1.age > e2.age)
# bubble_sort_with_dynamic_comparator(list_of_employees, lambda p1, p2: p1.age < p2.age)
# bubble_sort_with_dynamic_comparator(list_of_employees, lambda p1, p2: p1.name > p2.name)
# bubble_sort_with_dynamic_comparator(list_of_items, lambda i1, i2: i1.price > i2.price)

# # after overloading the ">" operator
# bubble_sort_2_optimizations(list_of_employees)
# print(f'After sorting: {list_of_items}')

# # > -- __gt__
# # < -- __lt__
# print(Employee("Jonas", 51) > Employee("Petras", 61))
# print(Employee("Petras", 61) > Employee("Jonas", 51))


# .. how to sort with default python sort() method
# print(f'Before sorting: {list_of_employees}')
# list_of_employees.sort(key=lambda e: e.name, reverse=True)
# print(f'After sorting: {list_of_employees}')

# ... how to sort by multiple fields?
# ... REMEMBER: the second and subsequent properties are used only when
# ... the object are equal by previous properties
# print(f'Before sorting: {list_of_employees}')
# # list_of_employees.sort(key=lambda e: (e.name, -e.age), reverse=True)
# list_of_employees.sort(key=lambda e: (e.name, e.age), reverse=True)
# print(f'After sorting: {list_of_employees}')



# no optimized
# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(0, n - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# first optimization
# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# second optimization
# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         swapped = False
#         if not swapped:
#             for j in range(0, n - i - 1):
#                 if arr[j] > arr[j + 1]:
#                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                     swapped = True

# calculate the iterations
# def bubbleSort(arr):
#     n = len(arr)
#     iterations = 0
#     for i in range(n - 1):
#         swapped = False
#         if not swapped:
#             for j in range(0, n - i - 1):
#                 iterations += 1
#                 if arr[j] > arr[j + 1]:
#                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                     swapped = True
#     print(f"iterations: {iterations}")

def bubbleSort(arr):
    n = len(arr)
    iterations = 0
    for i in range(n - 1):
        for j in range(0, n - 1):
            iterations += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(f"iterations: {iterations}")


# passing comparator
# def bubbleSort(arr, comparer):
#     n = len(arr)
#     iterations = 0
#     for i in range(n - 1):
#         swapped = False
#         if not swapped:
#             for j in range(0, n - i - 1):
#                 iterations += 1
#                 if comparer(arr[j], arr[j + 1]):
#                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                     swapped = True
#     print(f"iterations: {iterations}")


from dataclasses import dataclass

@dataclass
class Employee:
    age: int

# arr = [64, 34, 25, 12, 22, 11, 90]
# print(f"Before: {arr}")
# # bubbleSort(arr)
# bubbleSort(arr, lambda x, y: x < y)
# print(f"After: {arr}")

# arr = [Employee(64), Employee(34), Employee(25), Employee(12), Employee(22), Employee(11), Employee(90)]
# print(f"Before: {arr}")
# bubbleSort(arr, lambda x, y: x.age < y.age)
# print(f"After: {arr}")


from dataclasses import dataclass, field

@dataclass (order=True)
class Person:
    # sort_index: int = field(init=False, repr=False)
    comp_age: int = field(init=False, repr=False)
    comp_strength: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100


    def __post_init__(self):
        # self.sort_index = self.age
        self.comp_age = self.age
        self.comp_strength = -self.strength


person1 = Person("Geralt", "Witcher", 20)
person2 = Person("Yannefer", "Sarceress", 25, 10)
person3 = Person("Yannefer", "Sarceress", 25, 1000)

#
# print(f'person1: {person1}')
# print(f'person2: {person2}')
# print(f'person1 > person2: {person1 > person2}')

lst = [person1, person2, person3]
print(f"Before: {lst}")
# bubbleSort(lst)
lst.sort()
print(f"After: {lst}")
