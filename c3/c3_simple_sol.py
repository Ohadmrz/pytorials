class BankAccount:

    prime = 4.75

    def __init__(self, account_num: int,
                 owner_id: str, owner_name: str, owner_address: str,
                 usd_allowed: bool = False, credit_limit: float = 0):

        self.__account_num: int = account_num
        self.__account_owner: dict = {
            'id': owner_id,
            'name': owner_name,
            'address': owner_address
        }

        self.__nis_balance: float = 0
        self.__usd_balance: float = 0
        self.__usd_allowed: bool = usd_allowed
        self.__nis_credit_limit: float = credit_limit

        # date -> transactions
        self.__transactions: dict[str, list] = {}

    def __str__(self):
        return f"Account {self.__account_num}"

    @staticmethod
    def _valid_params(amnt, currency):
        return amnt > 0 and currency in ('nis', 'usd')


    def _add_transaction(self, transaction_date: str, transaction_type: str, amnt: float, currency: str):

        # add new dictionary key if needed
        if transaction_date not in self.__transactions:
            self.__transactions[transaction_date] = []

        # if we are here, we are sure that the key already exists
        new_transaction = {
            'date': transaction_date,
            'type': transaction_type,
            'amnt': amnt,
            'currency': currency
        }
        self.__transactions[transaction_date].append(new_transaction)

    def withdraw(self, date: str, amount: float, currency: str = 'nis') -> bool:

        if not self._valid_params(amount, currency):
            return False

        if currency == 'nis':
            if self.__nis_balance - amount >= (self.__nis_credit_limit * -1):
                self.__nis_balance -= amount
            else:
                return False
        else:
            if self.__usd_allowed and self.__usd_balance >= amount:
                self.__usd_balance -= amount
            else:
                return False
        self._add_transaction(date, 'withdraw', amnt=amount, currency=currency)
        return True

    def deposit(self, date, amount: float, currency: str = 'nis'):
        if not self._valid_params(amount, currency):
            return False

        if currency == 'nis':
            self.__nis_balance += amount
            self._add_transaction(date, 'deposit', amount, currency)
            return True
        else:
            if not self.__usd_allowed:
                return False
            else:
                self._add_transaction(date, 'deposit', amount, currency)
                self.__usd_balance += amount
                return True

    def convert_to_usd(self, date, nis_amnt, nis2usd_exchange_rate):
        if nis_amnt < 0:
            return False
        if not self.__usd_allowed or self.__nis_balance - nis_amnt < (self.__nis_credit_limit * -1):
            return False
        self.__nis_balance -= nis_amnt
        self.__usd_balance += nis_amnt * nis2usd_exchange_rate
        self._add_transaction(date, 'convert_to_usd', nis_amnt, 'nis')
        return True

    def convert_to_nis(self, date, usd_amnt, usd2nis_exchange_rate):
        if usd_amnt < 0:
            return False
        if not self.__usd_allowed or self.__usd_balance < usd_amnt:
            return False
        self.__nis_balance += usd_amnt * usd2nis_exchange_rate
        self.__usd_balance -= usd_amnt
        self._add_transaction(date, 'convert_to_nis', usd_amnt, 'usd')
        return True

    def get_current_balance(self) -> tuple[float, float]:
        return self.__nis_balance, self.__usd_balance

    def get_transactions_per_date(self, date: str) -> list[str]:
        return self.__transactions.get(date, [])


if __name__ == '__main__':

    # create bank account
    account1 = BankAccount(account_num=12345,
                           owner_id='019999999', owner_name='David', owner_address='Tel Aviv',
                           usd_allowed=True, credit_limit=10_000)
    print(f"Current balance for {account1}: {account1.get_current_balance()}")

    print("Trying to withdraw 10500 shekels passing the limit - should fail!")
    result = account1.withdraw("11-12-2022", 10500)
    print(f"Result: {result}")

    print("Trying to withdraw 9500 shekels in the range of limit - should succeed!")
    result = account1.withdraw("11-22-2022", 9500)
    print(f"Result: {result}")

    print(f"Current balance: {account1.get_current_balance()}")

    print("Trying to convert 1000 shekels to USD - outside the limit, should fail")
    result = account1.convert_to_usd("12-22-2022", 1000, 3.5)
    print(f"Result: {result}")

    print("Deposit 20_000 to account - should succeed")
    result = account1.deposit("12-22-2022", 20000)
    print(f"Result: {result}")

    print("Deposit $5_000 to account - should succeed")
    result = account1.deposit("12-22-2022", 5000, currency='usd')
    print(f"Result: {result}")

    print(f"New balance: {account1.get_current_balance()}")
    print(f"Transactions on 11-22-2022: {account1.get_transactions_per_date('11-22-2022')}")
    print(f"Transactions on 12-22-2022: {account1.get_transactions_per_date('12-22-2022')}")