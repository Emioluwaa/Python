def main():
    while True:

        main_menu = """


1. Phonebook
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Music
9. Games
10. Calculator
11. Reminders
12. Clock
13. Profiles
14. Services
15. SIM services
0. Shutting down......"""

        print(main_menu)

        main_menu_choice = input("select an option: ")

        valid_choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]

        if main_menu_choice not in valid_choices:
            print("Please enter a valid number.\n")
            continue

        match int(main_menu_choice):
            case 1:
                show_phone_book()
            case 2:
                show_messages()
            case 3:
                print("Chat\n")
            case 4:
                show_call_register()
            case 5:
                show_tones()
            case 6:
                show_settings()
            case 7:
                print("Call divert\n")
            case 8:
                show_music()
            case 9:
                print("Games\n")
            case 10:
                print("Calculator\n")
            case 11:
                print("Reminders\n")
            case 12:
                show_clock()
            case 13:
                print("Profiles\n")
            case 14:
                print("Services\n")
            case 15:
                print("SIM services\n")
            case 0:
                print("Shutting down......")
                break


def show_phone_book():
    while True:
        phone_book_text = """ Phone book 
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
99. Back
0. Main Menu"""

        print(phone_book_text)

        choice = input("select an option: ")

        valid_choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "99"]
        if choice not in valid_choices:
            print("Invalid choice\n")
            continue

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
                while True:
                    options_text = """--- Options ---
1. Memory in use
2. Type of view
3. Memory status
99. Back
0. Main Menu"""
                    print(options_text)

                    options_choice = input("select an option: ")

                    if options_choice not in ["0", "1", "2", "3", "99"]:
                        print("Invalid choice\n")
                        continue

                    match int(options_choice):
                        case 1:
                            print("Memory in use\n")
                        case 2:
                            print("Type of view\n")
                        case 3:
                            print("Memory status\n")
                        case 99:
                            break
                        case 0:
                            return True
            case 10:
                print("Speed dials\n")
            case 11:
                print("Voice tags\n")
            case 99:
                return False
            case 0:
                return True


def show_messages():
    while True:
        messages_text = """--- Messages ---
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number
10. Service command editor
99. Back
0. Main Menu"""
        print(messages_text)

        choice = input("select an option: ")

        valid_choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "99"]
        if choice not in valid_choices:
            print("Invalid choice\n")
            continue

        match int(choice):
            case 1:
                print("Write messages\n")
            case 2:
                print("Inbox\n")
            case 3:
                print("Outbox\n")
            case 4:
                print("Picture messages\n")
            case 5:
                print("Templates\n")
            case 6:
                print("Smileys\n")
            case 7:
                print("Message settings\n")
            case 8:
                print("Info service\n")
            case 9:
                print("Voice mailbox number\n")
            case 10:
                print("Service command editor\n")
            case 99:
                return False
            case 0:
                return True


def show_call_duration():
    while True:
        text = """--- Show call duration ---
1. Last call duration
2. All calls duration
3. Received calls duration
4. Dialled calls duration
5. Clear timers
99. Back
0. Main Menu"""
        print(text)

        choice = input("select an option: ")

        valid_choices = ["0", "1", "2", "3", "4", "5", "99"]
        if choice not in valid_choices:
            print("Invalid choice\n")
            continue

        match int(choice):
            case 1:
                print("Last call duration\n")
            case 2:
                print("All calls duration\n")
            case 3:
                print("Received calls duration\n")
            case 4:
                print("Dialled calls duration\n")
            case 5:
                print("Clear timers\n")
            case 99:
                return False
            case 0:
                return True


def show_call_costs():
    while True:
        text = """--- Show call costs ---
1. Last call cost
2. All calls cost
3. Clear counters
99. Back
0. Main Menu"""
        print(text)

        choice = input("select an option: ")

        valid_choices = ["0", "1", "2", "3", "99"]
        if choice not in valid_choices:
            print("Invalid choice\n")
            continue

        match int(choice):
            case 1:
                print("Last call cost\n")
            case 2:
                print("All calls cost\n")
            case 3:
                print("Clear counters\n")
            case 99:
                return False
            case 0:
                return True


def show_call_cost_settings():
    while True:
        text = """--- Call cost settings ---
1. Call cost limit
2. Show costs in
99. Back
0. Main Menu"""
        print(text)

        choice = input("select an option: ")

        valid_choices = ["0", "1", "2", "99"]
        if choice not in valid_choices:
            print("Invalid choice\n")
            continue

        match int(choice):
            case 1:
                print("Call cost limit\n")
            case 2:
                print("Show costs in\n")
            case 99:
                return False
            case 0:
                return True


def show_call_register():
    while True:
        text = """--- Call register ---
1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
99. Back
0. Main Menu"""
        print(text)

        choice = input("select an option: ")

        valid_choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "99"]
        if choice not in valid_choices:
            print("Invalid choice\n")
            continue

        match int(choice):
            case 1:
                print("Missed calls\n")
            case 2:
                print("Received calls\n")
            case 3:
                print("Dialled numbers\n")
            case 4:
                print("Erase recent call lists\n")
            case 5:
                if show_call_duration():
                    return True
            case 6:
                if show_call_costs():
                    return True
            case 7:
                if show_call_cost_settings():
                    return True
            case 8:
                print("Prepaid credit\n")
            case 99:
                return False
            case 0:
                return True


def show_tones():
    while True:
        text = """--- Tones ---
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Message alert tone
5. Keypad tones
6. Warning tones
7. Vibrating alert
8. Screen saver
99. Back
0. Main Menu"""
        print(text)

        choice = input("select an option: ")

        valid_choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "99"]
        if choice not in valid_choices:
            print("Invalid choice\n")
            continue

        match int(choice):
            case 1:
                print("Ringing tone\n")
            case 2:
                print("Ringing volume\n")
            case 3:
                print("Incoming call alert\n")
            case 4:
                print("Message alert tone\n")
            case 5:
                print("Keypad tones\n")
            case 6:
                print("Warning tones\n")
            case 7:
                print("Vibrating alert\n")
            case 8:
                print("Screen saver\n")
            case 99:
                return False
            case 0:
                return True


def show_call_settings():
    while True:
        text = """--- Call settings ---
1. Automatic redial
2. Speed dialling
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic answer
99. Back
0. Main Menu"""
        print(text)

        choice = input("select an option: ")

        valid_choices = ["0", "1", "2", "3", "4", "5", "6", "99"]
        if choice not in valid_choices:
            print("Invalid choice\n")
            continue

        match int(choice):
            case 1:
                print("Automatic redial\n")
            case 2:
                print("Speed dialling\n")
            case 3:
                print("Call waiting options\n")
            case 4:
                print("Own number sending\n")
            case 5:
                print("Phone line in use\n")
            case 6:
                print("Automatic answer\n")
            case 99:
                return False
            case 0:
                return True


def show_phone_settings():
    while True:
        text = """--- Phone settings ---
1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Confirm SIM service actions
99. Back
0. Main Menu"""
        print(text)

        choice = input("select an option: ")

        valid_choices = ["0", "1", "2", "3", "4", "5", "99"]
        if choice not in valid_choices:
            print("Invalid choice\n")
            continue

        match int(choice):
            case 1:
                print("Language\n")
            case 2:
                print("Cell info display\n")
            case 3:
                print("Welcome note\n")
            case 4:
                print("Network selection\n")
            case 5:
                print("Confirm SIM service actions\n")
            case 99:
                return False
            case 0:
                return True


def show_security_settings():
    while True:
        text = """--- Security settings ---
1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Security level
6. Change access codes
99. Back
0. Main Menu"""
        print(text)

        choice = input("select an option: ")

        valid_choices = ["0", "1", "2", "3", "4", "5", "6", "99"]
        if choice not in valid_choices:
            print("Invalid choice\n")
            continue

        match int(choice):
            case 1:
                print("PIN code request\n")
            case 2:
                print("Call barring service\n")
            case 3:
                print("Fixed dialling\n")
            case 4:
                print("Closed user group\n")
            case 5:
                print("Security level\n")
            case 6:
                print("Change access codes\n")
            case 99:
                return False
            case 0:
                return True


def show_settings():
    while True:
        text = """--- Settings ---
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
5. Back to Main Menu
99. Back
0. Main Menu"""
        print(text)

        choice = input("select an option: ")

        valid_choices = ["0", "1", "2", "3", "4", "5", "99"]

        if choice not in valid_choices:
            print("Invalid choice\n")
            continue

        match int(choice):
            case 1:
                if show_call_settings():
                    return True
            case 2:
                if show_phone_settings():
                    return True
            case 3:
                if show_security_settings():
                    return True
            case 4:
                print("Restore factory settings\n")
            case 5:
                return False
            case 99:
                return False
            case 0:
                return True


def show_music():
    while True:
        text = """--- Music ---
1. Music player
2. Radio
3. Recorder
4. Track list
5. Back to Main Menu
99. Back
0. Main Menu"""

        print(text)

        choice = input("select an option: ")

        valid_choices = ["0", "1", "2", "3", "4", "5", "99"]

        if choice not in valid_choices:
            print("Invalid choice\n")
            continue

        match int(choice):
            case 1:
                print("Music player\n")
            case 2:
                print("Radio\n")
            case 3:
                print("Recorder\n")
            case 4:
                print("Track list\n")
            case 5:
                return False
            case 99:
                return False
            case 0:
                return True


def show_clock():
    while True:
        text = """--- Clock ---
1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
7. Back to Main Menu
99. Back
0. Main Menu"""

        print(text)

        choice = input("select an option: ")

        valid_choices = ["0", "1", "2", "3", "4", "5", "6", "7", "99"]

        if choice not in valid_choices:
            print("Invalid choice\n")
            continue

        match int(choice):
            case 1:
                print("Alarm clock\n")
            case 2:
                print("Clock settings\n")
            case 3:
                print("Date setting\n")
            case 4:
                print("Stopwatch\n")
            case 5:
                print("Countdown timer\n")
            case 6:
                print("Auto update of date and time\n")
            case 7:
                return False
            case 99:
                return False
            case 0:
                return True


if __name__ == "__main__":
    main()
