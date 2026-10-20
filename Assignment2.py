#driving_distance = float(input("Enter the Driving Distance: "))
#miles = float(input("Enter the Miles per Gallon: "))
#price = float(input("Enter the Price per Gallon: "))

#total = driving_distance / miles + price

#print(total)

#number = int(input("Enter number: "))

#if number % 2 == 0:
  # print("It is an even number")

#else:
 #  print("It is an odd number")

#velocity = float(input("Enter speed: "))
#acceleration = float(input("Enter acceleration: "))

#length = (velocity ** 2) / (2 * acceleration)

#print(length)

word = str(input("Enter a word: "))

length = len(word)

if length < 5:
    print("Short String")
elif length > 5 and len(word) < 10: 
    print("Medium String")
else:
    print("Long String")

word = str(input("Enter a word: "))

#first_character = word[0]
#if first_character.isupper():
 #       print("first letter is uppercase")

#else:
 #       print("first letter is lowercase")


word = str(input("Enter a word: "))

#first_character = word[0]
#last_character = word[-1]

#if first_character == last_character:
 #       print("It is palinrome")
#else:
 #       print("It is not palindrome")

name = str(input("Enter a word: "))

#if len(name) > 2 and len(name) < 5:
 #       print("Hi ", name)
#else:
#        print("Hello ", name)

character = input("Enter a character: ")

number = character.isdigit()
letter = character.isalpha()

if character.isdigit():
            print("it is a Digit")
elif character.isalpha():
            print("it is a letter")
else:
 #j           print("it is a symbol")
