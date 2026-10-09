def length_text(word):
    count = 0
    for character in word:
         count+=1
    return count

word = 'semicolon'
count = length_text(word)
 

def length(word):

      if len(word) >= 2:
    
          return word[:2] + word[-2:]
      
      return '""' 

def add_string(text):

    if len(text) > 2:
        
        return text + 'ing'
        
    elif text.endswith('ing'):
        return text + 'ly'
        
    else:
        return text 

def finding_max(words):
    longest = max(words, key = len)
    return longest, len(longest)


word = ('welcome', 'out', 'weather', 'mobile', 'breakfast', 'journey')

def maximum_numbers(numbers):

   highest = numbers[0]
     
   for count in numbers:
       if count > highest:
            lowest = count
            
   return highest
    
    
numbers = [8,4,9,2,5,7,3]

my_numbers = maximum_numbers(numbers)
  

      























print(count)
print (length('mississippi'))
print (length('on'))
print (length(''))
print (add_string('boy'))
print (add_string('boying'))
print (add_string('on'))
print(finding_max(word))
print(my_numbers)


