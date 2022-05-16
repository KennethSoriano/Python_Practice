from multiprocessing.sharedctypes import Value


class User:
    def __init__(self, name, pin, password):
        self.value = Value
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password

""" Driver Code for Task 1 

user1 = User("Bob", "1234", "Password")
print(user1.name, user1.pin, user1.password)

"""


""" Driver Code for Task 2 
user1 = User("Bob", "1234", "Password")
print(user1.name, user1.pin, user1.password)

user1.change_name("Bobby")
user1.change_pin("4321")
user1.change_password("newpassword")
print(user1.name, user1.pin, user1.password)
"""

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        self.on_hold = False

    def show_balance(self):
        print(f"{self.name} has an account balance of: ${self.balance:.2f}")

    def withdraw(self, amount):
        if self.on_hold:
            print("Account on hold. Transaction Canceled.")
            return False

        if self.balance < amount:
            print("amount is greater than account balance. Canceling Transaction.")
            return False

        self.balance -= amount
        return True
        

    def deposit(self, amount):
        if self.on_hold:
            print("Account on hold. Transaction Canceled.")
            return False

        if amount < 0.01:
            print("Amount must be greater than or equal to one penny.")
            return False

        self.balance += amount
        return True
    
    def toggle_hold(self):
        if self.on_hold:
            self.on_hold = False
        else:
            self.on_hold = True

    def transfer_money(self, other_user, transfer_amount):

        if self.on_hold or other_user.on_hold:
            print("One or more user's accounts are on hold. Transaction Canceled.")
            return False

        print(f"{self.name} is transferring ${transfer_amount:.2f} to {other_user.name}")
        print()
        print("AUTHENTICATION REQUIRED")
        user_pin = int(input("User Pin: "))

        if user_pin != self.pin:
            print("Invalid PIN. Transaction Canceled.")
            return False

        print("Transfer Authorized...")
        print(f"Transferring ${transfer_amount:.2f} to {other_user.name}")
        self.balance -= transfer_amount
        other_user.balance += transfer_amount
        return True

    def request_money(self, user, amount):
        print()

        if self.on_hold or user.on_hold:
            print("One or more user's accounts are on hold. Transaction Canceled.")
            return False

        print(f"{self.name} is requesting ${amount:.2f} from {user.name}.")
        print(f"WE NEED TO AUTHENTICATE: {user.name}")
        pin = int(input(f"Enter {user.name}'s pin: "))

        if pin != user.pin:
            print("Invalid PIN. Transaction Canceled.")
            return False

        password = input(f"Enter {self.name}'s password: ")
        if password != self.password:
            print("Invalid Password. Transaction Canceled.")
            return False

        print("Request Authorized...")
        print(f"{user.name} has transferred ${amount:.2f} to {self.name}.")

        user.balance -= amount
        self.balance += amount

        return True   

            

""" Driver Code for Task 3
bankuser1 = BankUser("Bob", "1234", "password")
print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)


bankuser1 = BankUser("Bob", "1234", "password")
print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)
print(bankuser1.show_balance())
bankuser1.deposit(1000)
print(bankuser1.show_balance())
bankuser1.withdraw(500)
print(bankuser1.show_balance())
"""

if __name__ == '__main__':
    new_user = BankUser("Kenneth", 1234, "Hello")

    print(new_user.name, new_user.balance)
    new_user.deposit(0.01)
    new_user.toggle_hold()
    new_user.withdraw(10)

    other_user = BankUser("Bill", 1234, "Hello")

    print(other_user.name, other_user.balance)
    other_user.deposit(100)
    other_user.withdraw(20)

    print()
    new_user.show_balance()
    other_user.show_balance()

    print("\n")

    transfer_bool = other_user.transfer_money(new_user, 40.25)
    if transfer_bool:
        new_user.show_balance()
        other_user.show_balance()

    print()

    request_bool = other_user.request_money(new_user, 0.25)
    if request_bool:
        new_user.show_balance()
        other_user.show_balance()
