def length_text(word):
    count = 0
    for character in word:
         count+=1
    return count

word = 'semicolon'
count = length_text(word)

print(count)
