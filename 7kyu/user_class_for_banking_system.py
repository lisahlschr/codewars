# A company is opening a bank, but the coder who is designing the user class made some errors. They need you to help them.

# You must include the following:
# Note: These are NOT steps to code the class

#     A withdraw method
#         Subtracts money from balance
#         One parameter, money to withdraw
#         Raise a ValueError if there isn't enough money to withdraw
#         Return a string with name and balance(see examples)

#     A check method
#         Adds money to balance
#         Two parameters, other user and money
#         Other user will always be valid
#         Raise a ValueError if other user doesn't have enough money
#         Raise a ValueError if checking_account isn't true for other user
#         Return a string with name and balance plus other name and other balance(see examples)

#     An add_cash method
#         Adds money to balance
#         One parameter, money to add
#         Return a string with name and balance(see examples)

# Additional Notes:

#     Checking_account should be stored as a boolean

#     No input numbers will be negative

#     Output must end with a period

#     Float numbers will not be used so, balance should be integer

#     No currency will be used

# Examples:
# Jeff = User('Jeff', 70, True)
# Joe = User('Joe', 70, False)

# Jeff.withdraw(2) # Returns 'Jeff has 68.'

# Joe.check(Jeff, 50) # Returns 'Joe has 120 and Jeff has 18.'

# Jeff.check(Joe, 80) # Raises a ValueError

# Joe.checking_account = True # Enables checking for Joe

# Jeff.check(Joe, 80) # Returns 'Jeff has 98 and Joe has 40'

# Joe.check(Jeff, 100) # Raises a ValueError

# Jeff.add_cash(20.00) # Returns 'Jeff has 118.'

#My Solution:
class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, money_withdraw):
        self.money_withdraw = money_withdraw
        if int(self.balance - self.money_withdraw) > 0:
            self.balance = self.balance - self.money_withdraw
            return f"{self.name} has {int(self.balance)}."
        else:
            raise ValueError

    def check(self, other_user, money):
        self.money = money
        if other_user.checking_account == False or other_user.balance - self.money <1:
            raise ValueError
        else:
            self.balance = self.balance + self.money
            other_user.balance = other_user.balance - self.money
            return f"{self.name} has {int(self.balance)} and {other_user.name} has {other_user.balance}."

    def add_cash(self, money_to_add):
        self.money_to_add = money_to_add
        self.balance = self.balance + self.money_to_add
        return f"{self.name} has {int(self.balance)}."
