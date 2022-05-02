def show_balance(balance):
    print("Current Balance: $", balance)

def deposit(balance):
    amount_string = input("Enter amount to deposit:")
    amount = float(amount_string)
    updated_balance = balance + amount_string
    return updated_balance

def withdraw(balance):
    amount_string = input("Enter amount to withdraw:")
    amount = float(amount_string)
    updated_balance = balance + amount_string
    return updated_balance

def logout(name):
    print("Goodbye", name, "!")