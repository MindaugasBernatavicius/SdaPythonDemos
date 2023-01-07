#######################
# 0. Print vs. return #
#######################
# - Print and return are really different
# - Print is used to return a value of a variable to the console
# - Return is keyword that indicates the result that will passed from a function to caller of that function
# - Return is much less demanding performance vise, print is an I/O operation where the OS becomes involved
#   ... print has a much bigger performance impact than return

# name = "Mindaugas"
# print(name)
#
# def add(i: int, j: int) -> None:
#     sum_result = i + j
#     print(sum_result)
#     # return sum_result
#
#
# # res = add(5, 9)
# # print(add)
#
# add(5, 9)
#
#
# # - By default all functions even the ones that do not have a return statement return None
# def subtr(i: int, j: int) -> None:
#     sum_result = i - j
#     print(sum_result)
#
#
# def enhanced_print(val: str) -> None:
#     print(val, end="\n\n")
#
#
# print(subtr(5, 9))

# - Return ends the surrounding function immediately and gives control back to the calling context
def x():
    pass


def traverse_list(lst: list):
    filtered_items = []
    for item in lst:
        if item == "Jonas":
            return
        else:
            filtered_items.append(item)

    # ... do something with the filtered_items
    transformed_items = filtered_items
    return transformed_items


lst = ["Mindaugas", "Kukis", "Jonas", "Bukis"]
traverse_list(lst)

print(">>>")


# When to use which?
# - print only when you want to inspect a variable or produce a result for the user in console program.