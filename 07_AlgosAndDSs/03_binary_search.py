# # linear search
# l = [5,4,99,10]
#
# def linear_search(lst, needle):
#     for item in lst:
#         if item == needle:
#             return True
#     return False
#
# needle = 100
# print(f"Does the list contain {needle}: { linear_search(l, needle) }")



# import datetime
# # l_mixed = ["Jonas", "Antanas", 10, 25, datetime.datetime(2021, 1, 1), datetime.datetime(2020, 1, 1)]
# # l_mixed = [datetime.datetime(2021, 1, 1), datetime.datetime(2020, 1, 1)]
# l_mixed = ["Zita", "Antanas", "Mindaugas"]
#
# print(f'Before sorting: {l_mixed}')
# l_mixed.sort(reverse=True) # TypeError: '<' not supported between instances of 'int' and 'str'
# print(f'After sorting: {l_mixed}')


# ... binary search
import bisect

# nums = [1,2,2,2,4,7,9]
# print(bisect.bisect(nums, 3))
# print(bisect.bisect(nums, 2))
# print(bisect.bisect_left(nums, 2))

# print(f"Before: {nums}")
# bisect.insort(nums, 5)
# print(f"After: {nums}")


# def find(nums, num):
#     i = bisect.bisect_left(nums, num)
#     if i != len(nums) and nums[i] == num:
#         return i
#     raise ValueError
#
# l_ints = [1,2,2,2,4,7,9,10,55,66,125]
# print(find(l_ints, 10))
# print(l_ints[find(l_ints, 10)])

def binary_search(haystack, needle):
    start, middle, end = 0, 0, len(haystack) - 1
    while start <= end:
        middle = (start + end) // 2
        if haystack[middle] == needle:
            return middle
        elif haystack[middle] > needle:
            end = middle - 1
        elif haystack[middle] < needle:
            start = middle + 1
    raise ValueError("The number was not found!")
    # return -1

# Testcases
# print(binary_search([], 1))
# print(binary_search([1], 2))
# print(binary_search([2], 2))
# print(binary_search([1, 2], 2))
# print(binary_search([1, 2, 3], 3))
# print(binary_search([1, 2, 2, 3, 66, 69, 71], 66))
# print(binary_search([-17, -16, 5, 10, 25], -16))


def binary_search_recursive(haystack, start, end, needle):
    # TODO :: this needs to be fixed, potentially introducing another condition in the first if
    if start <= end and len(haystack) < start + end:
        middle = (start + end) // 2
        if haystack[middle] == needle:
            return middle
        elif haystack[middle] > needle:
            return binary_search_recursive(haystack, start, middle - 1, needle)
        elif haystack[middle] < needle:
            return binary_search_recursive(haystack, middle + 1, end, needle)
    else:
        return -1

# Testcases
# ... there is a mistake in this code: https://www.geeksforgeeks.org/python-program-for-binary-search/
# ... the case where an empty list is passed it not solved
# print(binary_search_recursive([], 0, len([]), 1))
# print(binary_search_recursive([1], 0, len([1]), 2))
# print(binary_search_recursive([2], 0, len([2]), 2))
# print(binary_search_recursive([1, 2], 0, len([1, 2]), 2))
# print(binary_search_recursive([1, 2, 3], 0, len([1, 2, 3]), 3))


# def binary_search_w_bisect(nums, num):
#     i = bisect.bisect_left(nums, num)
#     if i != len(nums) and nums[i] == num:
#         return i
#     raise ValueError

# def linear_search(lst, needle):
#     for item in lst:
#         if item == needle:
#             return True
#     return False

################################################################################################################################
# - įrodykite pavyzdžiu, jog algoritmas randa norimą skaičių, stringą/tekstą ir datą atitinkamai skaičių, stringų ir datų liste
################################################################################################################################
# - algoritmas randa norimą
#   - skaičių - skaičių liste
#   - stringą/tekstą - stringų liste
#   - datą - datų liste

# lst_ints = [1,2,4,7,9,10,55,66,125]
# possition = 7
# res = binary_search_raw(lst_ints, lst_ints[possition])
# print(f'Function returned: {res}, we searched for: {possition}, they are equal: {res == possition}')
#
# lst_str = ["Adelė", "Jonas", "Mindaugas", "Zita"]
# possition = 2
# res = binary_search_raw(lst_str, lst_str[possition])
# print(f'Function returned: {res}, we searched for: {possition}, they are equal: {res == possition}')
#
# import datetime
# lst_dates = [datetime.datetime(2019, 1, 1), datetime.datetime(2020, 1, 1), datetime.datetime(2021, 1, 1), datetime.datetime(2022, 1, 1)]
# res = binary_search_raw(lst_dates, datetime.datetime(2021, 1, 1))
# print(f'Function returned: {res}, we searched for: {possition}, they are equal: {res == possition}')

################################################################################################################################
# - atsakykite į klausimą ar šis algoritmas veikia teisingai jei duomenys surikuoti atvirkštine tvarka (default yra didėjimo, abecelinė ir chronologinė)
################################################################################################################################
# lst_str = ["Adelė", "Jonas", "Mindaugas", "Zita"]
# possition = 2
#
# lst_str.sort(reverse=True)
# res = binary_search_raw(lst_str, lst_str[possition])
# print(f'Function returned: {res}, we searched for: {possition}, they are equal: {res == possition}')
#
# lst_str.sort()
# res = binary_search_raw(lst_str, lst_str[possition])
# print(f'Function returned: {res}, we searched for: {possition}, they are equal: {res == possition}')

################################################################################################################################
# - pateikite pavyzdį kai šis paieškos algoritmas nesuveikia
################################################################################################################################
# pateikta prieš tai

################################################################################################################################
# - pamatuokite laiką, kiek greičiau veikia binary search vs. linear vs. binary search su bisect moduliu
################################################################################################################################
# import time
# import random
#
# # print(random.uniform(0, 20))
#
# # ... generate data
# numbers_list = []
# start = 0
# stop = 100000
# for i in range(start, stop):
#     numbers_list.append(random.uniform(0, 2000))
#     # numbers_list.append(i)
#
# numbers_list.sort()
#
# # ... run experiments in a loop
# experiment_results = []
# function_results = []
# # t_loop_0 = time.time()
# for experiment in range(0, 1000):
#     t0 = time.time()
#     # binary_search_raw(numbers_list, random.randint(start, stop))
#     # res = binary_search_raw(numbers_list, numbers_list[random.randint(start, stop)])        # Average time taken: 2.9985904693603516e-06
#     # res = linear_search(numbers_list, numbers_list[random.randint(start, stop-1)])
#     res = binary_search_w_bisect(numbers_list, numbers_list[random.randint(start, stop-1)])   # Average time taken: 1.9986629486083982e-06
#     t1 = time.time()
#     function_results.append(res)
#     experiment_results.append(t1-t0)
# # t_loop_1 = time.time()
#
# # calculate the average
# # print(f'Sum of all time taken: { t_loop_1 - t_loop_0}')
# print(f'Sum of all loops taken: { sum(experiment_results) }')
# print(f'Average time taken: { sum(experiment_results) / len(experiment_results) }')
# print(f'Function results {function_results}')


# Homework
# - find_last(haystack, needle) --> given an array, find the last item that is the same as needle (pay attention to dublicates!)

def find_last(haystack, needle):
    for item in haystack[::-1]:
        if item == needle:
            last_item_index = len(haystack) - haystack[::-1].index(item) - 1
            return f'The last {needle} in {haystack} is in {last_item_index} position'
    return f'{needle} was not found in {haystack}'

haystack_0 = [0, 1, 5, 100, 5]
print(haystack_0[::-1])

haystack_1 = [0, 1, 5, 100, 5]
haystack_2 = [1, 1]
haystack_3 = []
haystack_4 = [-1, -2, -3, 6, 6, 5, -3]

# testcases
print(find_last(haystack_0, 5))
print(find_last(haystack_1, 3))
print(find_last(haystack_2, 1))
print(find_last(haystack_3, 0))
print(find_last(haystack_4, 6))
