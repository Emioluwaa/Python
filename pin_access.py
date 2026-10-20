
secret_pin = "1234"

for index in range(3):
    pin = input("ENTER PIN: ")
    if (pin != secret_pin):
        print("Incorrect PIN")
        continue
    else:
        print("Access Granted!")
        break
