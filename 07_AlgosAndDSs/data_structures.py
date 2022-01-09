# Stack
# ... simple stack
stack_of_employees = []

# ... hiring order, should be push()
stack_of_employees.append("Mindaugas")
stack_of_employees.append("Jonas")
stack_of_employees.append("Antanas")

print(f"{stack_of_employees}")

# ... firing order (LIFO)
while len(stack_of_employees) > 0:
    print(f"{stack_of_employees.pop()}")


# ... more realistic stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()


stack_more_realistic = Stack()
stack_more_realistic.push("Petras")
stack_more_realistic.push("Kornelija")

print(f"{stack_more_realistic.peek()}")
print(f"{stack_more_realistic.pop()}")



# Queue
# ... deque
from collections import deque

dq = deque([1,2,3])
dq.append(0)

print(f"{dq}")
print(f"{dq.pop()}")
print(f"{dq.popleft()}")
print(f"{dq}")


# Heap, ref: https://www.youtube.com/watch?v=3c-p4zWx5yU
from heapq import heappop, heappush

def top_n_members(lst, n):
    heap = []
    for item in lst:
        heappush(heap, item)
        if len(heap) == n+1:
            heappop(heap)
    return heap

num_list = [1, 254, 5, 10, 11, 2, 18, 26, 12, 24]
n = 3
print(f"Max {n} items in the list: {top_n_members(num_list, n)}")

# ... compare to other solutions - sorting and looping with max()