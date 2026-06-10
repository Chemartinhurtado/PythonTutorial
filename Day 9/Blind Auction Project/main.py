from idlelib.pyshell import restart_line

import art
print(art.logo)
restart = True

while restart:
# TODO-1: Ask the user for input
    name = input("What is your name?:")
    price = input("What is your bid?: $ ")

# TODO-2: Save data into dictionary {name: price}
    bidders = {
    }

# TODO-3: Whether if new bids need to be added
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'")
    if other_bidders == "yes":
        print("\n" * 100)

    else:
        restart = False
        print(bidders)

# TODO-4: Compare bids in dictionary
