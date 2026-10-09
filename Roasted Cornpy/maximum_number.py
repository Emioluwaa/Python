def maximum_numbers(numbers):

   highest = numbers[0]
     
   for count in numbers:
       if count > highest:
            lowest = count
            
   return highest
    
    
numbers = [8,4,9,2,5,7,3]

my_numbers = maximum_numbers(numbers)
  
print(my_numbers)
