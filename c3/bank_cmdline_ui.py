from bank_account_exceptions import BankAccountException, InvalidParamError, InsufficientFundsError
from c3_2_exceptions import BankAccount, Person

if __name__ == '__main__':
    # nmae = input("insert name")
    bank_account = BankAccount('discount', 'ddd', 123,
                set([Person(1234, 'val', 'netanya', '046374653')]))

    while True:
        try:
            amnt = int(input("Inesrt amount to withdraw: "))
            crncy = input("Inesrt currency to withdraw: ")
            bank_account.withdraw(amnt, crncy)
            print("Operation succeded")
            break
        except ValueError:
            print("you inserted invalid amount")
        except BankAccountException as e:
            print(e)
    # except InvalidParamError:
    #     print("params")
    # except InsufficientFundsError:
    #     print("funds")