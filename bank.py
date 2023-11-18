# File Name:   bank.py
# Purpose:     Create a super class to represent a bank account with an owner, balance, and account number,
#              and two child classes to represent Savings and Checking accounts,
#              for CS172 HW3
# Author:      Sylvie Daines
# Date:        January 31, 2023

from abc import ABC, abstractmethod

# Abstract class to represent a Bank account
# with an owner (String), balance (float), account number (int)
class BankAccount(ABC):
    # Static attribute to keep track of account numbers for all bank accounts
    __nextAccountNumber = 1000
    
    def __init__(self, owner, balance = 0.0):
        self.__owner = owner
        self.__balance = balance
        self.__accountNumber = BankAccount.__nextAccountNumber
        BankAccount.__nextAccountNumber += 1
        
    def getOwner(self):
        return self.__owner
    
    def getBalance(self):
        return self.__balance
    
    def getAccountNumber(self):
        return self.__accountNumber

    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if self.__balance >= amount: 
            self.__balance -= amount
        else: 
            raise Exception("Not enough funds to withdraw")
        
    def __eq__(self, other):
        return self.__owner == other.__owner and self.__balance == other.__balance and self.__accountNumber == other.__accountNumber
    
    def __str__(self):
        str  = "Account Number: %s\n" % self.__accountNumber
        str += "Account Owner: %s\n" % self.__owner
        str += "Account Balance: $%.2f" % self.__balance # Two decimal places
        return str
    
    @staticmethod
    def getNextAccountNumber():
        return BankAccount.__nextAccountNumber
    
    @abstractmethod
    def endOfMonth(self):
        pass
    
# Class to represent a Savings Account
# Child of the Bank Account class
# Also has an interest rate
class Savings(BankAccount):

    def __init__(self, owner, balance=0.0, interestRate = 3.25):
        super().__init__(owner, balance) 
        self.__interestRate = interestRate
        
    def getInterestRate(self):
        return self.__interestRate
    
    def setInterestRate(self, interestRate):
        self.__interestRate = interestRate
        
    def __eq__(self, other):
        return super().__eq__(other) and self.__interestRate == other.__interestRate
    
    def __str__(self):
        str  = super().__str__() 
        str += "\nAnnual Interest Rate: %.2f%%" % self.__interestRate
        return str
    
    # Runs end of month operations (adding interest)
    def endOfMonth(self):
        # interest rate is annual and a percent instead of decimal, so needs to be divided by 12 and 100, respectively
        # Interest is balance times adjusted interest rate
        interest = self.getBalance() * (self.getInterestRate()/100 / 12)
        self.deposit(interest)
        
# Bank Account that keeps track of transactions per month
class Checking(BankAccount):

    def __init__(self, owner, balance=0.0):
        super().__init__(owner, balance) 
        self.__transactions = 0 
        
    # Get number of transactions in the account for this month
    def getTransactionsNum(self):
        return self.__transactions

    def deposit(self, amount):
        super().deposit(amount) 
        self.__transactions += 1 
        
    def withdraw(self, amount):
        super().withdraw(amount)
        self.__transactions += 1
        
    def __eq__(self, other):
        super().__eq__(other) and self.__transactions == other.__transactions
        
    def __str__(self):
        str  = super().__str__()
        str += "\nTransactions this month: %s" % self.__transactions
        return str

    def endOfMonth(self):
        if (self.__transactions > 7): # If number of transactions is more than 7
            self.withdraw(5.0) # $5 service fee 
        # Reset number of transactions
        self.__transactions = 0 
