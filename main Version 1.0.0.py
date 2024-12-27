accountDatabase = []

class Account:
    def __init__(self, accountNumber, name, initialDeposit):
        self.accountNumber = accountNumber
        self.FirstName, self.MiddleInitial, self.Surname = name
        self.currentBalance = initialDeposit #Because at creation, your current balance is the one you started with
        

    def GetName(self):
        return " ".join(list((self.FirstName, self.MiddleInitial, self.Surname))) #returns string

    def GetAccountNumber(self):
        return self.accountNumber #Returns string

    def GetCurrentBalance(self):
        return self.currentBalance #Returns int

    def SetCurrentBalance(self, value):
        self.currentBalanca += value # For Subtraction, set value as negative ( -100 ) so that currentBalance += (-100)


#Creates Account
def AccountCreation(accountDatabase):
    print("------------Welcome to Account Creation!------------\n")

    accountNumber = str(len(accountDatabase) + 100000)

    #Error handling in names aka John123 Smith69
    while True:
        name = [input("Enter your First Name: \n"),
                input("Enter your Middle Initial: \n"),
                input("Enter your Surname: \n")]
        if not any(names.isalpha() for names in name):
            print("You have entered an invalid name, Please try again.")
        else:
            while True:
                confirm = input(f"Your name is {name[0]} {name[1]} {name[2]}. Confirm? Yes or No\n").lower()

                if confirm == "yes" or confirm == "no":
                    break
                else:
                    print("Invalid input, please try again.")
                    
            if confirm == "yes":
                break

    while True:
        initialDeposit = input("Enter initial deposit: \n")

        if not initialDeposit.isdigit():
            print("Enter a proper value. Please try again.\n")
        else:
            break

    #Creating new account object
    newAccount = Account(accountNumber, name, initialDeposit)

    #Appending new account to the database
    accountDatabase.append(newAccount)

    print("Congratulations, you have created your account, Logging in.... \n\n")

    #Actual Logging in
    AccountStatusInterface(accountDatabase, len(accountDatabase)-1)

        
#Login to account
def Login(accountDatabase):
    print("------------Log in Page------------\n")
    while True:
        accountNumber = input("Enter your account number or enter exit to exit: ")

        if accountNumber.lower() == "exit":
            break
        for account in accountDatabase:
            if accountNumber == account.GetAccountNumber():
                AccountStatusInterface(accountDatabase, accountDatabase.index(account))
                break
        if not any(accountNumber == account.GetAccountNumber() for account in accountDatabase):
            print("Invalid input. Please try again.")
        else:
            break
        
def AccountStatusInterface(accountDatabase, accountIndex):
    print("------------Welcome to your Account Page------------\n")

    while True:
        print(f"Account Name: {accountDatabase[accountIndex].GetName()}")
        print(f"Account Number: {accountDatabase[accountIndex].GetAccountNumber()}")
        print(f"Account Balance: {accountDatabase[accountIndex].GetCurrentBalance()}\n")

        while True:
            #Here iinsert ang options for withdrawal, fund transfer, all transaction history etc.. add nyo lang sa userInput ung options (b, c, etc....) and lagay nyo rin ung letter sa options list in lowercase

            options = ["a","d"] # add option here
            
            userInput = input("What would you like to do?\n" +
                              "A. Other\n" +
                              "D. Exit\n").lower()
            if any(userInput == option for option in options):
                break
            else:
                print("Invalid Input. Please try again")

        #if user chose to quit
        if userInput == "d":
            break

def mainLoop():
    print("------------Welcome to XXX bank------------\n")

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
                    Login(accountDatabase)
                    print("------------Welcome to XXX bank------------\n")
                else:
                    print("There are no accounts stored in the database. Please create an account and try again\n")
             if userInput == "b":
                AccountCreation(accountDatabase)
                print("------------Welcome to XXX bank------------\n")
             if userInput == "c":
                 break
         else:
             print("Input is not valid, Please try again.\n")
            
    print("\n You have exited the program.")
    

        
    

    
        


mainLoop()
