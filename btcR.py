# created by NapSec_

from typing import List, Dict

# Store the user-input addresses in a list
addresses = []

# Prompt the user to enter an address
address = input("Enter a Bitcoin address: ")

# Add the address to the list
addresses.append(address)

def find_transactions(address: str) -> List[Dict[str, str]]:
    # Replace this with a proper implementation that returns a list of dictionaries, each representing a transaction
    return []

def get_other_address(transaction: Dict[str, str], address: str) -> str:
    # Replace this with a proper implementation that returns the other address involved in a transaction
    return ""

# Continue prompting the user for additional addresses until they enter "done"
while address != "done":
    address = input("Enter another Bitcoin address (or 'done' to finish): ")
    if address != "done":
        addresses.append(address)

# Use a loop to iterate over the list of addresses
for address in addresses:
    # For each address, find all transactions involving that address
    transactions = find_transactions(address)

    # Print the address and the number of transactions it was involved in
    print(f"{address}: {len(transactions)} transactions")

    # Use another loop to iterate over the transactions
    for transaction in transactions:
        # For each transaction, find the other address involved in the transaction
        other_address = get_other_address(transaction, address)

        # Print the other address and the amount transferred in the transaction
        print(f" - {other_address}: {transaction['amount']} BTC")
