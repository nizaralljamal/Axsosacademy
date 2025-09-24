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
md.make_deposit(100)
md.make_deposit(200)
md.make_deposit(200)
md.make_withdraw(50)
md.display_account_info() 
ms = user("ms",500)
ms.make_deposit(100)
ms.make_deposit(200)
ms.make_withdraw(50)
ms.make_withdraw(50)
ms.make_withdraw(50)
ms.make_withdraw(50)
ms.display_account_info()
ma = user('ma',0)
ma.make_deposit(1000)
ma.make_withdraw(50)
ma.make_withdraw(50)
ma.make_withdraw(50)

ma.display_account_info()


    