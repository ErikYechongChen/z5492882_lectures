

#
# # |            | AUD/USD | EUR/AUD |
# # |------------+---------+---------|
# # | 2020-09-08 | 0.7280  | 1.6232  |
# # | 2020-09-09 | 0.7209  | 1.6321  |
# # | 2020-09-10 | NaN     | 1.6221  |
# # | 2020-09-11 | 0.7263  | 1.6282  |
# # | 2020-09-14 | 0.7281  | NaN     |
# # | 2020-09-15 | 0.7285  | 1.6288  |
# data = {
#     'AUD/USD': [ 0.7280, 0.7209, np.nan, 0.7263, 0.7281, 0.7285,],
#     'EUR/AUD': [ 1.6232, 1.6321, 1.6221, 1.6282, np.nan, 1.6288,],
#     }
# index = [ '2020-09-08', '2020-09-09', '2020-09-10', '2020-09-11', '2020-09-14', '2020-09-15',]
# df = pd.DataFrame(data, index)
#
# new_df = df.copy()
# new_df.loc['1', :] = 1
# # print(df.loc['AUD/USD'])
#
# import pandas as pd
# import numpy as np
#
# csv_file = 'cars.csv'
# csv_data = pd.read_csv(csv_file,low_memory=False)
# csv_df = pd.DataFrame(csv_data)
# # print(csv_df)
# print(csv_df.mean())
# mean_car = csv_df['CAR'].mean()
# print(mean_car)
# # Calculate the squared deviations from the mean
# csv_df ['Squared Deviation'] = (csv_df['CAR'] - mean_car) ** 2
#
# # Calculate the sum of squared deviations
# sum_of_squared_deviations = csv_df['Squared Deviation'].sum()
# print(sum_of_squared_deviations.round(4))
#
# print(csv_df.var())
# # Calculate the variance of CAR
# variance_car = csv_df['Squared Deviation'].sum() / (len(csv_df) - 1)
#
# print(f"Variance of CAR: {variance_car:.4f}")
#
# print(csv_df.std())
# import math
#
# # Calculate the standard deviation of CAR
# std_dev_car = math.sqrt(variance_car)
#
# print(f"Standard Deviation of CAR: {std_dev_car:.4f}")
#
# root_n = len(csv_df['CAR'])**0.5
# t_statistic = -0.0120/(0.0955/root_n)
# print(t_statistic)
# # Given values
# # Given values
# # CAR = csv_df['CAR'].iloc[-1]  # The final cumulative abnormal return
# # expected_return = 0  # The expected return under the null hypothesis (as mentioned)
# #
# # # Calculate the t-statistic
# # t_statistic = (CAR - expected_return) / (std_dev_car / math.sqrt(len(csv_df)))
# #
# # print(f"Corrected t-Statistic: {t_statistic:.4f}")



# print(f"Total Sum of Squared Deviations: {sum_of_squared_deviations:.4f}")


import datetime as dt


def time_it(func, parms):
    start_time = dt.datetime.now()

    func(**parms)

    end_time = dt.datetime.now()

    elapsed_time = end_time - start_time

    days = elapsed_time.days
    seconds = elapsed_time.seconds
    microseconds = elapsed_time.microseconds

    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    result_str = _mk_msg(days, hours, minutes, seconds + microseconds / 1e6)

    return result_str


# Example usage:
def test_function(secs):
    import time
    time.sleep(secs)


def _test_time_it():
    import time
    print("Note: It will take about 1 min to execute this test function...")

    def _my_func(secs):
        time.sleep(secs)

    res = time_it(_my_func, {'secs': 64})
    print(res)


if __name__ == "__main":
    _test_time_it()
