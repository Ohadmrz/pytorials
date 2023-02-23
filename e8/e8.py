# add locking mechanism and make thread-safe
from concurrent.futures import ThreadPoolExecutor
from threading import Lock, Thread


class BankAccount:

    def __init__(self, account_num, holder_name):
        self._account_name = account_num
        self._holder_name = holder_name
        self._transactions_list = []  # just the name of the action
        self._balance = 0
        self._lock: Lock = Lock()

    def safe(f):
        def wrapper(self, *args, **kwargs):
            with self._lock:
                return f(self, *args, **kwargs)

        return wrapper

    @safe
    def deposit(self, amount):
        self._balance += amount
        self._transactions_list.append("deposit")

    @safe
    def withdraw(self, amount):
        self._balance -= amount
        self._transactions_list.append("withdraw")


# this code should run without problems
if __name__ == '__main__':
    account = BankAccount(123456, "Israel Israeli")

    def multiple_transactions_deposit(account):
        for i in range(100, 2000000, 10):
            account.deposit(i)

    def multiple_transactions_withdraw(account):
        for i in range(100, 2000000, 10):
            account.withdraw(i)

    with ThreadPoolExecutor(4) as executor:
        executor.submit(multiple_transactions_deposit, account)
        executor.submit(multiple_transactions_withdraw, account)

    assert account._balance == 0, \
        f"Expected balance: 0, received: {account._balance}"
    assert len(account._transactions_list) == 399980, \
        f"Expected transactions: 399980, received: {len(account._transactions_list)}"
