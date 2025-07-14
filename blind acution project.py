# TODO-1: Ask the user for input
user_name = input("What is your name?: \n")
user_bid = int(input("What's your bid?: \n"))


# TODO-2: Save data into dictionary {name: price}
bid_dict = {}

num_bids = int(input("How many bids do you want to collect?: "))

for _ in range(num_bids):
# for _ in range(num_bids):  # Iterate a specific number of times
    user_name = input("What is your name?: ")
    user_bid = int(input("What's your bid?: ")) # Convert bid to integer immediately

    # Add/update the dictionary using the assignment operator
    bid_dict[user_name] = user_bid

print(bid_dict)
# TODO-3: Whether if new bids need to be added
while True:
    user_response = input("Do you want to add another user? (yes/no): ").lower()
    if user_response == 'yes':
        print("\n" * 10)
        num_bids = int(input("How many bids do you want to collect?: "))
    else:
        break

# TODO-4: Compare bids in dictionary
bid_winner = max(bid_dict, key=bid_dict.get)
print(f"The Winner of bid: {bid_winner}")
