



main_menu = """

List of menu functions

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
"""
print(main_menu)
main_menu_choice = int(input("select an option: "))
match(main_menu_choice):

   case 1:
        print("Phone book")

        phone_book = """

Welcome to Phone book

Press 

1.  Search
2.  Service Nos
3.  Add name
4.  Erase
5.  Edit
6.  Copy
7.  Assign tone
8.  Send b’card
9.  Options 
"""
        print(phone_book)
        phone_book_choice = int(input("select an option: "))
        match(phone_book_choice):
             case 1:
                     print("Search")
             case 2: 
                     print("Service Nos.")
             case 3: 
                     print("Add name.")
             case 4: 
                     print("Erase")
             case 5: 
                     print("Edit")
             case 6: 
                     print("Copy")
             case 7: 
                     print("Assign tone")
             case 8: 
                     print("Send b’card")
             case 9: 
                print("Options")
                options = """

Welcome to Options

Press 

1. Memory in use
2. Type of view
3. Memory status
"""
                print(options)
                options_choice = int(input("select an option: "))
                match(options_choice):
                        case 1:
                            print("Memory in use")
                        case 2: 
                            print("Type of view")
                        case 3: 
                            print("Memory status")
    
             case 10: 
                     print("Speed dials")
             case 11: 
                     print("Voice tags")
                
         

   case 2:
        print("Messages")

        Messages = """

Welcome to Messages

Press 

1.  Write messages
2.  Inbox
3.  Outbox
4.  Picture messages
5.  Templates
6.  Smileys
7.  Message settings
8.  Info service
9.  Voice mailbox number
10. Service command editor
"""

        print(Messages)
        Messages = int(input("select an option: "))
        match(Messages):
                case 1:
                     print("Write messages")
                case 2: 
                     print("Inbox")
                case 3: 
                     print("Outbox")
                case 4: 
                     print("Picture messages")                
                case 5:
                     print("Templates")
                case 6: 
                     print("Smileys")
                case 7: 
                     print("Message settings")
                case 8: 
                     print("Info service")                
                case 9: 
                     print("Message settings")
                case 10: 
                     print("Info service")  
   case 3: print("Chat")
   case 4:
        print("Call register")
        Call_register = """
      
Welcome to Call register

Press 

1.  Missed calls
2.  Received calls
3.  Dialled numbers
4.  Erase recent call lists
5.  Show call duration
6.  Show call costs
7.  Call cost settings
8.  Prepaid credit
"""
        print(Call_register)
        Call_register_choice = int(input("select an option: "))
        match(Call_register_choice):
                    case 1:
                         print("Missed calls")
                    case 2: 
                         print("Received calls")
                    case 3:
                         print("Dialled numbers")
                    case 4:
                         print("Erase recent call lists")
                    case 5: 
                         print("Show call duration")
                         Show_call_duration = """

                               Press 

                               1. Last call duration
                               2. All calls’ duration
                               3. Received calls’ duration
                               4. Dialled calls’ duration
                               5. Clear timers
"""
                         print(Show_call_duration)
                         Show_call_duration = int(input("select an option: "))
                         match(Show_call_duration):
                            case 1:
                                 print("Last call duration")
                            case 2: 
                                 print("All calls’ duration")
                            case 3: 
                                 print("Received calls’ duration")
                            case 4: 
                                 print("Dialled calls’ duration")
                            case 5: 
                                 print("Clear timers")

                    case 6: 
                         print("Show call costs")
                         Show_call_costs = """

Welcome to Show call costs

Press 

1. Last call cost
2. All calls’ cost
3. Clear counters
"""
                         print(Show_call_costs)
                         Show_call_costs_choice = int(input("select an option: "))
                         match(Show_call_costs_choice):
                            case 1:
                                 print("Last call cost")
                            case 2:
                                 print("All calls’ cost")
                            case 3:
                                 print("Clear counters")
                    case 7:
                         print("Call cost settings")
                         Call_cost_settings = """

                             Welcome to Call cost settings

                               Press 

                               1. Call cost limit
                               2. Show costs in
"""
                         print(options)
                         Show_call_costs_choice = int(input("select an option: "))
                         match(Show_call_costs_choice):
                            case 1:
                                 print("Call cost limit")
                            case 2:
                                 print("Show costs in")
                    case 8: 
                         print("Prepaid credit")
             
                
   case 5:
        print("Tones")
        Tones = """
        
   Press
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Message alert tone
5. Keypad tones
6. Warning tones
7. Vibrating alert
8. Screen saver    
 """
        print(Tones)
        Tones = int(input("select an option: "))
        match(Tones):
                case 1:
                    print("Ringing tone")
                case 2:
                    print("Ringing volume")
                case 3: 
                    print("Incoming call alert")
                case 4: 
                    print("Message alert tone")
                case 5: 
                    print("Keypad tones")  
                case 6: 
                     print("Warning tones")
                case 7: 
                     print("Vibrating alert")
                case 8: 
                     print("Screen saver")    
   case 6: 
        print("Settings")
        Settings = """

   Press 

1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings                             
"""
        print(Settings)
        Settings = int(input("select an option: "))
        match(Settings):
            case 1:
                print("Call settings")
                Call_settings = """

 Press 

1. Automatic redial
2. Speed dialling
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic answer
"""
                print(Call_settings)
                Call_settings = int(input("select an option: "))
                match(Call_settings):
                         case 1:
                              print("Automatic redial")
                         case 2:
                              print("Speed dialling")
                         case 3: 
                              print("Call waiting options")
                         case 4: 
                              print("Own number sending")
                         case 5: 
                              print("Phone line in use")
                         case 6: 
                              print("Automatic answer")
            case 2: 
                print("Phone settings") 
                Phone_settings = """
 Press 

1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Confirm SIM service actions
"""
                print(Phone_settings)
                Phone_settings = int(input("select an option: "))
                match(Phone_settings):
                         case 1:
                              print("Language")
                         case 2:
                              print("Cell info display")
                         case 3: 
                              print("Welcome note")
                         case 4: 
                              print("Network selection")
                         case 5: 
                              print("Confirm SIM service actions")           
                 
            case 3:
                print("Security settings")
                Security_settings = """
 Press 

1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Security level
6. Change access codes
"""
                print(Security_settings)
                Security_settings = int(input("select an option: "))
                match(Security_settings):
                         case 1:
                              print("PIN code request")
                         case 2:
                              print("Call barring service")
                         case 3: 
                              print("Fixed dialling")
                         case 4: 
                              print("Closed user group")
                         case 5: 
                              print("Security level")   
            case 4:
                print("Restore factory settings")
                
   case 7: print("Call divert")
   case 8:
        print("Music")
        Music = """

    Press 
1. Music player
2. Radio
3. Recorder
4. Track list   
"""
        print(Music)
        Music = int(input("select an option: "))
        match(Music):
             case 1:
                  print("Music player")
             case 2:
                  print("Radio")
             case 3: 
                  print("Recorder")
             case 4: 
                  print(" Track list ")        
  
   case 9: print("Games")    
   case 10: print("Calculator")
   case 11: print("Reminders.")
   case 12: 
        print("Clock")
        Clock = """

    Press 
1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time  
"""

        print(Clock)
        Clock = int(input("select an option: "))
        match(Clock):
               case 1:
                    print("Alarm clock")
               case 2:
                    print("Clock settings")
               case 3: 
                    print("Date setting")
               case 4: 
                    print(" Stopwatch")
               case 5: 
                    print("Countdown timer")
               case 6: 
                    print("Auto update of date and time")

   case 13: print("Profiles")
   case 14: print("Services")
   case 15: print("SIM services")




