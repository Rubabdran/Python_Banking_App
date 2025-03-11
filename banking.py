import csv
import os 

#-----to do----#
#reactivate the account when balance>=0
#transfer function and main  
#build history class 
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
         reader = csv.DictReader(file)
         for row in reader:
            if row['account_id'] == account_id and row['password'] == password:
                checking_balance = float(row['balance_checking'])
                savings_balance = float(row['balance_savings'])
                if checking_balance < 0 or savings_balance < 0:
                    print("Your account is inactive .")
                    print("Please deposit enough money to reactivate your account.")
                else:
                    print("Welcome!")
                return row
                    
    def logout(self):
        print("Logged out")
        
    def view_info(self, account_id):
        with open('bank.csv', "r") as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                if row[0] == account_id:
                 print("Account Information:")
                 print(f"ID: {row[0]}")
                 print(f"Name: {row[1]} {row[2]}")
                 print(f"Checking Balance: {row[5]}")
                 print(f"Savings Balance: {row[6]}")
                 return

# SAVING CLASS CONTAIN DEPOSIT, WITHDRAW, TRANSFER
class savingAccount :
    def __init__(self):
         self.fieldnames = ['account_id', 'first_name', 'last_name', 'password','account_type', 'balance_checking', 'balance_savings']
    
    def deposit(self, amount ,account_id ):
        self.account_id=account_id
        rows = []
        with open('bank.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['account_id'] == self.account_id:
                    self.balance_savings = float(row['balance_savings']) 
                    self.balance_savings += amount 
                    row['balance_savings'] = str(self.balance_savings)  
                rows.append(row)
        with open('bank.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(rows)   
    
    def withdraw(self, amount,account_id):
        self.account_id=account_id
        rows = []
        with open('bank.csv', 'r') as file:
         reader = csv.DictReader(file)
         for row in reader:
            if row['account_id'] == self.account_id:
                self.balance_savings = float(row['balance_savings'])
                
                if self.balance_savings >= amount:
                    self.balance_savings -= amount
                    row['balance_savings'] = str(self.balance_savings)
                elif self.balance_savings < 0 and amount > 100:
                    print("Can't withdraw more than $100 when account balance is negative.") 
                elif self.balance_savings >= amount and amount > 100:
                    print("Can't withdraw more than $100 in one transaction.")    
                else:#overdraft
                    if (self.balance_savings - amount) < 0 and (self.balance_savings - amount - 35) > -100:
                        self.balance_savings -= amount
                        row['balance_savings'] = str(self.balance_savings)
                                             
            rows.append(row)
        with open('bank.csv', 'w', newline='') as file:
         writer = csv.DictWriter(file, fieldnames=self.fieldnames)
         writer.writeheader()
         writer.writerows(rows)
    
    def transfer(self, amount, to_this_account):
        pass

# CHECKING CLASS CONTAIN DEPOSIT, WITHDRAW, TRANSFER
class checkingAccount :
    def __init__(self):
         self.fieldnames = ['account_id', 'first_name', 'last_name', 'password','account_type', 'balance_checking', 'balance_savings']
    
    def deposit(self, amount, account_id):
        self.account_id = account_id
        
        rows = []
        with open('bank.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['account_id'] == self.account_id:
                    self.balance_checking = float(row['balance_checking']) 
                    self.balance_checking += amount 
                    row['balance_checking'] = str(self.balance_checking)  
                rows.append(row)
        with open('bank.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(rows)
            
    def withdraw(self, amount, account_id):
        self.account_id=account_id
        rows = []
        with open('bank.csv', 'r') as file:
         reader = csv.DictReader(file)
         for row in reader:
            if row['account_id'] == self.account_id:
                self.balance_checking = float(row['balance_checking'])
                if self.balance_checking >= amount:
                    self.balance_checking -= amount
                    row['balance_checking'] = str(self.balance_checking)
                elif self.balance_checking < 0 and amount > 100:
                    print("Can't withdraw more than $100 when account balance is negative.") 
                elif self.balance_checking >= amount and amount > 100:
                    print("Can't withdraw more than $100 in one transaction.")    
                else:#overdraft
                    if (self.balance_checking - amount) < 0 and (self.balance_checking - amount - 35) > -100:
                        self.balance_checking -= amount
                        row['balance_checking'] = str(self.balance_checking)
              
            rows.append(row)
        with open('bank.csv', 'w', newline='') as file:
         writer = csv.DictWriter(file, fieldnames=self.fieldnames)
         writer.writeheader()
         writer.writerows(rows)
         
    def transfer(self, amount, to_this_account):
        pass
    
#BONUS 
class history :
    pass # not yet

#------------------------ Command Line Interface ----------------------#

if __name__ == "__main__":
    
        ob=bank()
        ob2=savingAccount()
        ob3=checkingAccount()
        
        print("________________________________")
        print("")
        print(" WELCOME TO OUR BANKING SYSTEM "+"\U0001F600")
        print("________________________________")
        
        print("********************************")
        print("*                              *")
        print("*     1. Create Account        *")
        print("*     2. Login                 *")
        print("*                              *")
        print("********************************")

        
        choice_p1 = input("Enter choice: \U0001F31F ")
        
        if choice_p1 == "1":
            print("********************************")
            print("*                              *")
            print("*     Choose account type:     *")
            print("*     1. Savings Account       *")
            print("*     2. Checking Account      *")
            print("*     3. Both                  *")
            print("*                              *")
            print("********************************")
            choice_p2 = input("Enter choice: \U0001F31F ")
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
                
                choice_p3 = input("Enter choice: \U0001F31F ")
                if choice_p3 == "1":
                    amount = float(input("Enter amount: "))
                    saving_or_checking = input("Enter 1 to deposit in savings or 2 to deposit in checking : ")
                    if saving_or_checking == "1":
                        ob2.deposit(amount,account_id)
                    elif saving_or_checking == "2":
                        ob3.deposit(amount,account_id)
                        
                elif choice_p3=="2":
                    amount = float(input("Enter amount: "))
                    saving_or_checking = input("Enter 1 to withdraw from savings or 2 to withdraw from checking : ")
                    if saving_or_checking == "1":
                        ob2.withdraw(amount,account_id)
                    elif saving_or_checking == "2":
                        ob3.withdraw(amount,account_id)
                
                elif choice_p3=="3":
                    pass    # not yet
                    
                elif choice_p3 =="4":
                    ob.view_info(account_id)
                elif choice_p3 =="5":
                    ob.logout()
                    