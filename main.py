balance = 100  # Starting balance

while True:
    print("\nUSSD Menu:")
    print("1. Check Balance")
    print("2. Buy Data")
    print("3. Buy Airtime")
    print("4. Exit")
    
    option = input("Enter option: ")

    # -------------------------------
    # Group 1: Check Balance
    if option == "1":
        print(f"your account balance is {balance} birr")    
       

    # -------------------------------
    # Group 2: Buy Data
    elif option == "2":
        print("Buy package")
        print("1. main account")
        print("2. reward account")
        account_choice = input()
        if account_choice == "1":
            print("buy package")
            print("1. for self")
            print("2. for others")
            recepient_choice = input()
            if recepient_choice == "1":
                print("buy package")
                print("1. buy voice package")
                print("2. internet")
                package_choice = input()
                if recepient_choice == "1":
                    print("1. daily Birr 3 for 15Min+3SMS+15 Min Night bonus")
                    #TO DO: add all alternatives     
                    amount_choice = input()
                    if amount_choice == "1":
                        print("confirm daily birr3 ...")
                        print("1. confirm")
                        print("2. cancel")
                        confirmation_choice = input()
                        if confirmation_choice == "1":
                            print("enter your PIN"):
                            user_pin = input()
                            # TO DO: need to cal api
                            print("your request has been send you will receive sms shortly ...")
                
        pass   # <-- Group 2: Insert your code here

    # -------------------------------
    # Group 3: Buy Airtime
    elif option == "3":
        print("Airtime/Package")
        print("1. buy airtime")
        print("2. buy package")
        choice = input()
        pass   # <-- Group 3: Insert your code here

    # -------------------------------
    # Group 4: Exit & Invalid Input
    elif option == "4":
        pass   # <-- Group 4: Insert your code to handle exit here
        break
    else:
        pass   # <-- Group 4: Insert your code to handle invalid input here
