import time

# ############## 1
mystr = "Mindaugas"

t0 = time.time()
for i in range(0, 10000):
    finalstr = ""
    for i in range(len(mystr)-1, -1, -1):
        finalstr += mystr[i]
t1 = time.time()

print(t1-t0)
print(finalstr)

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