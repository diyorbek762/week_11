def withdraw_funds(account, amount):
    current_balance=account["balance"]
    my_limit=account["limit"]
    amount=float(amount)
    if amount<0:
        raise ValueError("Invalid amount")
    new_balance = current_balance - amount
    if new_balance>=0:
        account['balance'] = new_balance
    elif new_balance>=my_limit:
        account['balance'] = new_balance
        raise UserWarning("Overdraft used")
    elif new_balance<my_limit:
        raise ValueError("Overdraft limit exceeded")

    



        

            
my_account = {'balance': 50.0, 'limit': -100.0}
attempts = [40, 60, 200] 
# 1. 50 - 40 = 10 (Safe)
# 2. 10 - 60 = -50 (Warning, but works)
# 3. -50 - 200 = -250 (Fail)


for amount in attempts:
    try:
        withdraw_funds(my_account, amount)
    except UserWarning as e:
        print(f'Attempting to withdraw ${amount}..')
        print(f"Alert: {e}. Balance is {my_account['balance']}")
        print('Transaction completed with warning.')
    except ValueError as e:
        print(f'Attempting to withdraw ${amount}..')
        print(f'Transaction Failed: {e}')
    else:
        print(f'Attempting to withdraw ${amount}..')
        print("Transaction successful.")
    finally:
        print(f"Current Balance: {my_account['balance']}")

        

