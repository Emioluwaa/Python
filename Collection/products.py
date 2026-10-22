products = [
    ("Laptop", 1200),
    ("Mouse", 25),
    ("Keyboard", 45),
    ("Monitor", 300),
    ("USB Cable", 10),
]


def is_expensive(item):
  return item[1] > 100


expensive_products = list(filter(is_expensive, products))
total_price = sum(item[1] for item in products)

for name, price in expensive_products:
  print(f"Product: {name} - Price: {price}")

print(f"\n{total_price}")
