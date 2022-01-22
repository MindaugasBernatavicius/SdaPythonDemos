# 0. Serialization
# import pickle
#
# data = {
#     'a': [1, 2.0, 3, 4 + 6j],
#     'b': ("Alice has a cat", "Python programming is great"),
#     'c': [False, True, False]
# }
#
# # .pkl (Python2)
# # .pickle (Python3)
# with open('data.pickle', 'wb') as f:
#     pickle.dump(data, f)

# 1. Deserialization
# import pickle
#
# with open('data.pickle', 'rb') as f:
#     data = pickle.load(f)
#
# print(data)


# 2. CSV
# # ... reading from
# # import csv
# # with open("employees.csv") as in_file:
# #     reader = csv.reader(in_file, delimiter=";")
# #     for row in reader:
# #         print(row)
# #         # print(row[0].strip("'").split(';')) # if each line is surounded by qoutes, we need to remove them
#
# # ... writing to csv
# import csv
# # ... the open call might add an additional newline,
# # ... we can turn it off like this: https://stackoverflow.com/a/3191811/1964707
# with open("employees.csv", 'a', newline='') as out_file:
#     writer = csv.writer(out_file, delimiter=";")
#     writer.writerow(["Anna Dylan", 250])
#

# 3. JSON
# import json
#
# with open("example.json") as in_file:
#     data = json.load(in_file)
#
# # ... from this point we are working with standard python objects
# print(data)
# print(type(data))
# print(data[0])
# print(data[0]['name'])
#
# # ... writing the same data
# with open("students.json", 'w') as out_file:
#     json.dump(data, out_file, indent=2)


# Homework / exercises:
# 1. You have a list of employess in JSON format saved to a file: employees.json:
# [
#   {
#     "name": "Jonas",
#     "salary": 500,
#     "no_children": 3,
#     "children_names": ["Arminas", "Kainas", "Abelis"]
#   },{
#     "name": "Petras",
#     "salary": 900,
#     "no_children": 2
#     "children_names": ["Jonukas", "Grytute"]
#   }
# ]
# ... write a script that would read the file and allow 2 operations: add_child(name), remove_child(name).
# ... Assume that all child names are known al the time (no_children == len(children_names) - keep them synchronized)
# ... Additional features (implement if you want): change salary, increase salary by some percentage, add employees, etc.

# 2. Create a simple script that will conver all csv files in a directory to json files (in the same or other directory).
#
# """
# {
# 	"employees": [{
# 			"name": "Jonas"
# 		},
# 		{
# 			"name": "Petras"
# 		}
# 	]
# }
# """



# 3. Student homework
# ... console scripts can be made very complex
# ... one of my clients created a calculator game to
# ... help his son learn arithmetic
i = 7
j = 5
while True:
    inp = input(f"What is the sum of numbers: {i} + {j}?\n")
    if int(inp) == 12:
        break