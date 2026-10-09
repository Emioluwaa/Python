def add_string(text):

    if len(text) > 2:
        
        return text + 'ing'
        
    elif text.endswith('ing'):
        return text + 'ly'
        
    else:
        return text 
        
print (add_string('boy'))
print (add_string('boying'))
print (add_string('on'))

