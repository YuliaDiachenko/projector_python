class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number
    
    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number
    
    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'

class SavingsAccount(Account):
    def __init__(self, _balance, _account_number, interest):
        super().__init__(_balance, _account_number)    
        self.interest = interest
    def add_interest(self):
        self._balance += self.get_balance()*self.interest

class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
         super().__init__( balance, account_number)  
         self.overdraft_limit = overdraft_limit  

class Bank():
    def __init__(self, accounts: list):# list[Account]
        self.accounts = accounts
    def open_account(self, account):
        self.accounts.append(account)
    def close_account(self):
        self.accounts.remove(account)
    def update(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount) and account.get_balance() < 0:
                print(f"Account number {account.get_account_number()}: You are in overdraft")

accounts_list = []
Monobank = Bank(accounts_list)

first_account = SavingsAccount(4000, 1, 0.25)
Monobank.open_account(first_account)

my_account = CurrentAccount(3000, 2, 16000)
Monobank.open_account(my_account)

acc_overdraft = CurrentAccount(-2000, 3, 16000)
Monobank.open_account(acc_overdraft)



for account in accounts_list:
    print(account)

Monobank.update()
acc_overdraft.deposit(7000)
for account in accounts_list:
    print(account)

first_account.deposit(1000)
Monobank.update()
for account in accounts_list:
    print(account)
