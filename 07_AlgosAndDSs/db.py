import time

# ############## 1
# mystr = "Mindaugas"
#
# t0 = time.time()
# for i in range(0, 10000):
#     finalstr = ""
#     for i in range(len(mystr)-1, -1, -1):
#         finalstr += mystr[i]
# t1 = time.time()
#
# print(t1-t0)
# print(finalstr)

# ############## 2
# mystr = "Mindaugas"
#
# t0 = time.time()
# for i in range(0, 10000):
#     mylst = []
#     for i in range(len(mystr)-1, -1, -1):
#         # print(f'{i}:{mystr[i]}')
#         mylst.append(mystr[i])
#     final = ''.join(mylst)
# t1 = time.time()
#
# print(t1-t0)
# print(final)
# print(''.join(mylst))


# myinput = input("Please enter something: ")
# print(myinput)


# def factorial(n):
#     if n == 0:
#         return 1              # base case
#     return n * factorial(n-1) # recursive step
#
# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result = result * i
#     return result
#
# # testcase 1
# print(factorial(5))     # 120
# print(factorial(1))     # 1
# print(factorial(0))     # 1
# print(factorial(20))    # 2432902008176640000



# def fib(n):
#     if n <= 1: return n
#     return fib(n-1) + fib(n-2)

# memoization (vienas iš optimizacijos būdų)
# cache = {}
# def fib(n):
#     res = 0
#     if n in cache:
#         return cache[n]
#     elif n <= 1:
#         res = n
#     elif n > 1:
#         res = fib(n-1) + fib(n-2)
#     cache[n] = res
#     return res
#
# print(fib(0))
# print(fib(1))
# print(fib(2))
# print(fib(3))
# print(fib(7))
# print(fib(10))

######################################################################
# Time profiling
######################################################################

# import time
#
# t0 = time.time()
#
# l = []
# for i in range(0, 1000000):
#     # print("AAAAAAAAAAAA" + str(i))
#     l.append("AAAAAAAAAAAA" + str(i))
#
# t1 = time.time()
# print(t1 - t0)
#
# # Paklaida auga augant absolučiam laikui, kurį užtrunka "algoritmas":
# # - kai n 100_000 ==> ~0.002
# # - 0.027997493743896484
# # - 0.028000831604003906
# # - 0.026998519897460938
# # - 0.02599930763244629
#
# # - kai n 1_000_000 ==> ~0.02
# # - 0.29251575469970703
# # - 0.2899971008300781
# # - 0.29000067710876465
# # - 0.31004858016967773


# import time
#
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)
#
# t00 = time.time()
#
# n = 36
# l = []
# for i in range(1, n+1):
#     l.append(fib(i))
#
# t11 = time.time()
# print('pirmas fib: ', t11 - t00)

######################################################################
# cache = {}
# # n = 360000 * 2
# n = 1000
#
# def fib(n):
#     res = 0
#     if n in cache:
#         return cache[n]
#     elif n <= 1:
#         res = n
#     elif n > 1:
#         res = fib(n - 1) + fib(n - 2)
#     cache[n] = res
#     return res
#
# t0 = time.time()
#
# l = []
# for i in range(1, n+1):
#     l.append(fib(i))
#
# t1 = time.time()
# print('antras fib: ', t1 - t0)


###################################################################
# Memory profiling
###################################################################

# Simple fib()
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)
#
# if __name__ == '__main__':
#     from memory_profiler import memory_usage
#     mem_usage = memory_usage((fib, [20]))
#     print('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
#     print('Maximum memory usage: %s' % max(mem_usage))

# # Memoized fib()
# import time
# cache = {}
# def fib(n):
#     res = 0
#     if n in cache:
#         return cache[n]
#     elif n <= 1:
#         res = n
#     elif n > 1:
#         res = fib(n - 1) + fib(n - 2)
#     cache[n] = res
#     # time.sleep(0.01)
#     return res
#
# fib(100)

# if __name__ == '__main__':
#     import sys
#     sys.setrecursionlimit(3000)
#     from memory_profiler import memory_usage
#     mem_usage = memory_usage((fib, [1000]))
#     print('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
#     print('Maximum memory usage: %s' % max(mem_usage))



# import time
# from memory_profiler import profile
#
# cache = {}
# def fib(n):
#     res = 0
#     if n in cache:
#         return cache[n]
#     elif n <= 1:
#         res = n
#     elif n > 1:
#         res = fib(n - 1) + fib(n - 2)
#     cache[n] = res
#     # time.sleep(0.01)
#     return res
#
#
# @profile
# def profile_fib():
#     cache = {}
#     def fib(n):
#         res = 0
#         if n in cache:
#             return cache[n]
#         elif n <= 1:
#             res = n
#         elif n > 1:
#             res = fib(n - 1) + fib(n - 2)
#         cache[n] = res
#         # time.sleep(0.01)
#         return res
#     fib(500)
#
# # ... profiling using memory_profiler with global function and cache
# # if __name__ == '__main__':
# #     import sys
# #     sys.setrecursionlimit(3000)
# #     from memory_profiler import memory_usage
# #     mem_usage = memory_usage((fib, [2500]))
# #     print('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
# #     print('Maximum memory usage: %s' % max(mem_usage))
#
# # ... profiling using memory_profiler with separate function
# # if __name__ == '__main__':
# #     profile_fib()
#
# # simple profiling - checking the difference of cache after execution of the function
# if __name__ == '__main__':
#     import sys
#     print(sys.getsizeof(cache))
#     # profile_fib()
#     fib(100)
#     print(sys.getsizeof(cache))


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
# bisect.insort(nums, 2)
# print(f"After: {nums}")
#
#
# def find(nums, num):
#     i = bisect.bisect_left(nums, num)
#     if i != len(nums) and nums[i] == num:
#         return i
#     raise ValueError
#
# l_ints = [1,2,2,2,4,7,9,10,55,66,125]
# print(find(l_ints, 10))
# print(l_ints[find(l_ints, 10)])

def binary_search_raw(arr, needle):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < needle:
            low = mid + 1
        elif arr[mid] > needle:
            high = mid - 1
        else:
            return mid
    return -1

def binary_search_w_bisect(nums, num):
    i = bisect.bisect_left(nums, num)
    if i != len(nums) and nums[i] == num:
        return i
    raise ValueError

def linear_search(lst, needle):
    for item in lst:
        if item == needle:
            return True
    return False

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
import time
import random

# print(random.uniform(0, 20))

# ... generate data
numbers_list = []
start = 0
stop = 100000
for i in range(start, stop):
    numbers_list.append(random.uniform(0, 2000))
    # numbers_list.append(i)

numbers_list.sort()

# ... run experiments in a loop
experiment_results = []
function_results = []
# t_loop_0 = time.time()
for experiment in range(0, 1000):
    t0 = time.time()
    # binary_search_raw(numbers_list, random.randint(start, stop))
    # res = binary_search_raw(numbers_list, numbers_list[random.randint(start, stop)])        # Average time taken: 2.9985904693603516e-06
    # res = linear_search(numbers_list, numbers_list[random.randint(start, stop-1)])
    res = binary_search_w_bisect(numbers_list, numbers_list[random.randint(start, stop-1)])   # Average time taken: 1.9986629486083982e-06
    t1 = time.time()
    function_results.append(res)
    experiment_results.append(t1-t0)
# t_loop_1 = time.time()

# calculate the average
# print(f'Sum of all time taken: { t_loop_1 - t_loop_0}')
print(f'Sum of all loops taken: { sum(experiment_results) }')
print(f'Average time taken: { sum(experiment_results) / len(experiment_results) }')
print(f'Function results {function_results}')