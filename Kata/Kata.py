def is_even(number):

  return number % 2 == 0
 
def is_prime(number):


  if number <= 1:
    return False
    
    
  for index in range(2, number):
        if number % index == 0:
            return False
            
  return True


def subract_two_numbers(first_number, second_number):

        return abs(first_number - second_number)

def divide_two_numbers(first_number, second_number):
    return abs(first_number / second_number)    

def factor_of(number):
    factors = []
    for index in range(1, number + 1):
        if number % number == 0:
            factors.append(index)
    return factors


result = is_even(10)
result_two = is_prime(11)
result_three = subract_two_numbers(11, 214)
result_four = divide_two_numbers(120, 10)
result_five = factor_of(10)







print(result)
print(result_two)
print(result_three)
print(result_four)
print(result_five)
#print(result_six)
