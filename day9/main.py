import art

print(art.logo)

print("Welcom to the  secret aution program!")

auction={}
should_continue = True





def highest_bidder(auction):
    highes_bid =0
    for bidder in auction:
        bid_price = auction[bidder]
        if bid_price > highes_bid:
            highes_bid = bid_price
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highes_bid}")

while should_continue is True:
    name = input("What is your name?\n")
    price = int(input("How much would you like to bid $?\n"))
    auction[name] = price
    wanna_continue = input("Are there any other bidders? Type 'yes or 'no: \n").lower()
    if wanna_continue == "no":
        should_continue = False
        highest_bidder(auction)
    elif wanna_continue == "yes":
        print("\n "* 50)
