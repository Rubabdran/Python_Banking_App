import csv 

class bank:
     
    def __init__(self):
        self.is_logged_in = False  
        self.logged_in_user_id = ""
        self.fieldnames = ['account_id', 'first_name', 'last_name', 'password', 'balance_checking', 'balance_savings']

    def add_account(self):
        account_id = input("Enter your ID: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        password = input("Enter password: ")
        
    
        account_type = input("Choose account type: (1) Checking (2) Savings (3) Both: ")
        if account_type == "1":
            balance_checking = 0
            balance_savings = "Null"
                
        elif account_type == "2":
            balance_checking = "Null"
            balance_savings = 0
                
        elif account_type == "3":
            balance_checking = 0
            balance_savings = 0
               
                
        with open('bank.csv', "r", newline="") as file:
            contents = csv.DictReader(file)
            for row in contents:
                if row["account_id"] == account_id:
                    print("You already have an account.")
                    return  
        
        with open('bank.csv', 'a+', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writerow({'account_id': account_id, 'first_name': first_name, 'last_name': last_name, 'password': password, 'balance_checking': balance_checking, 'balance_savings': balance_savings})
            print("added account successfully.")

    def login(self):
        account_id = input("Enter yoyr ID: ")
        password = input("Enter password: ")
        
        with open('bank.csv', "r", newline="") as file:
            contents = csv.DictReader(file)
            for row in contents:
                if row["account_id"] == account_id and row["password"] == password:
                    print("Welcome!")
                    self.is_logged_in = True  
                    self.logged_in_user_id = account_id
                    return
                
        print("Invalid ID or password! Please try again.")

    def logout(self):
        if self.is_logged_in:
            print("Goodbye !")
            self.is_logged_in = False 
    
    def display_info(self):
        if self.is_logged_in:
            with open('bank.csv', "r", newline="") as file:
                contents = csv.DictReader(file)
                for row in contents:
                    if row["account_id"] == self.logged_in_user_id:
                        print("Account Information:")
                        print(f"ID: {row['account_id']}")
                        print(f"Name: {row['first_name']} {row['last_name']}")
                        print(f"Checking Balance: {row['balance_checking']}")
                        print(f"Savings Balance: {row['balance_savings']}")
                        return 
        else:
            print("Please log in first.")
            
            
class bankAccount:
    def deposit():
        pass
    
    def withdraw():
        pass
    
    def transfer():
        pass  
    
class checkingAccount(bankAccount):
    pass

class savingAccount(bankAccount):
    pass

class history:
    pass


#--------------------main------------------#

# Usage
# bank_account = bank("", "", "", "")
# bank_account.addAccount()
bank_account = bank()
bank_account.add_account()
bank_account.login()
bank_account.display_info()