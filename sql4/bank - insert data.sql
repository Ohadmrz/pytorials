DELETE FROM transaction_accounts;
DELETE FROM account_owners;
DELETE FROM transactions;
DELETE FROM accounts;
DELETE FROM customers;


INSERT INTO public.customers (id, passport_num, name, address) VALUES (2, 101010101, 'Angelina Jolie', 'California');
INSERT INTO public.customers (id, passport_num, name, address) VALUES (1, 123456789, 'Brad Pitt', 'USA, Los Angeles');
INSERT INTO public.customers (id, passport_num, name, address) VALUES (5, 1111111, 'John Travolta', 'New York, USA');
INSERT INTO public.customers (id, passport_num, name, address) VALUES (7, 222223333, 'James Cameron', 'Canada');
INSERT INTO public.customers (id, passport_num, name, address) VALUES (8, 454545454, 'Jennifer Lawrence', 'Monaco');
INSERT INTO public.customers (id, passport_num, name, address) VALUES (3, 12121212, 'John Lennon', 'London, UK');


INSERT INTO public.accounts (id, balance, max_limit) VALUES (2, 3001000, 10000000);
INSERT INTO public.accounts (id, balance, max_limit) VALUES (1, 2999000, 10000000);
INSERT INTO public.accounts (id, balance, max_limit) VALUES (3, 40000, 2000);
INSERT INTO public.accounts (id, balance, max_limit) VALUES (4, 1000000, 100230);
INSERT INTO public.accounts (id, balance, max_limit) VALUES (5, 3450000, 0);

INSERT INTO public.account_owners (id, customer_id, account_id) VALUES (1, 2, 2);
INSERT INTO public.account_owners (id, customer_id, account_id) VALUES (2, 1, 1);
INSERT INTO public.account_owners (id, customer_id, account_id) VALUES (3, 8, 3);
INSERT INTO public.account_owners (id, customer_id, account_id) VALUES (4, 8, 4);
INSERT INTO public.account_owners (id, customer_id, account_id) VALUES (5, 1, 5);
INSERT INTO public.account_owners (id, customer_id, account_id) VALUES (6, 2, 5);

INSERT INTO public.transactions (id, transaction_type, ts, initiated_by) VALUES (8, 'transfer', '2023-09-01 10:00:00', 2);
INSERT INTO public.transactions (id, transaction_type, ts, initiated_by) VALUES (9, 'transfer', '2023-01-11 14:55:53.439946', 2);
INSERT INTO public.transactions (id, transaction_type, ts, initiated_by) VALUES (11, 'transfer', '2023-01-11 15:10:01.928136', 2);
INSERT INTO public.transactions (id, transaction_type, ts, initiated_by) VALUES (12, 'transfer', '2023-02-27 10:00:00', 1);
INSERT INTO public.transactions (id, transaction_type, ts, initiated_by) VALUES (13, 'transfer', '2023-09-01 10:00:00', 2);
INSERT INTO public.transactions (id, transaction_type, ts, initiated_by) VALUES (15, 'transfer', '2023-09-01 10:00:00', 2);
INSERT INTO public.transactions (id, transaction_type, ts, initiated_by) VALUES (17, 'transfer', '2023-09-01 10:00:00', 2);
INSERT INTO public.transactions (id, transaction_type, ts, initiated_by) VALUES (19, 'transfer', '2023-09-01 10:00:00', 2);
INSERT INTO public.transactions (id, transaction_type, ts, initiated_by) VALUES (20, 'transfer', '2023-03-09 00:00:00', 1);
INSERT INTO public.transactions (id, transaction_type, ts, initiated_by) VALUES (21, 'transfer', '2023-03-09 21:53:39.86404', 1);



INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (8, 'sender', 8, 2);
INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (9, 'receiver', 8, 1);
INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (10, 'sender', 9, 2);
INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (11, 'receiver', 9, 1);
INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (14, 'sender', 11, 2);
INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (15, 'receiver', 11, 1);
INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (16, 'sender', 12, 1);
INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (17, 'receiver', 12, 2);
INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (18, 'sender', 13, 2);
INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (19, 'receiver', 13, 1);
INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (22, 'sender', 15, 2);
INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (23, 'receiver', 15, 1);
INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (26, 'sender', 17, 2);
INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (27, 'receiver', 17, 1);
INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (30, 'sender', 19, 2);
INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (31, 'receiver', 19, 1);
INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (32, 'receiver', 21, 2);
INSERT INTO public.transaction_accounts (id, account_role, transaction_id, account_id) VALUES (33, 'sender', 21, 1);
