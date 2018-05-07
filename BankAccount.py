class BankAccount:
    def __init__(self,first_name,last_name,middle_name,account_type,balance,status):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.account_type = account_type
        self.balance = balance
        self.status = status

    def open_account(self):
        userInput = int(input("Please enter your initial deposit amount: "))
        if userInput >= 100:
            print(f"{self.first_name} {self.last_name} can open an account!")
        else:
            print(f"{self.first_name}, you cannot open an account due to insufficient funds")

    def account_transfer(self,toAccount):
        userInput = int(input(f"Please enter amount to transfer to {toAccount.account_type}: "))
        toAccount.balance = toAccount.balance + userInput
        print(f"{self.first_name}, your new balance for your {self.account_type} account is: ${self.balance - userInput}.")
        print(f"Your new balance for your {toAccount.account_type} account is: ${toAccount.balance}")

    def withdraw(self):
        userInput = int(input(f"Please enter the amount to be withdrawn: "))
        self.balance = self.balance - userInput
        print(f"{self.first_name}, your new balance is: ${self.balance}.")

    def overdraft(self):
        if self.balance <= 0:
            self.balance = self.balance - 35
            print(f"You do not have enough funds, you will be charged an overdraft fee of $35")
            print(f"{self.first_name}, your new balance is: ${self.balance}")

micah = BankAccount('Micah','Finley','Jay','Checking',105,'Opened')
micah2 = BankAccount('Micah','Finley','Jay','Savings',250,'Opened')

#micah.open_account()
#micah.account_transfer(micah2)
#micah.withdraw()
#micah.overdraft()
