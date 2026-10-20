guessed_number = "10"
for index in range(3):
   number = input("Enter number: ")
   if (number != guessed_number):
       print("TRY AGAIN!")
       continue
   else:
       print("CORRECT!")
       break
