
total = 0 
Grade_counter = 0

grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]

for grade in grades:
    total += grade 
    Grade_counter += 1
    
    average = total / Grade_counter
    print(f'Class average is {average}')
    
    
    
    
    
    
    passes = 0
    failures = 0
    
    for student in range(10):
        result = int(input('Enter result (1=pass, 2=fail): '))
        
        if result == 1:
            passes = passes + 1
    else:
        failures = failures + 1
            print('Passed:',passes)
            print('Failed:', failures):
     if passes > 8:
        print('Bonus to instructor')
