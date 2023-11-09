def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return tic


def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return tic


tic = "WES.AX"
print(tic)
qan_tic()


def mk_csv_name(tic):
    tic = tic.lower()
    tic_base = tic.split( '.' ) [0]
    return f' (tic_base)'
    stx_prc.csv

watch_list = ['QAN.AX', 'CBA.AX', 'BHP.AX']

# The market opens and you notice that the following stocks in
# active_list has displayed unusual market activity
active_list = ['CBA.AX', 'BHP.AX', 'NAB.AX', 'WBC.AX', 'RIO.AX']

# You want to buy the stocks that have unusual market activity that
# are also in your watch_list

# TASK 1A:
# Use a for loop to create a list called buy_stocks_list that contain stocks
# that are in present in both watch_list and active_list

buy_stocks_list = []
for stock in active_list:
    if stock in watch_list:
        buy_stocks_list.append(stock)

print('Task 1A:')
print(buy_stocks_list)
print()

# TASK 1B:
# Use a list comprehension to create a list called buy_stocks that contain stocks
# that are in present in both watch_list and active_list

buy_stocks_list = [stock for stock in active_list if stock in watch_list]

print('Task 1B:')
print(buy_stocks_list)
print()


# After identifying the stocks that you want to buy, you have to decide
# how many shares of each stock to buy. Based on your research, you think that
# the following formula is the best way of determining how many shares to buy:
#
# Buy 17 + 1 + 14 = 32 shares of QAN.AX because
# Q is the 17th letter in the alphabet
# A is the 1st letter in the alphabet
# N is the 14th letter in the alphabet

# TASK 2:
# Write a function called buy_how_many that takes in a ticker (e.g. 'QAN.AX')
# and returns the number of shares to buy
# HINT: 'abc'.index('c') returns 2, the index of the letter 'c' in the string 'abc'
# HINT: You can loop through characters in a string like looping through a list

def buy_how_many(ticker):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num_shares = 0
    for i in ticker[:3]:
        num_shares += alphabet.index(i) + 1
    return num_shares


print('Task 2:')
for stock in buy_stocks_list:
    print(f'Buy {buy_how_many(stock)} shares of {stock}')
print()

# TASK 3A:
# Use a for loop to create a dictionary called buy_stock_dict
# that contains the stocks in buy_stocks_list as its keys
# and the number of shares we should buy for each stock as its values

buy_stock_dict = {}
for stock in buy_stocks_list:
    buy_stock_dict[stock] = buy_how_many(stock)

print('Task 3A:')
print(buy_stock_dict)
print()

# TASK 3B:
# Use a dictionary comprehension to create a dictionary called buy_stock_dict
# that contains the stocks in buy_stocks_list as its keys
# and the number of shares we should buy for each stock as its values

buy_stock_dict = {stock: buy_how_many(stock) for stock in buy_stocks_list}

print('Task 3B:')
print(buy_stock_dict)
print()
