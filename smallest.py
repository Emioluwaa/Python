number = input("Enter number: ")
smallest = 9
for counter in str(number):
    index = int(counter)
    if index < smallest:
        smallest = index
print(smallest)
    
