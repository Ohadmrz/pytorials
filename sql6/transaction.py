import datetime

import psycopg2


def transfer(from_account, to_account, amount, initiated_by):
    insert_trans_query = f"""
             INSERT INTO transactions
             (transaction_type, ts, initiated_by)
             VALUES(%s, %s, %s) returning id;
             """
    insert_trans_account_query = f"""
                             INSERT INTO transaction_accounts
                             (account_role, transaction_id, account_id)
                             VALUES( %s, %s, %s );
                             """
    reduce_balance_query = f"""
                             UPDATE accounts
                             SET balance= balance - %s
                             WHERE id=%s
                             """
    increase_balance_query = f"""
                             UPDATE accounts
                             SET balance= balance + %s
                             WHERE id=%s
                             """

    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='bank',
        user='postgres',
        password='postgres')

    with conn:
        with conn.cursor() as cur:
            cur.execute(insert_trans_query, ('transfer', datetime.datetime.now(), initiated_by))
            transfer_id = cur.fetchone()[0]
            cur.execute(insert_trans_account_query, ('receiver', transfer_id, to_account ))
            cur.execute(insert_trans_account_query, ('sender', transfer_id, from_account))
            cur.execute(increase_balance_query, (amount, to_account))
            cur.execute(reduce_balance_query, (amount, from_account))


if __name__ == '__main__':
    transfer(1, 2, 1000, 1)