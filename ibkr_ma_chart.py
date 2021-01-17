from ib_insync import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ib = IB()
# use this for IB Gateway
ib.connect('127.0.0.1', 4001, clientId=1)

# # use this for TWS Workstation
# ib.connect('127.0.0.1', 7497, clientId=1)

# create a contract for the security being charted
nio = Stock('NIO', 'SMART', 'USD')#, primaryExchange = 'ARCA')
bars = ib.reqHistoricalData(
    nio, endDateTime='', durationStr='200 D',
    barSizeSetting='1 day', whatToShow='MIDPOINT', useRTH=True)

# convert to indexable dictionary:
tree = util.tree(bars)

# create a list of closing prices from pulled data to calculate accompanying...
# ... moving average plot points
closing_prices = []
for day in range(len(tree)):
    closing_prices.append((tree[day]['BarData']['close']))

# create accompanying moving average plot points
ma_length = 9
i = 0
averages = []
while i < len(closing_prices) - ma_length + 1:
    this_window = closing_prices[i : i + ma_length]
    window_average = round(sum(this_window) / ma_length, 2)
    averages.append(window_average)
    i += 1

# print(closing_prices)
# print(averages)
# print(len(closing_prices))
# print(len(averages))

# if security is above MA its rich, if security is below MA its cheap
if closing_prices[len(closing_prices)-1] < averages[len(averages)-1]:
    print('Stock is cheap.')
else:
    print('Stock is rich.')

# plot candlestick stock chart against MA line
util.barplot(bars[-90:], upColor='green', downColor='red')
plt.plot(range(len(averages[-90:])), averages[-90:])
plt.title('VFF under the 9EMA... stock is cheap')
plt.show()
# plt.savefig('test_chart.png')


# vff = Option('VFF', '20210319', 12, 'C', 'SMART')
# market_data = ib.reqMktData(vff, '', False, False,).dict()
# ib.sleep(2)
# print(market_data)
