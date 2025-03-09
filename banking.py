import csv 

class bankAccount:
    def __init__(self,account_id,first_name,last_name,password):
        self.account_id=account_id
        self.first_name=first_name
        self.last_name=last_name
        self.password=password
    
    def addAccount(self, account_id, first_name, last_name, password, balance_checking=0, balance_savings=0):
         fieldnames = ['account_id', 'first_name', 'last_name', 'password', 'balance_checking', 'balance_savings']
         
         with open('bank.csv', "r", newline="") as file:
            contents = csv.DictReader(file)
            for row in contents:
                if row["account_id"] == str(account_id):
                     print(" You are already have account .")
    
         with open('bank.csv', 'a+', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'account_id': account_id,'first_name': first_name,'last_name': last_name,'password': password,'balance_checking': balance_checking,'balance_savings': balance_savings})
            print(f"Customer {first_name} added successfully.")
    
    def login():
        pass
    
    def logout():
        pass
    
    def authenticate():
        pass 
    
    
cust = bankAccount('1009', 'ruba', 'alharbi', 123321)
cust.addAccount('1009', 'ruba', 'alharbi', 123321, 0, 0)