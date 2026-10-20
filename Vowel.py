word = input("Enter word: ")
counter = 0
for char in word:
    if char in 'aeiou':
        counter += 1
print (counter)
