def sum_square_of_numbers(numbers):
    total_sum = 0
    
    for count in numbers:
        total_sum += count**2
        
    return total_sum
    
numbers = [2, 3, 4, 5, 7]

result = sum_square_of_numbers(numbers)

print(result)
