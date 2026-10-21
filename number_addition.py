number_addition = input("Enter number: ")
number =int (number_addition)

if number < 0:
    number = -number

while number >= 10:
    sum_of_number = 0
    
    while number > 0:
            last_digit = number % 10  
            sum_of_number = sum_of_number + last_digit
            number = number // 10     
        
    number = sum_of_number
        
print(number)
    
    



