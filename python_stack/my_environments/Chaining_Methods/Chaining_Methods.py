class user:
    def __init__ (self,name,balance):
        self.name = name
        self.balance = balance
    def make_deposit(self,amount):
        self.balance += amount
        return self
    def make_withdraw (self,amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f" name: {self.name} Balance: {self.balance}")

md = user("md",0)
md.make_deposit(100).make_deposit(200).make_deposit(200).make_withdraw(50).display_account_info() 
ms = user("ms",500)
ms.make_deposit(100).make_deposit(200).make_withdraw(50).make_withdraw(50).make_withdraw(50).make_withdraw(50).display_account_info()

    