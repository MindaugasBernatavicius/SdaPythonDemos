######################################
# 0. function calling another function
######################################
# def total_length(a, b):
#     return len(a) + len(b)

######################################
# 1. Recursion limit
######################################
# # RecursionError: maximum recursion depth exceeded
# def inf_recurs():
#     return inf_recurs()
#
# inf_recurs()


######################################
# 2. Factorial
######################################
# def factorial(n):
#     if n == 0:
#         return 1              # base case
#     return n * factorial(n-1) # recursive step w/ input modification

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result = result * i # 5! = 5 * 4 * ... * 1
#     return result

# # testcase 1
# print(factorial(5))     # 120
# print(factorial(1))     # 1
# print(factorial(0))     # 1
# print(factorial(20))    # 2432902008176640000

######################################
# 3. Recursive padding (could also be trim)
# ... left_pad("Jonas", 8) --> |___Jonas|
######################################
# def left_pad(st, length):
#     if len(st) < length:
#         return left_pad(" " + st, length)
#     return st
#
# # ... testcases
# print("|" + left_pad("Jonas", 9) + "|")
# print("|" + left_pad("XYZ", 9)+ "|")
# print("|" + left_pad("XYZ", 2)+ "|")

# Homework: create an iterative solution!

######################################
# 4. Fibonacci sequwnce generation
######################################

# def fib(n):
#     print(f"n: {n}")
#     if n <= 1: return n
#     return fib(n-1) + fib(n-2)

# output for fib(3):
# n: 3
# n: 2
# n: 1
# n: 0
# n: 1
# 2
# Why is the output 3,2,1,0,1? To understand that we need a recursion tree / call stack visualization


# memoization (vienas iš optimizacijos būdų)
# cache = {} # { 0: 0, 1: 1, 2: 1, ... , }
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

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
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
# for i in range(0, 1_000_000):
#     # print("AAAAAAAAAAAA" + str(i))
#     l.append("AAAAAAAAAAAA" + str(i))
#
# t1 = time.time()
# print(t1 - t0)

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
#     l.append(fib(i)) #n
#
# t11 = time.time()
# print('pirmas fib: ', t11 - t00)

######################################################################
# import time
# cache = {}
# # n = 360000 * 2
# n = 36000
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

# # Simple fib()
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)
#
# if __name__ == '__main__':
#     # pip install memory-profiler
#     from memory_profiler import memory_usage
#     mem_usage = memory_usage((fib, [20])) # same as fib(20)
#     print('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
#     print('Maximum memory usage: %s' % max(mem_usage))

# Memoized fib()
import time
cache = {}
def fib(n):
    res = 0
    if n in cache:
        return cache[n]
    elif n <= 1:
        res = n
    elif n > 1:
        res = fib(n - 1) + fib(n - 2)
    cache[n] = res
    time.sleep(0.01)
    return res

# fib(100)

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(3000)
    from memory_profiler import memory_usage
    mem_usage = memory_usage((fib, [1000]))
    print('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
    print('Maximum memory usage: %s' % max(mem_usage))



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