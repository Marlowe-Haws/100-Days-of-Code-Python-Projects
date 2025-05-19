from art import logo
print(logo)
user_names = []
user_bids = []
more_bidders = "y"

while more_bidders == "y":
    while True:
        user_name = input("What is your name?: ")
        if not user_name.isalpha():
            print("\nPlease enter letters only.")
            continue
        else:
            user_names.append(user_name)
            break

    while True:
        user_bid= input("\nWhat is your bid?: $")
        try:
            user_bid = float(user_bid)
        except ValueError:
            print("\nPlease only enter numbers (decimal point allowed): $")
            continue
        user_bid = round(user_bid, 2)
        user_bids.append(user_bid)
        break

    while True:
        more_bidders = input("\nAre there any other bidders? Type 'y' or 'n': ").strip().lower()
        if not more_bidders.isalpha():
            print("\nPlease only enter 'y' or 'n': ")
            continue
        elif more_bidders != "y" and more_bidders != "n":
            print("\nPlease only enter 'y' or 'n': ")
            continue
        else:
            print("\n" * 100)
            break

# My method relying on lists
max_bid = max(user_bids)
max_index = user_bids.index(max_bid)

# Alternative with dictionary
user_names_and_bids = dict(zip(user_names, user_bids))
#max_bid_key = max(user_names_and_bids, key = user_names_and_bids.get)
#max_bid = user_names_and_bids[max_bid_key]
#or
#max_bid = max(user_names_and_bids.values())

print(f"The winner is {user_names[max_index]}, with a bid of ${max_bid:.2f}.")
