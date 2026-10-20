list_of_words = ["book", "pen", "jotter", "box"]

total = 0
count = 0

for word in list_of_words:
    if count % 2 == 0:
        total += word
    
    
print("Length of the list is:", count)
