lst = [4, 3, 2, 1]

print(f'Before sorting: {lst}')


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
#
# for i in range(0, len(lst)-1):
#     if lst[i] > lst[i+1]:
#         lst[i], lst[i+1] = lst[i+1], lst[i]
#
# for i in range(0, len(lst)-1):
#     if lst[i] > lst[i+1]:
#         lst[i], lst[i+1] = lst[i+1], lst[i]
#
# for i in range(0, len(lst)-1):
#     if lst[i] > lst[i+1]:
#         lst[i], lst[i+1] = lst[i+1], lst[i]

# for i in range(0, len(lst)):
#     for j in range(0, len(lst)-1):
#         if lst[j] > lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]

# def bubble_sort(lst):
#     for i in range(0, len(lst)):
#         for j in range(0, len(lst) - 1):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]

# Bubble sort'as yra nenaudotinas ir nenaudojamas realiame software engineering
# ... tai kam jį išvis jį rodyti. 2 dalykai:
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

def bubble_sort_1_optimization(lst):
    iter_counter, swap_counter = 0, 0
    for i in range(0, len(lst)):
        for j in range(0, len(lst) - 1 - i):
            iter_counter += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap_counter += 1
    print(f'Iterations: {iter_counter}, swaps: {swap_counter}')

# 2-a optimizacija. Pažvelkime kaip veikia algoritmas
# ... jei paduotume beveik surikiuotą listą
# almost_sorted_lst = [1, 3, 2, 4]
presorted_lst = [1, 2, 3, 4, 5, 6]

def bubble_sort_2_optimizations(lst):
    iter_counter, swap_counter = 0, 0
    for i in range(0, len(lst)):
        swapped = False
        for j in range(0, len(lst) - 1 - i):
            iter_counter += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
                swap_counter += 1
        if not swapped:
            print(f'Iterations: {iter_counter}, swaps: {swap_counter}')
            return

    print(f'Iterations: {iter_counter}, swaps: {swap_counter}')


# bubble_sort(lst)                  # Iterations: 12, swaps: 6
# bubble_sort_1_optimization(lst)   # Iterations: 6, swaps: 6
# print(f'After sorting: {lst}')

# print(f'Before sorting: {presorted_lst}')
# # bubble_sort_1_optimization(almost_sorted_lst)
# # bubble_sort_2_optimizations(almost_sorted_lst)
#
# # bubble_sort_1_optimization(presorted_lst) # Iterations: 6, swaps: 0
# bubble_sort_2_optimizations(presorted_lst)  # Iterations: 3, swaps: 0
#
# print(f'After sorting: {presorted_lst}')

# Kiekvienas rikiavimo algoritmas turi:
# - pereiti narius (visus ar beveik visus)
# - palyginti narius, kad žinotų ar reikia apkeisti vietomis
# - apkeitimo operacija - swap


# Sort reverse, sort function with custom compare logic
# ... first option
def bubble_sort(lst, reverse=False):
    for i in range(0, len(lst)):
        for j in range(0, len(lst) - 1):
            if reverse: # reverse order (decreasing if numbers are used)
                if lst[j] < lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
            else: # default order (increasing if numbers are used)
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]

list_to_reverse = [1, 2, 3, 4, 5, 6]
print(f'Before sorting: {list_to_reverse} w/ reverse')
bubble_sort(list_to_reverse, reverse=True)
print(f'After sorting: {list_to_reverse} w/ reverse')

# ... now let's try sorting objects
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{{name: {self.name}, age: {self.age}}}"

    def __gt__(self, other):
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

# ... passing compare logic dynamically
def bubble_sort_with_dynamic_comparator(lst, compare):
    for i in range(0, len(lst)):
        for j in range(0, len(lst) - 1):
            if compare(lst[j], lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


print(f'Before sorting: {list_of_employees}')
# bubble_sort_with_dynamic_comparator(list_of_employees, lambda p1, p2: p1.age > p2.age)
# bubble_sort_with_dynamic_comparator(list_of_employees, lambda p1, p2: p1.age < p2.age)
# bubble_sort_with_dynamic_comparator(list_of_employees, lambda p1, p2: p1.name > p2.name)
# bubble_sort_with_dynamic_comparator(list_of_items, lambda i1, i2: i1.price > i2.price)

# after overloading the ">" operator
bubble_sort_2_optimizations(list_of_employees)
print(f'After sorting: {list_of_employees}')

# > -- __gt__
# < -- __lt__
print(Employee("Jonas", 51) > Employee("Petras", 61))
print(Employee("Petras", 61) > Employee("Jonas", 51))

# .. how to sort with default python sort() method
print(f'Before sorting: {list_of_employees}')
list_of_employees.sort(key=lambda e: e.name, reverse=True)
print(f'After sorting: {list_of_employees}')

# ... how to sort by multiple fields?
# ... REMEMBER: the second and subsequent properties are used only when
# ... the object are equal by previous properties
print(f'Before sorting: {list_of_employees}')
list_of_employees.sort(key=lambda e: (e.name, -e.age), reverse=True)
print(f'After sorting: {list_of_employees}')