def length(word):

      if len(word) >= 2:
    
          return word[:2] + word[-2:]
      
      return '""' 

print (length('mississippi'))
print (length('on'))
print (length(''))
