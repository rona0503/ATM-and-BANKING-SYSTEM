##  ATM and Banking System Release Version 1.1.0
##  Leader:     Ronald Vincent G. Sarmiento
##  Members:    Lorenz Gabriel Velasco
##              Charles Justin E. Glorioso
##              Marc Daniel Y. Gabrillo
##              Remier John M. Kundiman
##
##  Major Notable Contributions:
##      Charles Justin E. Glorioso  - Developed standalone Withdraw() feature to be sent to Ronald Vincent to be compiled and incorporated into the main program
##      Marc Daniel Y. Gabrillo     - Developed standalone Deposit()  feature to be sent to Ronald Vincent to be compiled and incorporated into the main program
##      Remier John M. Kundiman     - Developed standalone Transfer() feature to be sent to Ronald Vincent to be compiled and incorporated into the main program
##      Lorenz Gabriel Velasco      - Developed the program over 2 development cycles (see pastebin below)
##                                  - Developed the Bank Receipt Generation feature that handles receipt generation for transactions such as withdrawal, deposit and transferring funds excluding the investReceipt subfunction
##                                  - Developed the Investment feature that generates interest annually based on investment
##
##      Ronald Vincent G. Sarmiento - Developed the Account Class and its methods (Excluding UpdateInvestment and GetInvestmentBalance methods) for the foundation of the Account Database
##                                  - Developed the Account Creation function that takes Name, 16-Digit National I.D, Email, Phone Number, Password and Initial Deposit as user input
##                                  - Developed the mainLoop function to substitute for main()
##                                  - Developed the Account Status Interface for presenting individual account information
##                                  - Developed the Login Function
##                                  - Developed the Edit Account Information that allows the user to edit their user information provided that their new information is not the same as the information of other accounts
##                                  - Developed the Transaction History function in where the user can see their transactions such as withdrawal, deposit, transferring funds, receiving funds, investing and receiving interest from the investment
##                                  - Implemented the Options features in where the user can input what function they want to access (Excluding options in bank receipt and Investment functions)
##                                  - Implemented Confirmation features for each critical user input for minimizing accidents
##                                  - Incorporated and handled the Withdraw, Deposit and TransferFunds feature into the main program and accounted for possible errors
##                                  - Handled errors in the whole program using While Loops
##                                  - Handled the formatting of this program
##                                  - Fixed bugs that popped up during the development cycle
##



from datetime import datetime
accountDatabase = []
class Account:
    def __init__(self, accountNumber, name, idNumber, email,  phoneNumber, password, initialDeposit):
        self.accountNumber = accountNumber
        self.FirstName, self.MiddleInitial, self.Surname = name
        self.idNumber = idNumber
        self.email = email
        self.phoneNumber = phoneNumber
        self.password = password
        self.currentBalance = initialDeposit #Because at creation, your current balance is the one you started with

    def ShowAccountInformation(self):
        print("Account Info: \n")
        print(f"Account Name: {self.GetName()}")
        print(f"Account Number: {self.GetAccountNumber()}")
        print(f"National I.D: {self.GetIDNumber()}")
        print(f"Email: {self.GetEmail()}")
        print(f"Phone Number: {self.GetPhoneNumber()}")
        print(f"Password: {self.GetPassword()}")
        print(f"Account Balance: Php {self.GetCurrentBalance()}\n")

    def GetName(self):
        return " ".join(list((self.FirstName, self.MiddleInitial, self.Surname))) #returns string

    def GetIDNumber(self):
        return self.idNumber #returns string in the format 1234-1234-1234

    def GetEmail(self):
        return self.email

    def GetPhoneNumber(self):
        return self.phoneNumber

    def GetPassword(self):
        return self.password
    
    def GetAccountNumber(self):
        return self.accountNumber #Returns string

    def GetCurrentBalance(self):
        return self.currentBalance #Returns int

    def UpdateBalance(self, value):
        self.currentBalance = f"{float(self.currentBalance) +  value: .2f}" # For Subtraction, set value as negative ( -100 ) so that currentBalance += (-100)

    def UpdateName(self, name):
        self.FirstName, self.MiddleInitial, self.Surname = name

    def UpdateIDNumber(self, idNumber):
        self.idNumber = idNumber

    def UpdateEmail(self, email):
        self.email = email

    def UpdatePhoneNumber(self, PhoneNumber):
        self.phoneNumber = PhoneNumber

    def UpdatePassword(self, password):
        self.password = password

    def UpdateInvestment(self, amount):
        if hasattr(self, 'investmentBalance'):
            self.investmentBalance += amount
        else:
            self.investmentBalance = amount

    def GetInvestmentBalance(self):
        return getattr(self, 'investmentBalance', 0.0)

    def UpdateInterestAmountAnnually(self, accountDatabase, interestDate = None):
        
        if not hasattr(self, 'compoundDate') and interestDate != None:
            try:
                self.compoundDate = interestDate.replace(year = interestDate.year + 1)
            except ValueError:
                self.compoundDate = interestDate.replace(month = 2, day = 28, year = interestDate.year + 1)
            self.formattedCompoundDate = self.compoundDate.strftime("%Y-%m-%d")
        elif hasattr(self, 'compoundDate'):
            dateNow = datetime.now()
            
##            #Testing of Intrest Calculation
##            try:
##                dateNow = dateNow.replace(year = dateNow.year + 1)
##            except ValueError:
##                dateNow = dateNow.replace(month = 2, day = 28, year = dateNow.year + 1)
            dateNow = dateNow.strftime("%Y-%m-%d")

            
            if self.formattedCompoundDate == dateNow:
                previousInvestmentBalance = self.GetInvestmentBalance()
                
                #Compute Interest
                interest = self.GetInvestmentBalance() * 0.1 * 1
                #Final Amount
                self.UpdateInvestment(interest)

                #Set CompoundDate to 1 year later
                try:
                    self.compoundDate = self.compoundDate.replace(year = self.compoundDate.year + 1)
                except ValueError:
                    self.compoundDate = self.compoundDate.replace(month = 2, day = 28, year = self.compoundDate.year + 1)
                self.formattedCompoundDate = self.compoundDate.strftime("%Y-%m-%d")

                self.UpdateTransactionHistory(accountDatabase, accountDatabase.index(self), "interestReceived", previousInvestmentBalance, self.GetCurrentInvestment())

                
            
            

    def UpdateTransactionHistory(self, accountDatabase, accountIndex, transactionType, amount, previousBalance, currentBalance, recipientIndex=None):
        if not hasattr(self, 'transactionHistory'):
            self.transactionHistory = []
        if hasattr(self, 'transactionHistory'):
            dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            amount = float(amount)
            
            if transactionType == "withdraw":
                transaction = f"{dateTime} : Withdrew Php {amount: .2f}. Previous Balance: Php {previousBalance}. Current Balance: Php {currentBalance}" 
                self.transactionHistory.append(transaction)
            if transactionType == "deposit":
                transaction = f"{dateTime} : Deposit  Php {amount: .2f}. Previous Balance: Php {previousBalance}. Current Balance: Php {currentBalance}"
                self.transactionHistory.append(transaction)
            if transactionType == "transfer":
                transaction = f"{dateTime} : Transferred Php {amount: .2f} to {accountDatabase[recipientIndex].GetName()}. Previous Balance: Php {previousBalance}. Current Balance: Php {currentBalance}"
                self.transactionHistory.append(transaction)
            if transactionType == "received":
                transaction = f"{dateTime} : Received Php {amount: .2f} from {accountDatabase[accountIndex].GetName()}. Previous Balance: Php {previousBalance}. Current Balance: Php {currentBalance}"
                self.transactionHistory.append(transaction)
            if transactionType == "invest":
                transaction = f"{dateTime} : Invested Php {amount: .2f}. Previous Balance: Php {previousBalance}. Current Balance: Php {currentBalance}"
                self.transactionHistory.append(transaction)
            if transactionType == "interestReceived":
                transaction = f"{dateTime} : Interest compounded worth Php {amount: .2f}. Previous InvestmentBalance: Php {previousBalance}. Current Investment Balance: Php {currentBalance}"
                self.transactionHistory.append(transaction)

    def ShowTransactionHistory(self):
        print("-----------------------------Transaction History----------------------------\n")

        if hasattr(self, 'transactionHistory'):
            for transaction in self.transactionHistory:
                print(transaction)
            print("")
        else:
            print("You have not made any transactions yet.\n")
        
        print("----------------------------------------------------------------------------\n")
    def Withdraw(self,accountDatabase, Amount):
        if float(Amount) <= float(self.GetCurrentBalance()):
            previousBalance = self.currentBalance
            self.currentBalance = float(self.currentBalance) - float(Amount)
            self.currentBalance = f"{float(self.currentBalance): .2f}"
            print(f"Withdrawal successful.. \nNew Balance: {self.GetCurrentBalance()}")
            print("----------------------------------------------------------------------------\n")
            bankreciept(accountDatabase, accountDatabase.index(self), "withdraw", Amount)
            self.UpdateTransactionHistory(accountDatabase, accountDatabase.index(self), "withdraw", Amount, previousBalance, self.currentBalance)
        else:
            print("Insufficient Funds.\n")
            print("----------------------------------------------------------------------------\n")

    def Deposit(self):
        print("----------------------------------Deposit----------------------------------\n")
        while True:
            try:
                Amount = float(input("Enter the amount you want to deposit: "))
                if len(str(Amount).split(".")[-1]) >= 3:
                    print("Invalid amount of decimal places. Please try again \n")
                elif Amount >= 0:
                    while True:
                        confirm = input(f"Are you sure you want to deposit {Amount: .2f}? Confirm Yes or No. ").lower()
                        if confirm == "yes" or confirm == "no":
                            break
                        else:
                            print("Invalid Input. Please try again. \n")
                    if confirm == "yes":
                        previousBalance = self.currentBalance
                        self.currentBalance = float(self.currentBalance) + Amount
                        self.currentBalance = f"{float(self.currentBalance): .2f}"
                        print("Deposit successful.\n")
                        print("----------------------------------------------------------------------------\n")
                        bankreciept(accountDatabase, accountDatabase.index(self), "deposit", Amount)
                        self.UpdateTransactionHistory(accountDatabase, accountDatabase.index(self), "deposit", Amount, previousBalance, self.currentBalance)
                        break
                else:
                    print("Invalid amount. Please enter a positive value\n")
            except ValueError:
                print("Invalid Input. Please enter a numerical value\n")

#here i added the bank reciept for withdrawal and deposit(lorenz)


#Account Information Changes
def ChangeName(accountDatabase, accountIndex):
    print("\nEdit Name\n")
    print(f"Your current name is {accountDatabase[accountIndex].GetName()}\n")

    
   #Name
    while True:
        name = [input("Enter your new First Name: "),
                input("Enter your new Middle Initial: "),
                input("Enter your new Surname: ")]

        if not all(((s.isalpha() or s == "." or s == " ") for s in names) and ((names.endswith(".") and names[:-1].isalpha()) if "." in names else all(word.isalpha() for word in names.split())) for names in name):
            print("You have entered an invalid name, Please try again.\n")
        else:
            while True:
                confirm = input(f"Your new name is {name[0]} {name[1]} {name[2]}. Confirm? Yes or No. Or enter exit to exit: ").lower()

                if confirm == "yes" or confirm == "no":
                    break
                else:
                    print("Invalid input, please try again.\n")
                    
            if confirm == "yes":
                if any((" ".join(name) == account.GetName() and not (accountIndex == accountDatabase.index(account) ) ) for account in accountDatabase):
                    print("There is already an existing account with the same name. Please try again. \n")
                else:
                    print("Confirming changes......\n")
                    print("----------------------------------------------------------------------------\n")
                    accountDatabase[accountIndex].UpdateName(name)
                    break
            elif confirm == "no":
                print("")
            if confirm == "exit":
                print("----------------------------------------------------------------------------\n")
                break
        
def ChangeIDNumber(accountDatabase, accountIndex):
    print("\nEdit National I.D\n")
    print(f"Your current National I.D Number is {accountDatabase[accountIndex].GetIDNumber()}\n")

    while True:
        idNumber = input("Enter your new 16-digit National I.D No.: ")


        #Handles error for cases such as "123--123--1234", "123", "1234-1234-123-"
        if (not all((len(idNumber)== 19 or len(idNumber) == 16) and (s.isdigit() or s == " " or s == "-") for s in idNumber)) or ((len(idNumber) == 19) and  not all( (( (chunk[-1] == "-" or chunk[-1] == " ") and (all(digits.isdigit() for digits in chunk[:-1]) ) ) for chunk in [idNumber[i:i+5] for i in range(0, len(idNumber) + 1, 5)][:-1] ) ) or not all ((digits.isdigit() for digits in idNumber[15:19]) )
):
            print("Invalid Input, Please try again.\n")
        else:

            # Formats the variable into " 1234-1234-1234 " 
            if (len(idNumber) == 16 and (s.isdigit() for s in idNumber)):
                idNumber = "-".join(idNumber[i: i+4] for i in range(0, len(idNumber),4))   

            if (len(idNumber) == 19) and (idNumber[4] == " " or idNumber[4] == "-") or (idNumber[9] == " " or idNumber[9] == "-")  or (idNumber[14] == " " or idNumber[14] =="-" ):
                idNumber = idNumber[:4] + "-" + idNumber[5:]
                idNumber= idNumber[:9] + "-" + idNumber[10:]
                idNumber = idNumber[:14] + "-" + idNumber[15:]

            while True:
                confirm = input(f"Your new National I.D Number is {idNumber}. Confirm? Yes or No. Or enter exit to exit: ").lower()

                if confirm == "yes"  or confirm == "no" or confirm == "exit":
                    break
                else:
                    print("Invalid input, Please try again\n")

            if confirm == "yes":
                if any((idNumber == account.GetIDNumber() and not(accountIndex == accountDatabase.index(account))) for account in accountDatabase):
                    print("There is already an existing account with the same ID Number. Please try again \n")
                else:
                    print("Confirming changes.....\n\n")
                    print("----------------------------------------------------------------------------\n")
                    accountDatabase[accountIndex].UpdateIDNumber(idNumber)
                    break
            elif confirm == "no":
                print("")
            if confirm == "exit":
                print("----------------------------------------------------------------------------\n")
                break

def ChangeEmail(accountDatabase, accountIndex):
    print("\nEdit Email\n")
    print(f"Your current email is {accountDatabase[accountIndex].GetEmail()}\n")

    while True:
        email = input("Enter your new email: ")

        if not email.endswith(".com")  or email == ".com":
            print("Invalid Input. Please try again. \n")
        else:
            while True:
                confirm = input(f"Your new email is {email}. Confirm? Yes or No. or enter exit to exit: ").lower()

                if confirm == "yes" or confirm == "no" or confirm == "exit":
                    break
                else:
                    print("Invalid input, please try again.\n")
                    
            if confirm == "yes":
                
                if any((email == account.GetEmail() and not (accountIndex == accountDatabase.index(account))) for account in accountDatabase):
                    print("There is already an existing account with the same email. Please try again. \n")
                else:
                    print("Confirming changes.....\n\n")
                    print("----------------------------------------------------------------------------\n")
                    accountDatabase[accountIndex].UpdateEmail(email)
                    break
            elif confirm == "no":
                print("")
            if confirm == "exit":
                print("----------------------------------------------------------------------------\n")
                break

def ChangePhoneNumber(accountDatabase, accountIndex):
    print("\nEdit Phone Number\n")
    print(f"Your current Phone Number is {accountDatabase[accountIndex].GetPhoneNumber()}\n")

    while True:
        phoneNumber = input("Input your Phone Number: ")

        if not (len(phoneNumber) == 11) or not phoneNumber.startswith("09") or not all(digits.isdigit() for digits in phoneNumber):
            print("Invalid Input. Please Try again. \n")
        else:
            while True:
                confirm = input(f"Your phone number is {phoneNumber}. Confirm? Yes or No: ").lower()

                if confirm == "yes" or confirm == "no" or confirm == "exit":
                    break
                else:
                    print("Invalid input, please try again.\n")
                    
            if confirm == "yes":
                
                if any((phoneNumber == account.GetPhoneNumber() and not (accountIndex == accountDatabase.index(account))) for account in accountDatabase):
                    print("There is already an existing account with the same phone number. Please try again \n")
                else:
                    print("Confirming changes.....\n\n")
                    print("----------------------------------------------------------------------------\n")
                    accountDatabase[accountIndex].UpdatePhoneNumber(phoneNumber)
                    break
            elif confirm == "no":
                print("")
            if confirm == "exit":
                print("----------------------------------------------------------------------------\n")
                break

def ChangePassword(accountDatabase, accountIndex):
    print("\nEdit Password\n")
    print(f"Your current password is {accountDatabase[accountIndex].GetPassword()}\n")

    
    while True:
        password = input("Input New Password: ")
        while True:
            confirm = input(f"Your password is {password}. Confirm? Yes or No. or enter exit to exit: ").lower()

            if confirm == "yes" or confirm == "no" or confirm == "exit":
                break
            else:
                print("Invalid Input. Please Try again\n")

        if confirm == "yes":
            print("Confirming changes.....\n\n")
            print("----------------------------------------------------------------------------\n")
            accountDatabase[accountIndex].UpdatePassword(password)
            break
        elif confirm == "no":
            print("")
        if confirm == "exit":
            print("----------------------------------------------------------------------------\n")
            break




#Creates Account
def AccountCreation(accountDatabase):
    print("------------------------Welcome to Account Creation!------------------------\n")
    accountNumber = str(len(accountDatabase) + 100000)

    print("Name Field \n")
    #Name
    while True:
        name = [input("Enter your First Name: "),
                input("Enter your Middle Initial: "),
                input("Enter your Surname: ")]

        if not all(((s.isalpha() or s == "." or s == " ") for s in names) and ((names.endswith(".") and names[:-1].isalpha()) if "." in names else all(word.isalpha() for word in names.split())) for names in name):
            print("You have entered an invalid name, Please try again.\n")
        else:
            while True:
                confirm = input(f"Your name is {name[0]} {name[1]} {name[2]}. Confirm? Yes or No: ").lower()

                if confirm == "yes" or confirm == "no":
                    break
                else:
                    print("Invalid input, please try again.\n")
                    
            if confirm == "yes":
                if any(" ".join(name) == account.GetName() for account in accountDatabase):
                    print("There is already an existing account with the same name. Please try again. \n")
                else:    
                    break
            elif confirm == "no":
                print("")

    print("\nNational I.D  \n")
    #ID Number
    while True:
        idNumber = input("Enter your 16-digit National I.D No. : ")


        #Handles error for cases such as "123--123--1234", "123", "1234-1234-123-"
        if (not all((len(idNumber)== 19 or len(idNumber) == 16) and (s.isdigit() or s == " " or s == "-") for s in idNumber)) or ((len(idNumber) == 19) and  not all( (( (chunk[-1] == "-" or chunk[-1] == " ") and (all(digits.isdigit() for digits in chunk[:-1]) ) ) for chunk in [idNumber[i:i+5] for i in range(0, len(idNumber) + 1, 5)][:-1] ) ) or not all ((digits.isdigit() for digits in idNumber[15:19]) )
):
            print("Invalid Input, Please try again.\n")
        else:

            # Formats the variable into " 1234-1234-1234 " 
            if (len(idNumber) == 16 and (s.isdigit() for s in idNumber)):
                idNumber = "-".join(idNumber[i: i+4] for i in range(0, len(idNumber),4))   

            if (len(idNumber) == 19) and (idNumber[4] == " " or idNumber[4] == "-") or (idNumber[9] == " " or idNumber[9] == "-")  or (idNumber[14] == " " or idNumber[14] =="-" ):
                idNumber = idNumber[:4] + "-" + idNumber[5:]
                idNumber= idNumber[:9] + "-" + idNumber[10:]
                idNumber = idNumber[:14] + "-" + idNumber[15:]
            while True:
                confirm = input(f"Your National I.D Number is {idNumber}. Confirm? Yes or No: ").lower()

                if confirm == "yes"  or confirm == "no":
                    break
                else:
                    print("Invalid input, Please try again\n")

            if confirm == "yes":
                if any(idNumber == account.GetIDNumber() for account in accountDatabase):
                    print("There is already an existing account with the same ID Number. Please try again \n")
                else:
                    break
            elif confirm == "no":
                print("")

    print("\nEmail Details\n")
    #Email
    while True:
        email = input("Enter your email: ")

        if not email.endswith(".com")  or email == ".com":
            print("Invalid Input. Please try again. \n")
        else:
            while True:
                confirm = input(f"Your email is {email}. Confirm? Yes or No: ").lower()

                if confirm == "yes" or confirm == "no":
                    break
                else:
                    print("Invalid input, please try again.\n")
                    
            if confirm == "yes":
                if any(email == account.GetEmail() for account in accountDatabase):
                    print("There is already an existing account with the same email. Please try again. \n")
                else:
                    break
            elif confirm == "no":
                print("")

    print("\nPhone Number\n")
    #Phone Number
    while True:
        phoneNumber = input("Input your Phone Number: ")

        if not (len(phoneNumber) == 11) or not phoneNumber.startswith("09") or not all(digits.isdigit() for digits in phoneNumber):
            print("Invalid Input. Please Try again. \n")
        else:
            while True:
                confirm = input(f"Your phone number is {phoneNumber}. Confirm? Yes or No: ").lower()

                if confirm == "yes" or confirm == "no":
                    break
                else:
                    print("Invalid input, please try again.\n")
                    
            if confirm == "yes":
                if any(phoneNumber == account.GetPhoneNumber() for account in accountDatabase):
                    print("There is already an existing account with the same phone number. Please try again \n")
                else:
                    break
            elif confirm == "no":
                print("")

    print("\nPassword\n")
    #Password No error handling here, because.... passwords..
    while True:
        password = input("Input Password: ")
        while True:
            confirm = input(f"Your password is {password}. Confirm? Yes or No: ").lower()

            if confirm == "yes" or confirm == "no":
                break
            else:
                print("Invalid Input. Please Try again\n")

        if confirm == "yes":
            break
        elif confirm == "no":
            print("")

        
    print("\nYour Initial Deposit\n")
    #Initial Deposit
    while True:
        try:
            #input
            while True:
                initialDeposit = input("Enter initial deposit: ")

                isdeposit = float(initialDeposit)
                if "." not in initialDeposit:
                    initialDeposit = f"{float(initialDeposit): .2f}"
                    break
                elif "." in initialDeposit:
                    if not (len(initialDeposit.split(".")[-1]) == 2) and not(len(initialDeposit.split(".")[-1]) == 1):
                        print("Invalid amount of decimal places. Please try again. \n")
                    else:
                        break

            #Confirmation
            while True:
                confirm = input(f"Your initial deposit is {float(initialDeposit): .2f}. Confirm?. Yes or No: ").lower()

                if confirm == "yes" or confirm == "no":
                    break
                else:
                    print("Invalid Input. Please try again\n")
            if confirm == "yes":
                break
            elif confirm == "no":
                print("")
                
        except ValueError:
            print("Enter a proper value. Please try again.\n")

        
    #Creating new account object
    newAccount = Account(accountNumber, name, idNumber, email, phoneNumber, password, initialDeposit)

    #Appending new account to the database
    accountDatabase.append(newAccount)

    print("\nCongratulations, you have created your account, Logging in....")
    print("----------------------------------------------------------------------------\n")
    
    #Actual Logging in
    AccountStatusInterface(accountDatabase, len(accountDatabase)-1)

        
#Login to account
def Login(accountDatabase):
    print("---------------------------------Log in Page--------------------------------\n")
    while True:

        #Account Number
        while True:
            accountNumber = input("Enter your account number or enter exit to exit: ")
            if accountNumber.lower() == "exit":
                break
            if not any(accountNumber == account.GetAccountNumber() for account in accountDatabase):
                print("That account number does not exist in our database. Please try again.\n")
            else:
                break
        
        if accountNumber.lower() == "exit":
            break

        #Email
        while True:
            email = input("Enter your email or enter exit to exit: ")
            if email.lower() == "exit":
                break
            if not any(email == account.GetEmail() for account in accountDatabase):
                print("Invalid Email. Please Try again.\n")
            else:
                break
        
        if email.lower() == "exit":
            break

        #Password
        while True:
            password = input("Enter your password: ")
            if not any( password == account.GetPassword() for account in accountDatabase):
                print("Invalid Password. Please try again. \n")
            else:
                break
        
        #Actual Logging in
        for account in accountDatabase:
            if accountNumber == account.GetAccountNumber() and email == account.GetEmail() and password == account.GetPassword():
                AccountStatusInterface(accountDatabase, accountDatabase.index(account))
                break
                
        #Checked if Logged in
        if not any((accountNumber == account.GetAccountNumber() and email == account.GetEmail() and password == account.GetPassword()) for account in accountDatabase):
            print("Invalid Account Number, Email and Password. Please try again.\n")
        else:
            break
        
def EditAccountInfo(accountDatabase, accountIndex):
    
    while True:
        print("--------------------------Edit Account Information--------------------------\n")
        

        while True:
            options = ["a","b","c","d","e","f"]

            userInput = input("What would you like to edit?: \n" +
                              "a.Name\n" +
                              "b.National I.D\n" +
                              "c.Email\n" +
                              "d.Phone Number\n" +
                              "e.Password\n" +
                              "f.Quit\n").lower()

            if any(userInput == option for option in options):
                if userInput == "a":
                    ChangeName(accountDatabase, accountIndex)
                if userInput == "b":
                    ChangeIDNumber(accountDatabase, accountIndex)
                if userInput == "c":
                    ChangeEmail(accountDatabase, accountIndex)
                if userInput == "d":
                    ChangePhoneNumber(accountDatabase, accountIndex)
                if userInput == "e":
                    ChangePassword(accountDatabase, accountIndex)
                break
            else:
                print("Invalid Input. Please try again.\n")
                
        if userInput == "f":
            print("----------------------------------------------------------------------------\n")
            break


#########################################################################
        
def transferFunds(accountDatabase, senderIndex):
    print("------------------------------ Transfer Funds ------------------------------\n")
    sender = accountDatabase[senderIndex]
    if len(accountDatabase) < 2:
        print("At least two accounts are required to transfer funds.\n")
        print("----------------------------------------------------------------------------\n")
        return
    while True:
        recipientAccountNumber = input("Enter the recipient's account number: \nOr enter exit to exit: ")
        if recipientAccountNumber.lower() == "exit":
            print("Returning.......\n")
            print("----------------------------------------------------------------------------\n")
            return
        recipient = None
        for account in accountDatabase:
            if account.GetAccountNumber() == recipientAccountNumber:
                recipient = account
                break
        if not recipient:
            print("Recipient account not found.")
            print("----------------------------------------------------------------------------\n")
            return
        if recipient == sender:
            print("You cannot transfer funds to your own account.")
            print("----------------------------------------------------------------------------\n")
            return
        else:
            while True:
                confirm = input(f"You want to transfer funds to {recipient.GetName()} (Account No.: {recipient.GetAccountNumber()}) Confirm Yes or No: ").lower()
                if confirm == "yes" or confirm == "no":
                    break
                else:
                    print("Invalid Input. Please try again. \n")
        if confirm == "yes":
            break
    while True:
        try:
            amount = float(input("\nEnter the amount to transfer: "))
            if amount <= 0:
                print("Amount must be greater than zero.\n")
            elif amount > float(sender.GetCurrentBalance()):
                print("Insufficient balance.\n")
            else:
                while True:
                    confirm = input(f"You want to transfer {amount: .2f}? Confirm Yes or No: ").lower()
                    if confirm == "yes" or confirm == "no":
                        break
                    else:
                        print("Invalid Input. Please try again. \n")
                if confirm == "yes":
                    break
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    #here i change the balance so that the recipt will show the correct balance
    senderPreviousBalance = sender.GetCurrentBalance()
    recipientPreviousBalance = recipient.GetCurrentBalance()
    sender.UpdateBalance(-amount)
    recipient.UpdateBalance(amount)
    print(f"Transferred {amount:.2f} to {recipient.GetName()} (Account No.: {recipient.GetAccountNumber()}).")
    print("----------------------------------------------------------------------------\n")
    bankreciept(accountDatabase, senderIndex, "transfer", amount, accountDatabase.index(recipient))
    sender.UpdateTransactionHistory(accountDatabase, senderIndex, "transfer", amount, senderPreviousBalance, sender.GetCurrentBalance(), accountDatabase.index(recipient))
    recipient.UpdateTransactionHistory(accountDatabase, senderIndex, "received", amount, recipientPreviousBalance, recipient.GetCurrentBalance(), accountDatabase.index(recipient))

    #here i add the receipt for the recipient(lorenz)


#################################################################################

def AccountStatusInterface(accountDatabase, accountIndex):
    print("\n")
    while True:
        accountDatabase[accountIndex].UpdateInterestAmountAnnually(accountDatabase)

        
        print("------------------------Welcome to your Account Page------------------------\n")
        
        accountDatabase[accountIndex].ShowAccountInformation()

        #Here iinsert ang options for withdrawal, fund transfer, all transaction history etc.. add nyo lang sa userInput ung options (b, c, etc....) and lagay nyo rin ung letter sa options list in lowercase

        options = ["a", "b","c","d","e", "f", "g"] # add option here
        
        userInput = input("What would you like to do?\n" +
                          "A. Edit Account Info\n" +
                          "B. Withdraw\n" +
                          "C. Deposit\n" +
                          "D. Transfer\n" +
                          "E .Investment\n" +
                          "F. Show Transaction History\n" +
                          "G. Exit\n").lower()
        if any(userInput == option for option in options):
            if userInput == "a":
                print("----------------------------------------------------------------------------\n")
                EditAccountInfo(accountDatabase,accountIndex)
            if userInput == "b":
                print("----------------------------------------------------------------------------\n")
                while True:
                    print("----------------------------------Withdraw----------------------------------\n")
                    try:
                        while True:
                            Amount = input("How much would you like to withdraw?: ")

                            isAmountFloat = float(Amount) #returns valueerror if not float

                            if "." in Amount:
                                if not(len(Amount.split(".")[-1]) == 2) and not (len(Amount.split(".")[-1]) == 1):
                                    print("Invalid Amount of decimal places. Please try again. \n")
                                else:
                                    Amount = f"{float(Amount): .2f}"
                                    break
                            elif "." not in Amount:
                                Amount = f"{float(Amount): .2f}"
                                break

                        while True:
                            confirm = input(f"You want to withdraw {float(Amount): .2f}. Confirm? Yes or No\n").lower()

                            if confirm == "yes" or confirm == "no":
                                break
                            else:
                                print("Invalid Input. Please Try again. \n")
                                
                        if confirm == "yes":
                            break

                        
                    except ValueError:
                        print("Invalid Input. Please try again\n")

                    

                accountDatabase[accountIndex].Withdraw(accountDatabase, Amount)
            if userInput == "c":
                print("----------------------------------------------------------------------------\n")
                accountDatabase[accountIndex].Deposit()
            if userInput == "d":
                print("----------------------------------------------------------------------------\n")
                transferFunds(accountDatabase, accountIndex)
            if userInput == "e":
                print("----------------------------------------------------------------------------\n")
                investment(accountDatabase, accountIndex)
            if userInput == "f":
                print("----------------------------------------------------------------------------\n")
                accountDatabase[accountIndex].ShowTransactionHistory()
        else:
            print("Invalid Input. Please try again\n")
            print("----------------------------------------------------------------------------\n")

        #if user chose to quit
        if userInput == "g":
            print("----------------------------------------------------------------------------\n")
            break

def bankreciept(accountDatabase, accountIndex, transactionType, amount, recipientIndex=None):
    dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bankstatement = "Please make sure that you have a copy of your receipt for future reference."
    
    def withdrawreciept(accountDatabase, accountIndex):
        print("-----------------------------Withdrawal Receipt-----------------------------\n")
        print(f"Name: {accountDatabase[accountIndex].GetName()}")
        print(f"Account Number: {accountDatabase[accountIndex].GetAccountNumber()}")
        print(f"Timestamp: {dateTime}")
        print(f"Amount Withdrawn: {amount}")
        print(f"New Balance: {accountDatabase[accountIndex].GetCurrentBalance()}\n")
        print(bankstatement)
        print("----------------------------------------------------------------------------\n\n")
    
    def depositreciept(accountDatabase, accountIndex):
        print("------------------------------Deposit Receipt-------------------------------\n")
        print(f"Name: {accountDatabase[accountIndex].GetName()}")
        print(f"Account Number: {accountDatabase[accountIndex].GetAccountNumber()}")
        print(f"Timestamp: {dateTime}")
        print(f"Amount Deposited: {amount}")
        print(f"New Balance: {accountDatabase[accountIndex].GetCurrentBalance()}\n")
        print(bankstatement)
        print("----------------------------------------------------------------------------\n\n")
    
    def transferreciept(accountDatabase, senderIndex, recipientIndex):
        print("------------------------------Transfer Receipt------------------------------\n")
        print("Your transaction is successful")
        print(f"Timestamp: {dateTime}")
        print(f"Sender: {accountDatabase[senderIndex].GetName()}")
        print(f"Recipient: {accountDatabase[recipientIndex].GetName()}")
        print(f"Amount Transferred: {amount}\n")
        print(bankstatement)
        print("----------------------------------------------------------------------------\n\n")

    def investmentReceipt(accountDatabase, accountIndex):
        print("----------------------------Investment Receipt------------------------------\n")
        print(f"Name: {accountDatabase[accountIndex].GetName()}")
        print(f"Account Number: {accountDatabase[accountIndex].GetAccountNumber()}")
        print(f"Timestamp: {dateTime}")
        print(f"Amount Invested: {amount}")
        print(f"New Investment Balance: {accountDatabase[accountIndex].GetInvestmentBalance()}\n")
        print(bankstatement)
        print("----------------------------------------------------------------------------\n\n")
    
    if transactionType == "withdraw":
        withdrawreciept(accountDatabase, accountIndex)
    elif transactionType == "deposit":
        depositreciept(accountDatabase, accountIndex)
    elif transactionType == "transfer":
        transferreciept(accountDatabase, accountIndex, recipientIndex)
    elif transactionType == "invest":
        investmentReceipt(accountDatabase, accountIndex)

def investment(accountDatabase, accountIndex):
    dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def interest(accountDatabase, accountIndex):
        print("----------------------------------Interest----------------------------------\n")
        
        while True:
            interest = input("Would you like to invest? Yes or No: ").lower()

            if interest not in ["yes", "no"]:
                print("Invalid input. Please enter 'yes' or 'no'.")
            else:
                break

        if interest == "yes":
            while True:
                try:
                    amount = float(input("Enter the amount you want to invest: "))
                    if amount <= 0:
                        print("Invalid amount. Please enter a positive number.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

                #Confirmation
                while True:
                    confirm = input(f"Your investment amount is {amount: .2f}. Confirm?. Yes or No: \nOr enter exit to exit: ").lower()

                    if confirm == "yes" or confirm == "no":
                        break
                    elif confirm == "exit":
                        print("Exiting Interest Page.........\n")
                        print("----------------------------------------------------------------------------\n")
                        return
                    else:
                        print("Invalid Input. Please try again")
                if confirm == "yes":
                    break

            

            currentBalance = float(accountDatabase[accountIndex].GetCurrentBalance())
            if currentBalance >= amount:
                previousBalance = accountDatabase[accountIndex].GetCurrentBalance()
                accountDatabase[accountIndex].UpdateBalance(-amount)  # Deduct from current balance
                accountDatabase[accountIndex].UpdateInvestment(amount)  # Add to investment balance
                accountDatabase[accountIndex].UpdateInterestAmountAnnually(accountDatabase, datetime.now())
                accountDatabase[accountIndex].UpdateTransactionHistory(accountDatabase, accountIndex, "invest", amount, previousBalance, accountDatabase[accountIndex].GetCurrentBalance())
                print("You have successfully invested in our bank")
                print("You will receive your interest annually")
                print("Thank you for investing in our bank")
                print("----------------------------------------------------------------------------\n")
                bankreciept(accountDatabase, accountIndex, "invest", amount)
            else:
                print("Insufficient balance to invest.")
        elif interest == "no":
            print("Thank you for visiting our bank")
            print("Have a nice day")
            print("Goodbye.")
            print("----------------------------------------------------------------------------\n")
            return

    def dashboard(accountDatabase, accountIndex):
        try:
            while True:
                user = input("\nDo you want to view your dashboard? \nYes or No: ").lower()

                if user not in ["yes", "no"]:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                else:
                    print("----------------------------------------------------------------------------\n")
                    break

            if user == "yes":
                print("---------------------------------Dashboard----------------------------------")
                print(f"Name: {accountDatabase[accountIndex].GetName()}")
                print(f"Account Number: {accountDatabase[accountIndex].GetAccountNumber()}")
                print(f"Your current savings amount is: {accountDatabase[accountIndex].GetCurrentBalance()}")
                print(f"Your current investment amount is: {accountDatabase[accountIndex].GetInvestmentBalance()}")
                print(f"Timestamp: {dateTime}\n")
                print("Thank you for investing in our bank")
                print("Have a nice day")
                print("----------------------------------------------------------------------------\n")
            elif user == "no":
                return
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    while True:
        print("-------------------------------Investment Page------------------------------\n")
        try:
            while True:
                show = input("Do you want to: \n1. View Dashboard  \n2. Invest \n3. Exit \n").strip()

                if show not in ["1", "2", "3"]:
                    print("Invalid input. Please enter 1, 2, or 3.\n")
                else:
                    break

            if show == "1":
                dashboard(accountDatabase, accountIndex)
            elif show == "2":
                print("----------------------------------------------------------------------------\n")
                interest(accountDatabase, accountIndex)
            elif show == "3":
                print("Thank you for visiting our bank")
                print("Have a nice day")
                print("Goodbye\n")
                print("----------------------------------------------------------------------------\n")
                return
        except Exception as e:
            print(f"An unexpected error occurred: {e}")



#Main Loop
def mainLoop():
    print("-----------------------------Welcome to XXX bank----------------------------\n")

    #Ensures that no errors are passed through and handles errors
    while True:
         userInput = input("What would you like to do?\n" +
                           "A. Login to your account\n" +
                           "B. Create Account\n" +
                           "C. Quit\n"                                 )
         #Ensures consistency
         userInput = userInput.lower()
         
         #function selection
         options = ["a", "b", "c"]
         if any(userInput == option for option in options):
             if userInput == "a":
                if len(accountDatabase) != 0:
                    print("----------------------------------------------------------------------------\n")
                    Login(accountDatabase)
                    print("-----------------------------Welcome to XXX bank----------------------------\n")
                else:
                    print("There are no accounts stored in the database. Please create an account and try again\n")
             if userInput == "b":
                print("----------------------------------------------------------------------------\n")
                AccountCreation(accountDatabase)
                print("-----------------------------Welcome to XXX bank----------------------------\n")
             if userInput == "c":
                 break
         else:
             print("Input is not valid, Please try again.\n")

    print("Thank you for enjoing the ATM and Banking System.")
    print("----------------------------------------------------------------------------\n\n\n")
    print("\n You have exited the program.")
    

        
    

    
        


mainLoop()

