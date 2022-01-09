
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

# def bubbleSort(arr):
#     n = len(arr)
#     iterations = 0
#     for i in range(n - 1):
#         for j in range(0, n - 1):
#             iterations += 1
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     print(f"iterations: {iterations}")


# passing comparator
def bubbleSort(arr, comparer):
    n = len(arr)
    iterations = 0
    for i in range(n - 1):
        swapped = False
        if not swapped:
            for j in range(0, n - i - 1):
                iterations += 1
                if comparer(arr[j], arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
    print(f"iterations: {iterations}")

from dataclasses import dataclass

@dataclass
class Employee:
    age: int

arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Before: {arr}")
# bubbleSort(arr)
bubbleSort(arr, lambda x, y: x < y)
print(f"After: {arr}")

arr = [Employee(64), Employee(34), Employee(25), Employee(12), Employee(22), Employee(11), Employee(90)]
print(f"Before: {arr}")
bubbleSort(arr, lambda x, y: x.age < y.age)
print(f"After: {arr}")