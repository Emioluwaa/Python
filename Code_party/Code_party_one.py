old_tuple = (1, 2, 3)
new_tuple = original_tuple[:3] + (4,)
print(new_tuple)

numbers = (1, 2, [3, 4], 5)
numbers[2][1] = 99
print(numbers)

fruit_tuple = ("apple", "banana", "cherry")
fruit_list = list(fruit_tuple)
fruit_list[len(fruit_list) :] = ["mango"]
fruit_tuple = tuple(fruit_list)
print(fruit_tuple)

number = (10, 20, 30, 40)
num_a = data[0]
num_b = data[1]
rest = data[2:]
print(a, b, rest)
