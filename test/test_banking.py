import unittest
import os
import csv
from banking import *

class TestFunctions(unittest.TestCase):
        
    def setUp(self):
        self.bank = bank()
        self.saving_account = savingAccount()
        self.checking_account = checkingAccount()
    

    def test_1(self):
        #run deposit here
        self.saving_account.deposit(50,'00')
        #then do assert equals to check the balance has changed
        with open('bank.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['account_id'] == '00':
                 self.assertEqual(float(row['balance_savings']),900)
    def test_2(self):
        self.saving_account.withdraw(50,'00')
        with open('bank.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['account_id'] == '00':
                 self.assertEqual(float(row['balance_savings']),950)
    def test_3(self):
        self.saving_account.transfer_from_saving_to_checking(50,'00')
        with open('bank.csv','r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['account_id']=='00':
                    self.assertEqual(float(row['balance_checking']),650 )
    def test_4(self):    
        self.checking_account.deposit(50,'00')
        with open('bank.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['account_id'] == '00':
                 self.assertEqual(float(row['balance_checking']),700)
    def test_5(self):             
        self.checking_account.withdraw(100,'00')
        with open('bank.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['account_id'] == '00':
                 self.assertEqual(float(row['balance_checking']),600)
    def test_6(self):    
        self.checking_account.transfer_from_checking_to_saving(100,'00')
        with open('bank.csv','r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['account_id']=='00':
                    self.assertEqual(float(row['balance_savings']),1000 )
                    
    def test_7(self):
        
        self.bank.login('00', '123321')  
        self.assertTrue(True) 
        
        self.bank.login('00', '1111')  
        self.assertFalse(False)  

            
    
if __name__ == '__main__':
    unittest.main()