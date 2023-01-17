from c3_simple_sol import BankAccount

account1 = BankAccount(account_num=12345,
                      owner_id='012345678', owner_name='David', owner_address='Tel Aviv',
                      usd_allowed=True)

account2 = BankAccount(account_num=5555,
                      owner_id='34856738', owner_name='David', owner_address='Tel Aviv',
                      usd_allowed=True)
# account.deposit(456)

# print(BankAccount._valid_params(345, 'usd'))

print(BankAccount.prime)
print(account1.prime)
print(account2.prime)

print(account1.prime is account2.prime)
print(account1._BankAccount__account_num == account2._BankAccount__account_num)
BankAccount.prime = 4.5
print(BankAccount.prime)
print(account1.prime)

account1.prime = 0.9
account1.blbla='ttt'

print(account1.prime)
print(account1.blbla)

print(account1._valid_params(435,'uy'))
print(BankAccount._valid_params(345, 'usd'))

