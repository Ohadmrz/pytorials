import random


class Person:

    def __init__(self, person_id: str, name: str, address: str, phone: str):
        self.id = person_id
        self.name = name
        self.address = address
        self.phone = phone


class BankAccount:

    def __init__(self, bank: str, branch: str, holders: set[Person], credit_limit: int=0):
        self.bank = bank
        self.branch = branch
        self.holders = holders
        self.account_num = random.randint(1000, 10000)
        self.balance = 0
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


class Bank:
    def __init__(self):
        self. accounts = {}

    def transfer(self, from_account:BankAccount, to_account:BankAccount):
        from_account.withdraw(300)
        to_account.deposit(300)


# holder = {
#     'name': 'Valeria',
#     'id': '12334534',
#     'address': 'netanya',
#     'phoe': 's873456872'
# }
holder1 = Person('12334534', 'Valeria', 'netanya', '73482345')
holder2 = Person('12363333', 'Victor', 'netanya', '034645765')
holders_set = set([holder1, holder2])
account = BankAccount('Discount', 'Netanya', holders_set, credit_limit=10000)
account.transfer(to_account, amount, date)
