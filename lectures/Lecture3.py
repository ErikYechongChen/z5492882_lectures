# Use the following data for Questions 1 - 3

stk_data = [
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.5,
        'volume': 1000,
        'ownerName': 'John',
     },
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.75,
        'volume': 1200,
        'ownerName': 'Micheal',
     },
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.4,
        'volume': 150,
        'ownerName': 'Lucy',
     },
]

# Question 1
# Write a simple for-loop to determine the amount traded
# i.e. the sum of price * volume across all dicts in stk_data






# Question 2
# We are only interested in finding out whether the amount traded is more than $1000
# In reality, we might be working with a list that contains hundreds or even thousands of items
# Iterating all items in such a list might take a long time
#
# Write a for-loop that contains a break statement that can
# efficiently tell us whether the amount traded is more than $1000






# Question 3
# We are only interested in insider trades that are large enough
# E.g. We are not interested in Lucy's trade because
# we consider the amount traded = $5.4 * 150 = $810 to be too small
# We only want to consider trades that are >= $1000
# Write a for-loop that sums up the amount traded for trades that are >= $1000






# Question 4
aapl = [
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.5,
        'volume': 1000,
        'ownerName': 'John',
     },
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.75,
        'volume': 1200,
        'ownerName': 'Micheal',
     },
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.4,
        'volume': 150,
        'ownerName': 'Lucy',
     },
]

amzn = [
    {
        'ticker': 'AMZN',
        'date': '2022-09-30',
        'price': 11,
        'volume': 950,
        'ownerName': 'John',
     },
    {
        'ticker': 'AMZN',
        'date': '2022-09-30',
        'price': 11.2,
        'volume': 650,
        'ownerName': 'Micheal',
     },
]

ibm = [
    {
        'ticker': 'IBM',
        'date': '2022-09-30',
        'price': 6,
        'volume': 300,
        'ownerName': 'John',
     },
    {
        'ticker': 'IBM',
        'date': '2022-09-30',
        'price': 6.4,
        'volume': 1100,
        'ownerName': 'Micheal',
     },
]

stk_list = [aapl, amzn, ibm]

# Given stk_list above, we want to create a dictionary of the form
# {'aapl': xxxx, 'amzn': xxxx, 'ibm': xxxx}, where xxxx is the amount traded for each stock
#
# Achieve this using a single for-loop that iterates over stk_list
#
# HINT: write a function that calculates the amount traded for a single stock
#       and call that function in each interation of the for-loop







# Question 5 - Challenge
stk_data = [
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.5,
        'volume': 1000,
        'ownerName': 'John',
     },
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.75,
        'volume': 1200,
        'ownerName': 'Micheal',
     },
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.4,
        'volume': 150,
        'ownerName': 'Lucy',
     },
    {
        'ticker': 'AMZN',
        'date': '2022-09-30',
        'price': 11,
        'volume': 950,
        'ownerName': 'John',
     },
    {
        'ticker': 'AMZN',
        'date': '2022-09-30',
        'price': 11.2,
        'volume': 650,
        'ownerName': 'Micheal',
     },
    {
        'ticker': 'IBM',
        'date': '2022-09-30',
        'price': 6,
        'volume': 300,
        'ownerName': 'John',
     },
    {
        'ticker': 'IBM',
        'date': '2022-09-30',
        'price': 6.4,
        'volume': 1100,
        'ownerName': 'Micheal',
     },
]

# Given stk_data above, we want to create a dictionary of the form
# {'aapl': xxxx, 'amzn': xxxx, 'ibm': xxxx}, where xxxx is the amount traded for each stock
#
# Achieve this using a single for-loop that iterates over stk_data

