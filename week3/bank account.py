class BankAccount:
    def __init__(self):
        self.__balance = 0
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal")
    
    def get_balance(self):
        return self.__balance

account = BankAccount()

account.deposit(100)
print(account.get_balance())

account.withdraw(30)
print(account.get_balance())

account.withdraw(80)
print(account.get_balance())