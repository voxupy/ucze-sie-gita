from turtle import clear

print("Welcome to bid auction program.")

bids ={}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_ammount = bidding_record[bidder]
        if bid_ammount > highest_bid:
            highest_bid = bid_ammount
            winner = bidder
            
    print(f"The winner is the {winner}, with ammount {highest_bid}$.")


while not bidding_finished:
    name = input("What's your name?: ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    else:
        clear()




