
def highest_bid(bidding):
    winner = ""
    highest = 0
    for bidder in bidding:
        bid_amount = bidding[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()
    if other_bidders == "no":
        continue_bidding = False
        highest_bid(bids)
    elif other_bidders == "yes":
        print("\n" * 20)

