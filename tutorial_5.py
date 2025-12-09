def perform_atomic_transfer(accounts, sender, receiver, amount):
    if sender not in accounts:
        raise KeyError("Sender not found")
    if accounts[sender]<amount:
        raise ValueError ("Insufficient funds")
    
    accounts[sender]-=amount
    print(f"Withdrew {amount} from {sender}")
    try:
        accounts[receiver]+=amount
        print(f"Deposited {amount} to {receiver}")
    except KeyError:
        accounts[sender]+=amount
        print(f"Error: Receiver not found. Refunding {sender}...")
        raise
    print("Transfer Complete.")


bank_db = {"Alice": 100.0, "Bob": 50.0}

# # try:
# perform_atomic_transfer(bank_db, "Alice", "Bob", 120.0 )

# except 
def main():
    bank_db = {"Alice": 100.0, "Bob": 10.0}
    try:
        perform_atomic_transfer(bank_db, "Alice", "Bob", 150.0 )
    except Exception as e:
        print(e)
        print(f"Current State: {bank_db}")
main()



