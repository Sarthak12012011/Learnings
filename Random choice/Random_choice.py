import random

list = []
try:
    a = int(input("Enter the number of elements in the list: "))
except Exception:
    print("Please enter a valid integer.")

for i in range(a):
    b=input(f'Enter element: ')
    list.append(b)

print("Randomly selected element:", random.choice(list))