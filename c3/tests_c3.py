from c3_simple_sol import BankAccount


def test_deposit_nis():
    account = BankAccount(account_num=12345,
                          owner_id='012345678', owner_name='David', owner_address='Tel Aviv')
    ret_val = account.deposit('11-11-2022', 100)
    assert ret_val == True
    assert account.get_current_balance() == (100, 0)


def test_deposit_usd_not_allowed():
    account = BankAccount(account_num=12345,
                          owner_id='012345678', owner_name='David', owner_address='Tel Aviv')
    ret_val = account.deposit('11-11-2022', 100, 'usd')
    assert ret_val == False
    assert account.get_current_balance() == (0, 0)


def test_get_transactions():
    account = BankAccount(account_num=12345,
                          owner_id='012345678', owner_name='David', owner_address='Tel Aviv',
                          usd_allowed=True)
    account.deposit('11-11-2022', 100, 'usd')
    account.convert_to_nis('11-11-2022', 10, 3.5)
    account.deposit('10-12-2022', 100.5, 'nis')
    t1 = account.get_transactions_per_date('11-11-2022')
    t2 = account.get_transactions_per_date('10-12-2022')
    assert len(t1) == 2
    assert len(t2) == 1


if __name__ == '__main__':
    test_deposit_nis()
    test_deposit_usd_not_allowed()
    test_get_transactions()