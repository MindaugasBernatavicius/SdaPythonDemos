# 0. Proving that file is closed even if exception happens
# import time as t
#
# with open('file.txt', 'r') as f:
#     print(f.read())
#     raise Exception
#     print(">>>")
#     t.sleep(5)
#
# print(">>>")
# t.sleep(5)


# 1. Creating your own context manager
# class FileManager():
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         # opening and sharing of resources
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, type, value, traceback):
#         # cleaning, release of resources
#         self.file.close()
#         # pass
#
#
# with FileManager("file.txt", 'w') as f:
#     f.write("Test")
#
# import time as t
# print(">>>>")
# t.sleep(5)

# 2. Context manager order of operations
# class FileManager():
#     def __init__(self, filename, mode):
#         print('f{__init__}')
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         print('f{__enter__}')
#         # opening and sharing of resources
#         self.file = open(self.filename, self.mode)
#         return self.file # must return the object that will be used inside the with block
#         # return True
#
#     def __exit__(self, type, value, traceback):
#         print('f{__exit__}')
#         # cleaning, release of resources
#         self.file.close()
#
#
# with FileManager("file.txt", 'w') as f:
#     f.write("Test")
#     print("<<<<")
#
# print(">>>>")


# 3. Exceptions and context managers
# class FileManager():
#     def __init__(self, filename, mode):
#         print('f{__init__}')
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         print('f{__enter__}')
#         # opening and sharing of resources
#         self.file = open(self.filename, self.mode)
#         return self.file # must return the object that will be used inside the with block
#         # return True
#
#     def __exit__(self, type, value, traceback):
#         print('f{__exit__}')
#         print(type)
#         print(value)
#         # print(traceback)
#         # cleaning, release of resources
#         self.file.close()
#         # return True   # if the value of __exit__ is truthy then the exception is not propagated
#
# file_name = 'file.txt'
# try:
#     with FileManager(file_name, 'r') as f:
#         raise Exception('Mindaugas message')
#         # print(f.read())
#         # pass
# except FileNotFoundError:
#     print("File not found!")
# except Exception:
#     print("Something bad, but not specific happended")


# 4. Context manager with as a decorator (function)
from contextlib import contextmanager

@contextmanager
def file_manager(name, mode):
    print(f'{1}')
    file = open(name, mode) # Same as: __init__(name, mode)
    print(f'{2}')
    yield file              # Return the same as return from __enter__
    # Do the same as in __exit__ (after yield)
    print(f'{3}')
    file.close()
    print(f'{4}')


with file_manager('file.txt', 'r') as f:
    print(f.read())
    print(f"Something")