from ib_insync import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ib = IB()
# use this for IB Gateway
ib.connect('127.0.0.1', 4001, clientId=1)

# # use this for TWS Workstation
# ib.connect('127.0.0.1', 7497, clientId=1)

# list of securities to cycle through
securities = [
    ['VFF', 'NASDAQ'],
    ['GDX', 'ARCA'],
    ['NEM', 'ARCA'],
    ['GOLD', 'ARCA'],
    ['MSOS', 'ARCA'],
    ['OIH', 'ARCA']
]

def ma_chart(tickerCapString, primeExchangeCapString, maLength, numDailyTicks):
    # create a contract for the security being charted
    stock = Stock(tickerCapString, 'SMART', 'USD', primaryExchange = primeExchangeCapString)
    bars = ib.reqHistoricalData(
        stock, endDateTime='', durationStr='365 D', #365days max
        barSizeSetting='1 day', whatToShow='MIDPOINT', useRTH=True)
    # convert to indexable dictionary:
    tree = util.tree(bars)

    # create a list of closing prices from pulled data to calculate accompanying...
    # ... moving average plot points
    closing_prices = []
    for day in range(len(tree)):
        closing_prices.append((tree[day]['BarData']['close']))

    # create accompanying moving average plot points
    ma_length = maLength
    i = 0
    averages = []
    while i < len(closing_prices) - ma_length + 1:
        this_window = closing_prices[i : i + ma_length]
        window_average = round(sum(this_window) / ma_length, 2)
        averages.append(window_average)
        i += 1
    # if security is above MA its rich, if security is below MA its cheap
    if closing_prices[len(closing_prices)-1] < averages[len(averages)-1]:
        # plot candlestick stock chart against MA line
        util.barplot(bars[-90:], upColor='green', downColor='red')
        plt.plot(range(len(averages[-numDailyTicks:])), averages[-numDailyTicks:])
        plt.title(f'''
    {tickerCapString} below the {maLength}SMA''')
    else:
        print(
f'''{tickerCapString} out of range.''')
    plt.show()
    # plt.savefig('test_chart.png')

# cycle through list of securities
for ticker in range(len(securities)):
    ma_chart(securities[ticker][0], securities[ticker][1], 9, 90)



