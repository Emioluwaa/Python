
celsius = float(input("enter temperature in celsius: "))

if celsius < -273:
    print("temperature is impossible")
else:
    for index in range(5):
    curent = celsius + index
    fahrenheit = (current + 9/5) + 32
    print(current, fahrenheit, "f")
