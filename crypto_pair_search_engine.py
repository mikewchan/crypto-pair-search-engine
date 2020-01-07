import cryptowatch as cw

# Asks user to input a crypto they would like to buy
# Think about whether they will enter the entire name or the 3-letter ticker
# Will eventually need this to be a dropdown list with search

currency1a_input = input('Enter the first currency of the trading pair: ')

# Input Validation - check to see if the input exists and is all alphabetical, then changes to lowercase to search
# figure this out later

# if len(currency1_input) > 0 and currency1_input.isalpha():
#    currency1 = currency1_input.lower()
# else:
#    print("Please enter the currency correctly: ")

currency1b_input = input('Enter the second currency of the trading pair: ')

# Repeat Input Validation for currency2_input

all_markets = cw.markets.list()

market_pair_1a = currency1a_input+currency1b_input
market_pair_1b = currency1b_input+currency1a_input
market_exchange_count = 0


# Need to eventually turn this into a function to apply to other inputted market pairs
for market in all_markets.markets:
    if market.pair == market_pair_1a:
        print("{} has a {} market".format(market.exchange, market_pair_1a))
        market_exchange_count = market_exchange_count + 1
    elif market.pair == market_pair_1b:
        print("{} has a {} market".format(market.exchange, market_pair_1b))
        market_exchange_count = market_exchange_count + 1

if market_exchange_count == 0:
    print("There doesn't seem to be a market for these currencies. Wanna try another pair?")
else:
    print("There are {} exchanges that have this market".format(market_exchange_count))



