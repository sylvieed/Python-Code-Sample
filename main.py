# File Name:   main.py
# Purpose:     Create an interface with the Bank Account classes (Savings & Checking),
#              for CS172 HW3
# Author:      Sylvie Daines
# Date:        January 31, 2023

from bank import Savings, Checking

def getAccount(accounts):
    """Helper method to attempt to find a bank account by its account number
       Returns None if no bank account is found

    Args:
        accounts (list of BankAccounts): the bank account list to search

    Returns:
        BankAccount: the bank account the user wants to access
    """
    accountNumber = getValidInput("Enter account number: ", True) 
    
    for account in accounts:
        if account.getAccountNumber() == accountNumber:
            return account
    
    return None

def getValidInput(prompt, integer=False):
    """ Gets a valid input from the user
        Will not return until the input is valid

    Args:
        prompt (String): What to prompt the user with when asking for input
        integer (bool, optional): Whether to check for an integer or float input. 
                                True: check for an integer. 
                                False: check for a float.
                                Defaults to False.

    Returns:
        int or float: The valid input from the user -- type depends on the integer argument
    """
    value = input(prompt)
    
    invalid = True
    while invalid: # Loop until the input is valid
        try:
            if integer:
                value = int(value)
            else:
                value = float(value)
        except ValueError: # The input was not an integer / float
            value = input("Invalid input: an " + ("integer" if integer else "float") + " value was expected. Try again: ")
        else: # The input was an integer / float
            # Check if the input was in the valid range (>= 0)
            if (value < 0): # The input was not in the valid range
                value = input("Enter a greater than or equal to zero: ")
            else: # The input was valid
                invalid = False
    return value

# Main routine
if __name__ == "__main__":
    # List of bank accounts
    accounts = []
    
    # Loop until the user exits
    cont = True
    while cont: 
        print("""
1. Create Savings Account
2. Create Checking Account
3. Deposit
4. Withdraw
5. Perform End of Month Operations
6. Display Savings Accounts
7. Display Checking Accounts
8. Display All Accounts
9. Exit""")
        
        choice = input("Enter your choice: ")
        
        print()
        if choice == "1": # Create a new Savings account
            print("Savings Account")
            
            owner = input("Enter owner's name: ") # Owner name doesn't need validation
            balance = getValidInput("Enter initial balance: ")
            
            savings = Savings(owner, balance)
            accounts.append(savings) 
            print("Account added")
            
        elif choice == "2": # Create a new Checking account
            print("Checking Account")

            owner = input("Enter owner's name: ") # Owner name doesn't need validation
            balance = getValidInput("Enter initial balance: ")
            
            # Create a new instance of the Checking account with the given input
            checking = Checking(owner, balance)
            accounts.append(checking) # Add this account to the list
            print("Account added")
            
        elif choice == "3": # Deposit money into an account
            print("Deposit")

            account = getAccount(accounts)
            if account is None: # No account with the inputted account number was found
                print("That account number does not exist")
            else: 
                amount = getValidInput("Enter amount to deposit: ")
                account.deposit(amount)
        
        elif choice == "4": # Withdraw money into an account
            print("Withdraw")
            account = getAccount(accounts)
            if account is None: # No account with the inputted account number was found
                print("That account number does not exist")
            else: 
                amount = getValidInput("Enter amount to withdraw: ")
                if (account.getBalance() > amount): 
                    account.withdraw(amount) 
                else: 
                    print("You do not have enough funds")
                    
        elif choice == "5": # Perform end of month operations
            for account in accounts:
                account.endOfMonth()
            print("End of month operations have been performed")
            
        elif choice == "6": # Display savings accounts
            for account in accounts:
                if isinstance(account, Savings): 
                    print(account)
                    
        elif choice == "7": # Display checking accounts
            for account in accounts:
                if isinstance(account, Checking): 
                    print(account)
            
        elif choice == "8": # Display all accounts
            for account in accounts:
                print(account)
        
        elif choice == "9": # Exit
            print("Good-bye!")
            # Stop looping
            cont = False
            
        else: # Not a valid input
            print("Invalid choice. Try again.")
