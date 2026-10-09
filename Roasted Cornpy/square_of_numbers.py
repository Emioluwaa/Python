def square_of_numbers(numbers):
    squared_number = []
    
    for count in numbers:
        squared_number.append(count**2)
        
    return squared_number
    
index = [2, 3, 4, 5, 7]
result = square_of_numbers(index)

print(result)
