
students = [('Alice', 78), 
                    ('Bob', 45), 
                    ('Charlie', 90), 
                    ('Diana', 62), 
                    ('Kent', 30) 
    ]

passed_mark = 50

for count in students:
    name, score = count
    if score >= 60:
        print(name, score)
    elif score == passed_mark:
        print(name, score)
        
        
