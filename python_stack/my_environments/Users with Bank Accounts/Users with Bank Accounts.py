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

class user:
    def __init__ (self,name):
        self.name = name
        self.Account = []
    def make_deposit(self,amount,index):
        self.Account[index].deposit(amount)
        return self
    def make_withdraw (self,amount,index):
        self.Account[index].withdraw(amount)
        return self
    def display_account_info(self):
        print(f" name: {self.name}")
        for i in range(len(self.Account)):
            print(self.Account[i].display_account_info())
    def creat_account(self):
        self.Account.append(BankAccount(2,1000)) 

Nizar = user("Nizar")
Nizar.creat_account()
Nizar.make_deposit(1000,0)
Nizar.display_account_info()
