def show_phone_book():
    while True:
        phone_book_text = """--- Phone book ---
1. Search
2. Service Nos
3. Add name
4. Erase
5. Edit
6. Copy
7. Assign tone
8. Send b card
9. Options
10. Speed dials
11. Voice tags
0. Back to Main Menu"""
        print(phone_book_text)
        
        choice = input("select an option: ")
        
        # Valid list of strings for phone book options
        valid_choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        
        if choice not in valid_choices:
            print("Invalid choice\n")
            continue  # Restarts the phone book loop
            
        match int(choice):
            case 1:
                print("Search\n")
            case 2:
                print("Service Nos.\n")
            case 3:
                print("Add name.\n")
            case 4:
                print("Erase\n")
            case 5:
                print("Edit\n")
            case 6:
                print("Copy\n")
            case 7:
                print("Assign tone\n")
            case 8:
                print("Send b card\n")
            case 9:
                # Embedded Options Loop using def-compatible if/continue logic
                while True:
                    options_text = """--- Options ---
1. Memory in use
2. Type of view
3. Memory status
0. Back"""
                    print(options_text)
                    
                    options_choice = input("select an option: ")
                    
                    if options_choice not in ["0", "1", "2", "3"]:
                        print("Invalid choice\n")
                        continue  # Restarts the sub-options loop
                        
                    match int(options_choice):
                        case 1:
                            print("Memory in use\n")
                        case 2:
                            print("Type of view\n")
                        case 3:
                            print("Memory status\n")
                        case 0:
                            break
            case 10:
                print("Speed dials\n")
            case 11:
                print("Voice tags\n")
            case 0:
                break
