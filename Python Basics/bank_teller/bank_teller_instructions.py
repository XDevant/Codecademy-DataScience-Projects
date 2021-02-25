#!/usr/bin/env python
# coding: utf-8

# Bank Teller

# In this project you will be implementing code that emulates transactions performed between a bank-teller and a customer. 

# The prerequisites for this project are Python 3 syntax, functions and control flow. Let's jump right into it!

#1. Initializing savings and checking account values. 
# Creates two variables, one named `checking_balance` and the other `savings_balance`. Assign them both the value of zero. Use these as your starting bank balances.

checking_balance = 0
savings_balance =0


# ### 2. Create a function to check the Balance

def check_balance(account_type, checking_balance, savings_balance):
    if account_type == "savings":
        balance = savings_balance
    elif account_type == "checking":
        balance = checking_balance
    else:
        return 'Unsuccessful, please enter \"checking\" or \"savings\"'
    balance_statement = "Your {account_type} balance is {balance}$".format(account_type=account_type, balance = str(balance))
    return balance_statement


# 3. Calling and Printing the check_balance() function for Checking Account

print(check_balance("checking", checking_balance, savings_balance))

# 4. Calling and Printing the check_balance() function for Savings Account

print(check_balance("savings", checking_balance, savings_balance))

# 5. Create a function to make a deposit

def make_deposit(account_type, amount, checking_balance, savings_balance):
    deposit_status = ''
    if amount > 0:
        if account_type == "savings":
            savings_balance += amount
            deposit_status = "successful"
        elif account_type == "checking":
            checking_balance += amount
            deposit_status = "successful"
        else:
            deposit_status = 'Unsuccessful, please enter \"checking\" or \"savings\"'
    else:
        deposit_status = "unsuccessful, please enter an amount greater than 0"
    deposit_statement = "Deposit of {amount}$ to your {account_type} account was {deposit_status}".format(amount = str(amount), account_type = account_type, deposit_status = deposit_status)
    print(deposit_statement)
    return checking_balance, savings_balance


# 6. Call deposit function and make a savings deposit

checking_balance, savings_balance = make_deposit("savings", 10,checking_balance, savings_balance)


# 7. Print savings balance call after making a savings deposit

print(check_balance("savings", checking_balance, savings_balance))


# 8. Call deposit function and make a checking deposit

checking_balance, savings_balance = make_deposit("checking", 200,checking_balance, savings_balance)


#9. Print checking balance call after making a checking deposit

print(check_balance("checking", checking_balance, savings_balance))


# 10. Create a function to make a withdrawal

def make_withdrawal(account_type, amount, checking_balance, savings_balance):
    withdrawal_status = ""
    fail = "Unsuccessful, please enter amount less than balance"
    if account_type == "savings":
        if amount <= savings_balance:
            savings_balance -= amount
            withdrawal_status = "successful"
        else:
            withdrawal_status = fail
    elif account_type == "checking":
        if amount <= checking_balance:
            checking_balance -= amount
            withdrawal_status = "successful"
        else:
            withdrawal_status = fail
    else:
        withdrawal_status = "unsuccessful, please enter \"checking\" or \"savings\""
    withdrawal_statement = "Withdrawal of {amount} dollars from your {account_type} was {withdrawal_status}".format(amount=str(amount), account_type=account_type, withdrawal_status=withdrawal_status)
    print(withdrawal_statement)
    return checking_balance, savings_balance


# ### 11. Call withdrawal function and make a savings withdrawal

checking_balance, savings_balance = make_withdrawal("savings", 11,checking_balance, savings_balance)


# ### 12. Print savings balance call, after making a savings withdrawal

print(check_balance("savings", checking_balance, savings_balance))


#13. Call withdrawal function and make a checking withdrawal

checking_balance, savings_balance = make_withdrawal("checking", 170,checking_balance, savings_balance)


#14. Print checking balance call, after making a checking withdrawal

print(check_balance("checking", checking_balance, savings_balance))


# 15. Create a function to make a transfer between accounts

def acc_transfer(acc_from, acc_to, amount, checking_balance, savings_balance):
    trans_status = ''
    trans_error = "unsuccessful, please enter amount less than "
    if acc_from == "savings" and acc_to == "checking":
        if amount <= savings_balance:
            savings_balance -= amount
            checking_balance += amount
            trans_status = "successful"
        else:
            trans_status = trans_error + str(savings_balance)
    elif acc_from == "checking" and acc_to == "savings":
        if amount <= checking_balance:
            checking_balance -= amount
            savings_balance += amount
            trans_status = "successful"
        else:
            trans_status = trans_error + str(checking_balance)
    else:
        trans_status = "unsuccessful, please enter \"checking\" or \"savings\""
    trans_statement = "transfer of {amount}$ from your {acc_from} to your {acc_to} account was {trans_status}".format(amount=str(amount), acc_from=acc_from, acc_to=acc_to, trans_status=trans_status)
    print(trans_statement)
    return checking_balance, savings_balance
    


#16. Call transfer function and make a checking to savings transfer

checking_balance, savings_balance = acc_transfer("checking", "savings", 40,checking_balance, savings_balance)

# 17. Print checking balance after making a checking to savings transfer

print(check_balance("checking", checking_balance, savings_balance))

# 18. Print savings balance after making a checking to savings transfer

print(check_balance("savings", checking_balance, savings_balance))

# 19. Call transfer function and make a savings to checking transfer

checking_balance, savings_balance = acc_transfer("savings", "checking", 5,checking_balance, savings_balance)

# 20. Print checking balance after making a savings to checking transfer

print(check_balance("checking", checking_balance, savings_balance))

# 21. Print saving balance after making a savings to checking transfer

print(check_balance("savings", checking_balance, savings_balance))






