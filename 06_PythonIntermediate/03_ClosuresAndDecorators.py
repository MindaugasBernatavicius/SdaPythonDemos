# 0. Functional programing features

# 0.1. list comprehension
# lst = [x for x in range(0, 10)]

# 0.2. functions as first class citizens
# def formatter(func, str):
#     str = "_" + str + "_"
#     func(str)
#
# def printer(param = ""):
#     print(param)
#
# formatter(printer, "ddd")
#
#
# def get_vowels(variable):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if (variable in letters):
#         return True
#
# def get_all_consonants(variable):
#     letters = ['a', 'e', 'i', 'o', 'u', ' ']
#     if (variable not in letters):
#         return True
#
# sequence = "My name is Jonas"
# print("Original: " + sequence)
# # filter for vowels - return vowels that are in the sentence
# filtered = filter(get_vowels, sequence)
# print("Filtered: " + str(list(filtered)))
#
# filtered = filter(get_all_consonants, sequence)
# print("Filtered: " + str(list(filtered)))

# 0.2. closures
# def print_msg(msg):
#     formatted_msg = "_" + msg + "_"
#     # ...
#     # ...
#     # ... this function below is called a "closure"
#     def printer():
#         print(msg + " -> " + formatted_msg)
#     return printer
#
# p = print_msg("Mindaugas")
# p()

# 1. Minimal decorator (closures + functions as variables)
# def disable_at_night(func): # decorator definition
#     def wrapper():
#         pass
#     # return wrapper() # if we have parentheses after the function name it will be called!
#     return wrapper # return funtion reference, not the value that the funciton returns
#
# @disable_at_night # decorator invocation
# def say_something():
#     print("Hello world")
#
# say_something()

# 2. Adding some logic
# from datetime import datetime
#
# def disable_at_night(func):
#     # a decorator that only calls a decorated function during the day
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             func()
#     return wrapper
#
# @disable_at_night # decorator invocation
# def say_something():
#     print("Hello world")
#
# say_something()

# 3. Simple decorator for primitive logging
# def log(func):
#     def wrapper():
#         print("----")
#         func()
#         print("----")
#     return wrapper
#
# @log
# def my_function():
#     print("Hello world")
#
# @log
# def my_function2():
#     print("Hello world")
#
# my_function()

# 4. Decorator with arguments
from datetime import datetime

# ... triple nesting [[]], if inside an if - nested if
def run_only_between(from_=7, to_=22):
    def dec(func):
        def wrapper():
            if from_ <= datetime.now().hour < to_:
                func()
        return wrapper
    return dec

@run_only_between(10, 15)
def say_something():
    print("Hello world")

say_something()
