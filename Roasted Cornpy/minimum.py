def minimum_numbers(numbers):

    lowest = numbers[0]
     
    for count in numbers:
       if count < lowest:
            lowest = count
            
    return lowest
    
    
numbers = [8,4,9,2,5,7,3]

my_numbers = minimum_numbers(numbers)
  
print(my_numbers)
