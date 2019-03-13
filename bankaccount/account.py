

class account():
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            data = file.read().splitlines()
            try:
                self.balance = int(data[-1])
            except:
                self.balance = 0

    def withdrawl(self, withdrawl):
        self.balance -= withdrawl

    def deposit(self, deposit):
        self.balance += deposit

    def commit(self):
        with open(self.filepath, 'a') as file:
            file.write('\n')
            file.write(str(self.balance))

def main():
    an_account = account('/home/denkpolster/Python/Udemy/pythonmegacourse/bankaccount/balance.txt')
    print(an_account.balance)
    an_account.deposit(600)
    print(an_account.balance)
    an_account.commit()


if __name__ == "__main__":
    main()
