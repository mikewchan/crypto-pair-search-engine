import cryptowatch as cw

# Asks user to input a crypto they would like to buy
# Think about whether they will enter the entire name or the 3-letter ticker
# Will eventually need this to be a dropdown list with search

currencypair1_input1 = input('Enter the abbreviation for the 1st currency of the 1st trading pair to search: ')
currencypair1_input2 = input('Enter the abbreviation for the 2nd currency of the 1st trading pair to search: ')

currencypair1_combo1 = currencypair1_input1 + currencypair1_input2
currencypair1_combo2 = currencypair1_input2 + currencypair1_input1

currencypair2_input1 = None
currencypair2_input2 = None

answer = None
while answer not in ("y", "Y", "n", "N"):
    answer = input("Would you like to search for another trading pair? Enter y/n: ")
    if answer == "y":
        currencypair2_input1 = input(
            'Enter the abbreviation for the 1st currency of the 2nd trading pair to search: ')
        currencypair2_input2 = input(
            'Enter the abbreviation for the 2nd currency of the 2nd trading pair to search: ')
        currencypair2_combo1 = currencypair2_input1 + currencypair2_input2
        currencypair2_combo2 = currencypair2_input2 + currencypair2_input1
    elif answer == "n":
        break
    else:
        print("Please enter either 'y' or 'n' only.")

currencypair3_input1 = None
currencypair3_input2 = None

answer = None
while answer not in ("y", "Y", "n", "N"):
    answer = input("Would you like to search for another trading pair? Enter y/n: ")
    if answer == "y":
        currencypair3_input1 = input(
            'Enter the abbreviation for the 1st currency of the 2nd trading pair to search: ')
        currencypair3_input2 = input(
            'Enter the abbreviation for the 2nd currency of the 2nd trading pair to search: ')
        currencypair3_combo1 = currencypair3_input1 + currencypair3_input2
        currencypair3_combo2 = currencypair3_input2 + currencypair3_input1
    elif answer == "n":
        break
    else:
        print("Please enter either 'y' or 'n' only.")

all_markets = cw.markets.list()

market_exchange_count = 0

# Need to eventually turn this into a function to apply to other inputted market pairs
for market in all_markets.markets:
    if market.pair == currencypair1_combo1:
        print("{} has a {} market".format(market.exchange, currencypair1_combo1))
        market_exchange_count = market_exchange_count + 1
    elif market.pair == currencypair1_combo2:
        print("{} has a {} market".format(market.exchange, currencypair1_combo2))
        market_exchange_count = market_exchange_count + 1

if market_exchange_count == 0:
    print("There doesn't seem to be a market for these currencies. Wanna try another pair?")
else:
    print("There are {} exchanges that have this market".format(market_exchange_count))



