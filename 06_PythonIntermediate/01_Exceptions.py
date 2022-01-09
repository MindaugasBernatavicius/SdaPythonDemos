# import time as t
# import os
#
# __location__ = os.path.realpath(
#     os.path.join(os.getcwd(), os.path.dirname(__file__)))
#
# f = open(os.path.join(__location__, 'file.txt'))
# print(f.read())
# # t.sleep(5)
# # f.close()
# t.sleep(60)


# 1. Simplest exception provocation
# print(f'{1 / 0}')                 # division by zero : ZeroDivisionError
# xyz                               # non existing variable : NameError
# l = [1, 2]; print(f'{ l[2] }')    # accessing non-existing item in list: IndexError
# d = { "n": "Jonas"}; d["x"]       # accessing non-existing item in dict: KeyError
# d = { "n": "Jonas"}; d["x]        # SyntaxError: EOL while scanning string literal


# 2. A bit more complicated example
# a = 3
# b = [1, 0, 2]
# for elem in b:
#     res = a / elem
#     print(f"Result is: {res}")

# 3. Multiple functions with exception
# def divide(p1, p2):
#     return p1 / p2
#
# def main():
#     print(f'{ divide(1, 0) }')
#
# if __name__ == '__main__':
#     main()

# 4. Built-in exceptions
# def divide(p1, p2):
#     assert p2 != 0      # AssertionError
#     assert p1 > 5000
#     return p1 / p2
#
# print(f'{ divide(5, 0) }')

# 5. Handling exceptions: try-except
# try:
#     print(f'{1 / 0}')
#     print(f'1: Will this code execute?') # ... this line will not be executed if an exception happens 1 line above
# except: # ... except block will only be executed if an exception happens
#     print(f'Do not divide by 0')
#
# print(f'2: Will this code execute?')

# ... check the documentation if an exception is thrown from this method
# import os
# os.wait()

# 6. I/O boundary and finally block
# import time as t
#
# try:
#     f = open('file.txt')           # FileNotFoundError: [Errno 2] No such file or directory: 'file2.txt'
#     file_str = f.read()
#     i1, i2 = file_str.split('\n')
#     print(f'{int(i1) / int(i2)}')  # ZeroDivisionError
# except FileNotFoundError:
#     print(f'File handling error')
# except (ZeroDivisionError, ValueError):
#     print(f'Problem in file data')
# except: # catch-all
#     print(f'General error occurred')
# finally:
#     print(f'Inside finally!')
#     f.close()
#
# t.sleep(20)
#
# print(f'Will this code execute?')


# 7. Raise - how to protect our function
# ... so that when empty string is passed,
# ... the whole application is not terminated
# def get_strings_first_letter(stringy):
#     # assert len(stringy) != 0 # you could use this as well
#     if len(stringy) == 0:
#         raise ValueError("Can't process empty strings")
#     elif len(stringy) > 10:
#         raise Exception("String is too long!")
#     return stringy[0]
#
# try:
#     print(f'{get_strings_first_letter("")}')
# except ValueError as e:
#     print(e.__class__.__name__)
#     print(e)


# 8. Custom exception types
# class StringLengthException(Exception):
#     def __init__(self):
#         message = "Some default error message"
#         super().__init__(message)
#
# def get_strings_first_letter(stringy):
#     if len(stringy) == 0:
#         raise StringLengthException
#     return stringy[0]
#
# try:
#     print(f'{get_strings_first_letter("")}')
# except StringLengthException as e:
#     print(f'{ e.__class__.__name__ }: { e }')


# 9. Exception hierarchy

# 10. Multiple nested exceptions


# Homework (student solutions)
import csv
from tabulate import tabulate

while True:
    f_input = input('Enter csv file name: ')
    f_name = f_input + '.csv'
    try:
        with open(f_name, 'r') as f:
            reader = csv.reader(f, delimiter=';', quotechar='"')
            table = []
            mysum, count = 0, 0
            for line in reader:
                mysum += int(line[1])
                count += 1
                table.append(line)
            print(tabulate(table, headers='firstrow', tablefmt='github', stralign='center', numalign='center'))
            # print("{:<15} {:<15} {:<10} {:<8}".format(*line))
            print("{:>20}".format("Avg: " + str(mysum / count)))
            break
    except FileNotFoundError:
        print("File not found!")