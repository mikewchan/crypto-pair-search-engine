import cryptowatch as cw


# Asks user to input a trading pair they would like to search
# Think about whether they will enter the entire name or the 3-letter ticker
# Will eventually need this to be a dropdown list with search

pair1_currency1 = input('Enter the abbreviation for the 1st currency of the 1st trading pair to search: ')
pair1_currency2 = input('Enter the abbreviation for the 2nd currency of the 1st trading pair to search: ')

# Pairs in the CryptoWatch API can either be btceth or ethbtc, this code creates both combos to search
pair1_name1 = pair1_currency1 + pair1_currency2
pair1_name2 = pair1_currency2 + pair1_currency1

pair_matrix = []

pair_matrix.append([pair1_name1, pair1_name2])

# Asks user if they want to search a 2nd pair and 3rd pair

second_pair_answer = None
second_pair_answer = input("Would you like to search for another trading pair? Enter y/n: ")
if second_pair_answer == "y":
    pair2_currency1 = input(
        'Enter the abbreviation for the 1st currency of the 2nd trading pair to search: ')
    pair2_currency2 = input(
        'Enter the abbreviation for the 2nd currency of the 2nd trading pair to search: ')
    pair2_name1 = pair2_currency1 + pair2_currency2
    pair2_name2 = pair2_currency2 + pair2_currency1

    pair_matrix.append([pair2_name1, pair2_name2])

    third_pair_answer = None
    third_pair_answer = input("Would you like to search for another trading pair? Enter y/n: ")
    if third_pair_answer == "y":
        pair3_currency1 = input(
            'Enter the abbreviation for the 1st currency of the 3rd trading pair to search: ')
        pair3_currency2 = input(
            'Enter the abbreviation for the 2nd currency of the 3rd trading pair to search: ')
        pair3_name1 = pair3_currency1 + pair3_currency2
        pair3_name2 = pair3_currency2 + pair3_currency1

        pair_matrix.append([pair3_name1, pair3_name2])

print(pair_matrix)

# Searches all pairs in pair_matrix for markets

all_markets = cw.markets.list()
market_exchange_count = 0

for pair_combo in pair_matrix:
    for pair in pair_combo:
        for market in all_markets.markets:
            if market.pair == pair:
                print("{} has a {} market".format(market.exchange, pair))
                market_exchange_count = market_exchange_count + 1


if market_exchange_count == 0:
    print("There doesn't seem to be a market for these currencies. Wanna try another pair?")
else:
    print("There are {} exchanges that have this market".format(market_exchange_count))



