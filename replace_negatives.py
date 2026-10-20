def replace_negatives(number):
    for count in range(len(number)):
        if number[count] < 0:
            number[count] = 0
    return number

print(replace_negatives([5, -9, 3, -6, 2, -11, -0, 9, -0]))



#
#def negative_number():
#    
#    count = [5, -9, 3, -6, 2, -11, 0, 9, -0]
#
#        if count <= 0:
#             count =0
#    
#    return (count) 
#
#print(negtive_number)
