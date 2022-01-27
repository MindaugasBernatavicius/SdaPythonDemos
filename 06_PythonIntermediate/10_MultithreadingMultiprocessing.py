# # 0. Basic threading
# from threading import Thread
# import time as t
#
# def iterative_print(iter):
#     """
#     A function prints the elements of a list
#     """
#     # for item in iter:
#     #     t.sleep(0.01)
#     #     print(item)
#
#     for i in range(0,50):
#         t.sleep(0.1)
#         print(iter)
#
# # creating threads
# t1 = Thread(target=iterative_print, args=(range(5),))  # writing out successive natural numbers
# t2 = Thread(target=iterative_print, args=("Python",))  # writing the characters of the string
#
# # starting threads
# # t1.start()
# t2.start()
# # print("Done!")
#
# # waiting until both threads have finished executing before executing further code
# # t1.join()
# print(t2.join()) # None
# print("Done!")


# # 1. Threads as objects
# import threading
# import time
#
# class ThreadWithReturnValue(threading.Thread):
#     def __init__(self, target, args=(), kwargs=None):
#         if kwargs is None:
#             kwargs = {}
#         self.target = target
#         print(type(args))
#         self.args = args
#         self.kwargs = kwargs
#         super().__init__()
#
#     def run(self):
#         self.result = self.target(*self.args, **self.kwargs)
#
#     def join(self, timeout=None):
#         super().join(timeout)
#         return self.result
#
#
# def print_cube(num):
#     # A function that returns the third power of a number given as a parameter
#     time.sleep(2)
#     print(f"Cube: {num * num * num}")
#
# def print_square(num):
#     # A function that returns the square of the number given as a parameter
#     time.sleep(2)
#     return num * num
#
#
# # creating threads
# t1 = ThreadWithReturnValue(target=print_square, args=(10,))
# t2 = threading.Thread(target=print_cube, args=(10,))
#
# # starting threads
# t1.start()
# t2.start()
#
# # waiting until both threads have finished executing before executing further code
# print(f">>> { t1.join() }")
# t2.join()
#
# print("Done!")



# 2. Time comparison
# import requests
# print(requests.get('https://www.delfi.lt').text)

# import requests
# import timeit
#
# def crawl(url, dest):
#     try:
#         result = requests.get(url).text
#         with open(dest, "a") as f:
#             f.write(result)
#     except requests.exceptions.RequestException:
#         print("Error with URL check!")
#
# def wo_threading_func(urls):
#     for url in urls:
#         crawl(url, "without_threads.txt")
#
# def with_threading_func(urls):
#     import threading
#     threads = []
#     for url in urls:
#         th = threading.Thread(target=crawl, args=(url, "with_threads.txt"))
#         th.start()
#         threads.append(th)
#     for th in threads:
#         th.join()
#
# if __name__ == "__main__":
#     wo_threading = "wo_threading_func(urls)"
#     with_threading = "with_threading_func(urls)"
#
#     setup = '''
# from __main__ import wo_threading_func, with_threading_func
#
# urls = [
#     "https://jsonplaceholder.typicode.com/comments/1",
#     "https://jsonplaceholder.typicode.com/comments/2",
#     "https://jsonplaceholder.typicode.com/comments/3"
# ]
#     '''
#     print("Without threads:", timeit.timeit(stmt=wo_threading, setup=setup, number=100))
#     print("With threads:", timeit.timeit(stmt=with_threading, setup=setup, number=100))




# # ... CPU bound workload (little to no I/O) - this is in contrast to I/O bound workload (above)
# import timeit
#
# def count(_from, _to):
#     while _from >= _to:
#         _from -= 1
#
# def wo_threading_func():
#     count(400000, 0)
#
# def with_threading_func():
#     import threading
#
#     t1 = threading.Thread(target=count, args=(400000, 200000))
#     t2 = threading.Thread(target=count, args=(200000, 0))
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
# if __name__ == "__main__":
#     wo_threading = "wo_threading_func()"
#     with_threading = "with_threading_func()"
#     setup = "from __main__ import wo_threading_func, with_threading_func"
#
#     print("Without threads:", timeit.timeit(stmt=wo_threading, setup=setup, number=100))
#     print("With threads:", timeit.timeit(stmt=with_threading, setup=setup, number=100))


# 3. Multiprocessing
import timeit
import multiprocessing
import threading

def count(_from, _to):
    while _from >= _to:
        _from -= 1

def wo_threading_func():
    count(400000, 0)

def with_threading_func():
    t1 = threading.Thread(target=count, args=(400000, 200000))
    t2 = threading.Thread(target=count, args=(200000, 0))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

def with_multiprocessing_func():
    p1 = multiprocessing.Process(target=count, args=(400000, 200000))
    p2 = multiprocessing.Process(target=count, args=(200000, 0))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    wo_threading = "wo_threading_func()"
    with_threading = "with_threading_func()"
    with_multiprocessing = "with_multiprocessing_func()"
    setup = "from __main__ import wo_threading_func, with_threading_func, with_multiprocessing_func"

    print("Without threads:", timeit.timeit(stmt=wo_threading, setup=setup, number=100))
    print("With threads:", timeit.timeit(stmt=with_threading, setup=setup, number=100))
    print("With sub-processes:", timeit.timeit(stmt=with_multiprocessing, setup=setup, number=100))
