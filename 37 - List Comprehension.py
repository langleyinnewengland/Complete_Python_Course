#double the numbers in the list
numbers = [0, 1, 2, 3, 4]
doubled_numbers = []

for num in numbers:
    doubled_numbers.append(num * 2)

print(doubled_numbers)

#this does the same thing as above
numbers = [0, 1, 2, 3, 4]
doubled_numbers = [number *2 for number in numbers]
print(doubled_numbers)

numbers = [0, 1, 2, 3, 4]  # list(range(5)) is better
doubled_numbers = [num * 2 for num in numbers]
# [num * 2 for num in range(5)] would be even better.


names = ["Rolf", "Bob", "Jen"]
