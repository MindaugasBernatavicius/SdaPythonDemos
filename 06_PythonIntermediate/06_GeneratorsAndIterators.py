# 0. Iterators

# ... generate primes with lists
# from math import sqrt
# import psutil
#
# def is_prime(n):
#     for i in range(2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# def get_n_primes(n):
#     primes = []
#     i = 2
#     while len(primes) != n:
#         if is_prime(i):
#             primes.append(i)
#         i += 1
#     return primes
#
# import time as t
# m0 = psutil.Process().memory_info().rss / (1024 * 1024)
# t0 = t.time()
#
# lst = get_n_primes(10000)
# for elem in lst:
#     # print(elem)       # I/O operation should not be benchmarked
#     elem = elem + 1
#
# print(f"Time: {t.time() - t0}")
# print(f"Memory: {psutil.Process().memory_info().rss / (1024 * 1024) - m0}")

# ... generate primes with iterator
# from math import sqrt
#
# def is_prime(n):
#     for i in range(2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# class PrimeIterator:
#     # Iterator that allows you to iterate over n primes
#     def __init__(self, n):
#         self.n = n
#         self.generated_numbers = 0
#         self.number = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.number += 1
#         if self.generated_numbers >= self.n:
#             raise StopIteration
#         elif is_prime(self.number):
#             self.generated_numbers += 1
#             return self.number
#         return self.__next__()
#
#
# import time as t
# import psutil
# m0 = psutil.Process().memory_info().rss / (1024 * 1024)
# t0 = t.time()
#
# iter = PrimeIterator(10000)
# for elem in iter:
#     # print(elem)      # I/O operation should not be benchmarked
#     elem = elem + 1
#
# print(f"Time: {t.time() - t0}")
# print(f"Memory: {psutil.Process().memory_info().rss / (1024 * 1024) - m0}")


# 1. Generators
def my_gen():
    for i in range(10):
        print(">>>")
        yield i

g = my_gen()
print(next(g))
print(next(g))
print(next(g))

print(list(my_gen()))


def gen_even_numbers(to=10):
    for i in range(to):
        if i % 2 == 0:
            yield i

geven = gen_even_numbers()
print(next(geven))
print(next(geven))
print(next(geven))
print(list(gen_even_numbers()))


def inf_gen():
    val = 0
    while True:
        yield val
        val += 1

ig = inf_gen()
# print(next(ig))
# print(next(ig))
# print(next(ig))
# print(next(ig))

# print(list(inf_gen())) # can't do that!