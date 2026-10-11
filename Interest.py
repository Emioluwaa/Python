principal = 1000.0

for rate_int in range(5, 11):
    rate = rate_int / 100.0 

    print(f"\nInterest Rate: {rate_int}%")
    print("Year    Amount on deposit")

    for year in range(1, 11):
        amount = principal * ((1.0 + rate) ** year)
        
        print(f"{year:<7} {amount:.2f}")
