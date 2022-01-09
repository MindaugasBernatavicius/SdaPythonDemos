# 0. Simple profiling
# import time as t
# t1 = t.time()
#
# for i in range(0, 10):
#     t.sleep(0.1)
#
# t2 = t.time()
# print(f"Time taken: {t2-t1}")

# 1. Simple profiling is unstable
# ... affected by other programs
# ... that execute at the same time
# ... one way to minimize the effect
# ... is to run many experiments and
# ... calculate their average
# import time as t
#
# experiments = 10
# times_measured = []
# for experiment in range(0, experiments):
#     t1 = t.time()
#     for i in range(0, 10):
#         t.sleep(0.01)
#     t2 = t.time()
#     times_measured.append(t2-t1)
#
# print(f"Avg. time taken: {sum(times_measured) / len(times_measured)}")

# 3. Microbenchmarking/benchmarking with timeit
# from timeit import timeit as tmt
# iterations = 10
# t = tmt('for i in range(0, 10): time.sleep(0.01)', number=iterations)
# print(f'Total time: {t}, average time: {t/iterations}')
# # Total time: 1.56, average time: 0.156 -- Avg. time taken: 0.156


import timeit

# ... functions are not called automatically
# code = '''
# def func():
#     return [sqrt(x) for x in range(100)]
# '''

# ... you need to call it!
# code = '''
# def func():
#     return [sqrt(x) for x in range(100)]
#
# func()
# '''

# # ... however it is best to just run the smallest
# # ... piece of code that is the slowest / or that we are interested in
# code = '''[sqrt(x) for x in range(100)]'''
# print(timeit.timeit(stmt=code, setup="from math import sqrt", number=100_000))
#
# print(timeit.timeit('"-".join(str(n) for n in range(100) )', number=10000))


# 4. Benchmarking linear and binary search
setup = '''
import linear_search, binary_search
import random
'''

linear_search_code = '''
lst = sorted([random.randint(0, 1000000) for _ in range(1000)])
to_find = random.randint(0, 1000000)
result = linear_search(lst, to_find)
'''

binary_search_code = '''
lst = sorted([random.randint(0, 1000000) for _ in range(1000)])
to_find = random.randint(0, 1000000)
result = binary_search(lst, to_find)
'''

print(timeit.timeit(stmt=linear_search_code, setup=setup, number=1000))
print(timeit.timeit(stmt=binary_search_code, setup=setup, number=1000))