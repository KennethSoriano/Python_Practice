from multiprocessing.sharedctypes import Value


class User:
    def __init__(self, name, pin, password):
        self.value = Value
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password

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

    def show_balance(self):
        print(self.name, "has an account balance of: ", self.balance)

    def withdraw(self, withdrawal):
        self.withdrawal = withdrawal
        self.balance -= withdrawal

    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.balance += deposit_amount

""" Driver Code for Task 3
bankuser1 = BankUser("Bob", "1234", "password")
print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)
"""

bankuser1 = BankUser("Bob", "1234", "password")
print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)
print(bankuser1.show_balance())
bankuser1.deposit(1000)
print(bankuser1.show_balance())
bankuser1.withdraw(500)
print(bankuser1.show_balance())