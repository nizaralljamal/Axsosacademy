class BankAccount:
    def __init__ (self,int_rate = 1,balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw (self,amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= ( self.int_rate)
        return self     

md = BankAccount()
md.deposit(100).deposit(200).deposit(200).withdraw(50).yield_interest().display_account_info()
ms = BankAccount(3,500)
ms.deposit(100).deposit(200).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()


