number = input("Enter number: ")
largest = -1
for counter in str(number):
    index = int(counter)
    if index > largest:
        largest = index
print(largest)
    
