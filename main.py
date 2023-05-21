class BankAccount:
    accounts = []
    def __init__(self,int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print(f"Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self 
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()
        
account1 = BankAccount(0.25,250000)
account2 = BankAccount(0.125,150000)

account1.deposit(10000).deposit(20000).deposit(5000).withdraw(50000).yield_interest().display_account_info()

account2.deposit(10).deposit(20).withdraw(1000).withdraw(5000).withdraw(10000).withdraw(50000).yield_interest().display_account_info()

BankAccount.print_all_accounts()