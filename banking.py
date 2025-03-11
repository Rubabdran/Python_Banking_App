import csv
import os

#overdraft 
#link the transaction methods with my csv 
#build history class 
#transfer choice in main  

#------------------------ CSV ----------------------#

def initialize_bank():
    bank_info = [
        {'account_id': '10001', 'first_name': 'suresh', 'last_name': 'sigera', 'password': 'juagw362','account_type':'both', 'balance_checking': 1000, 'balance_savings': 10000},
        {'account_id': '10002', 'first_name': 'james', 'last_name': 'taylor', 'password': 'idh36%@', 'account_type':'both','balance_checking': 1000, 'balance_savings': 10000},
        {'account_id': '10003', 'first_name': 'melvin', 'last_name': 'gordon', 'password': 'uYWE732g4ga1', 'account_type':'both', 'balance_checking': 2000, 'balance_savings': 20000},
        {'account_id': '10004', 'first_name': 'stacey', 'last_name': 'abrams', 'password': 'DEU8_qw3y72','account_type':'both', 'balance_checking': 2000, 'balance_savings': 20000},
        {'account_id': '10005', 'first_name': 'jake', 'last_name': 'paul', 'password': 'd^dg23g@','account_type':'both', 'balance_checking': 100000, 'balance_savings': 100000}
    ]
    fieldnames = ['account_id', 'first_name', 'last_name', 'password', 'account_type', 'balance_checking', 'balance_savings']
    if not os.path.exists("bank.csv"):
        with open("bank.csv", 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in bank_info:
                writer.writerow(row)

initialize_bank()

#------------------------ Classes ----------------------#

# BANK CLASS CONTAIN CREATE ACCOUNT, LOGIN, LOGOUT, DISPLAY INFO 
class bank :
    def __init__(self):
        self.fieldnames = ['account_id', 'first_name', 'last_name', 'password','account_type', 'balance_checking', 'balance_savings']

    
    def create_account(self, account_id, first_name, last_name, password, account_type):
        with open('bank.csv', "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == account_id:
                    print("Account ID already exists.")
                    return
        
        with open('bank.csv', "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([account_id, first_name, last_name, password, account_type, 0 , 0])
            print("Account created successfully!")
        
    def login(self, account_id, password):
        with open('bank.csv', "r") as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                if row[0] == account_id and row[3] == password:
                    print("welcome !")
                    return row   
            print("Invalid login.")
                    
    def logout(self):
        print("Logged out")
        
    def view_info(self, account_id):
        with open('bank.csv', "r") as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                if row[0] == account_id:
                    print("Account Information:")
                    print(f"ID: {row['account_id']}")
                    print(f"Name: {row['first_name']} {row['last_name']}")
                    print(f"Checking Balance: {row['balance_checking']}")
                    print(f"Savings Balance: {row['balance_savings']}")
                    return 

# SAVING CLASS CONTAIN DEPOSIT, WITHDRAW, TRANSFER
class savingAccount :
    def __init__(self, account_id, first_name, last_name, password,account_type, balance_savings=0):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.account_type=account_type
        self.balance_savings = float(balance_savings)
    
    def deposit(self, amount):
        self.balance_savings += amount
    
    def withdraw(self, amount):
        if self.balance_savings >= amount:
            self.balance_savings -= amount
        else:
            return "can't withdraw"
    
    def transfer(self, amount, to_this_account):
        pass
        # if self.balance_savings >= amount:
        #    self.balance_savings -= amount
        #    to_this_account.deposit(amount)
        # else:
        #     return "can't transfer"
  
# CHECKING CLASS CONTAIN DEPOSIT, WITHDRAW, TRANSFER
class checkingAccount :
    def __init__(self, account_id, first_name, last_name, password,account_type, balance_checking=0):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.account_type=account_type
        self.balance_checking = float(balance_checking)
    
    def deposit(self, amount):
        self.balance_checking += amount
    
    def withdraw(self, amount):
        if self.balance_checking >= amount:
            self.balance_checking -= amount
        else:
            return "can't withdraw"
    
    def transfer(self, amount, to_this_account):
        pass
        # if self.balance_checking >= amount:
        #    self.balance_checking -= amount
        #    to_this_account.deposit(amount)
        # else:
        #     return "can't transfer"

#BONUS 
class history :
    pass # not yet

#------------------------ Command Line Interface ----------------------#

if __name__ == "__main__":
    
        ob=bank()
        ob2=savingAccount()
        ob3= checkingAccount()
        
        print("________________________________")
        print("")
        print(" WELCOME TO OUR BANKING SYSTEM ")
        print("________________________________")
        
        print("********************************")
        print("*                              *")
        print("*     1. Create Account        *")
        print("*     2. Login                 *")
        print("*                              *")
        print("********************************")

        
        choice_p1 = input("Enter choice: ")
        
        if choice_p1 == "1":
            print("********************************")
            print("*                              *")
            print("*     Choose account type:     *")
            print("*     1. Savings Account       *")
            print("*     2. Checking Account      *")
            print("*     3. Both                  *")
            print("*                              *")
            print("********************************")
            choice_p2 = input("Enter choice: ")
            account_type = "savings" if choice_p2 == "1" else "checking" if choice_p2 == "2" else "both"
            
            account_id = input("Enter account ID: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            password = input("Enter password: ")
            ob.create_account(account_id, first_name, last_name, password, account_type)
            
        elif choice_p1== "2":
            
            account_id = input("Enter account ID: ")
            password = input("Enter password: ")
            login = ob.login(account_id, password)
            if login:
                print("********************************")
                print("*                              *")
                print("*         1. Deposit           *")
                print("*         2. Withdraw          *")
                print("*         3. Transfer          *")
                print("*         4. View Account      *")
                print("*         5. Exit              *")
                print("*                              *")
                print("********************************")
                
                choice_p3 = input("Enter choice: ")
                if choice_p3 == "1":
                    amount = float(input("Enter amount: "))
                    saving_or_checking = input("Enter 1 to deposit in savings or 2 to deposit in checking : ")
                    if saving_or_checking == "1":
                        ob2.deposit(amount)
                    elif saving_or_checking == "2":
                        ob3.deposit(amount)
                        
                elif choice_p3=="2":
                    amount = float(input("Enter amount: "))
                    saving_or_checking = input("Enter 1 to withdraw from savings or 2 to withdraw from checking : ")
                    if saving_or_checking == "1":
                        ob2.withdraw(amount)
                    elif saving_or_checking == "2":
                        ob3.withdraw(amount)
                
                elif choice_p3=="3":
                    pass    # not yet
                    
                elif choice_p3 =="4":
                    ob.view_info(account_id)
                elif choice_p3 =="5":
                    ob.logout()
                    