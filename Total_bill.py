
total_bill = 0.0
product_counter = 0

name = input('Enter your name: ')

while True:
    product_name = input('Enter product name: ')
    quantity = float(input(f'Enter quantity of {product_name}: '))
    price = float(input(f'Enter price of {product_name}: '))
    
    
    item_total = price * quantity
    total_bill += item_total
    product_counter += 1
    
    another_product = input("Do you want to add another product? (yes/no): ").lower()
    
   
    if another_product != 'yes':
        break



print(f"Total items purchased: {product_counter}")
print(f"Total Bill: {total_bill:.2f}")

