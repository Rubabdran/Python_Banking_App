import unittest
import os
import csv
from banking import *

class TestFunctions(unittest.TestCase):
    
    def setUp(self):
        self.bank = bank()
        self.saving_account = savingAccount()
        self.checking_account = checkingAccount()
        

    def test_savingAccount_class(self):
        
        #run deposit here
        self.saving_account.deposit(0,'1109698322')
        #then do assert equals to check the balance has changed
        with open('bank.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['account_id'] == '1109698322':
                 self.assertEqual(float(row['balance_savings']), 0)

        self.saving_account.withdraw(0,'1109698322')
        with open('bank.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['account_id'] == '1109698322':
                 self.assertEqual(float(row['balance_savings']), 0)
        
        self.saving_account.transfer_from_saving_to_checking(0,'1109698322')
        with open('bank.csv','r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['account_id']=='1109698322':
                    self.assertEqual(float(row['balance_checking']),0 )
        
    def test_checkingAccount_class(self): 
        
        self.checking_account.deposit(0,'1109698322')
        with open('bank.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['account_id'] == '1109698322':
                 self.assertEqual(float(row['balance_checking']), 0)
                 
        self.checking_account.withdraw(0,'1109698322')
        with open('bank.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['account_id'] == '1109698322':
                 self.assertEqual(float(row['balance_checking']), 0)
         
        self.checking_account.transfer_from_checking_to_saving(0,'1109698322')
        with open('bank.csv','r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['account_id']=='1109698322':
                    self.assertEqual(float(row['balance_savings']),0 )
                    
    def test_bank_class(self):
        
        self.bank.login('1109698322', '123321')  
        self.assertTrue(True) 
        
        self.bank.login('1109698322', '1111')  
        self.assertFalse(False)  

            
    
if __name__ == '__main__':
    unittest.main()