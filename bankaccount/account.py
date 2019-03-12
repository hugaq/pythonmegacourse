class account():
    def __init__(self, balance, accountnumber):
        self.balance = balance
        self.accountnumber = accountnumber

    def withdrawl(self, withdrawl):
        self.balance -= withdrawl

    def deposit(self, deposit):
        self.balance += deposit

def main():
