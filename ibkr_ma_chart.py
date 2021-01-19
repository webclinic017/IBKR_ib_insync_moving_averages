from ib_insync import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statistics import stdev


ib = IB()
# use this for IB Gateway
ib.connect('127.0.0.1', 4001, clientId=1)

# # use this for TWS Workstation
# ib.connect('127.0.0.1', 7497, clientId=1)

#removes duplicate chart posts
hits = []

# list of securities to cycle through
SMA9_securities = [
    ['VFF', 'NASDAQ'],
    ['MSOS', 'ARCA'],
    ['OIH', 'ARCA'],
    ['CGC', 'NASDAQ'],
    ['CRON', 'NASDAQ'],
    ['BHP', 'ARCA'],
    ['DE', 'ARCA'],
    ['ESTC', 'ARCA'],
    ['ETSY', 'NASDAQ'],
    ['FNV', 'ARCA'],
    ['GDX', 'ARCA'],
    ['GOLD', 'ARCA'],
    ['IWM', 'ARCA'],
    ['JO', 'ARCA'],
    ['TLRY', 'NASDAQ'],
    ['TLT', 'NASDAQ'],
    ['BABA', 'ARCA'],
    ['BGNE', 'NASDAQ'],
    ['BILI', 'NASDAQ'],
    ['DQ', 'ARCA'],
    ['FUTU', 'NASDAQ'],
    ['FXI', 'ARCA'],
    ['GDS', 'NASDAQ'],
    ['HTHT', 'NASDAQ'],
    ['IQ', 'NASDAQ'],
    ['JMIA', 'ARCA'],
    ['KWEB', 'ARCA'],
    ['MCHI', 'NASDAQ'],
    ['NIU', 'NASDAQ'],
    ['NTES', 'NASDAQ'],
    ['SOL', 'ARCA'],
    ['TAL', 'ARCA'],
    ['VNET', 'NASDAQ'],
    ['ZLAB', 'NASDAQ'],
    ['ZTO', 'ARCA']
]

SMA20_securities = [
    ['CAT', 'ARCA'],
    ['CRWD', 'NASDAQ'],
    ['RIO', 'ARCA'],
    ['DIA', 'ARCA'],#############
    ['EBAY', 'NASDAQ'],
    ['EEM', 'ARCA'],
    ['FVRR', 'NASDAQ'],
    ['ROKU', 'NASDAQ'],
    ['SPY', 'ARCA'],
    ['XRT', 'ARCA'],
    ['ZS', 'NASDAQ'],
    ['VIPS', 'NASDAQ']
]

SMA50_securities = [
    ['SLV', 'ARCA'],
    ['AAPL', 'NASDAQ'],
    ['BBY', 'ARCA'],
    ['CSIQ', 'NASDAQ'],
    ['DDOG', 'NASDAQ'],
    ['UUUU', 'ARCA'],
    ['CCJ', 'ARCA'],
    ['NXE', 'ARCA'],
    ['DECK', 'ARCA'],
    ['DOCU', 'NASDAQ'],
    ['FSLR', 'NASDAQ'],
    ['GPS', 'ARCA'],
    ['HD', 'ARCA'],
    ['LOW', 'ARCA'],
    ['NET', 'NASDAQ'],
    ['NFLX', 'NASDAQ'],
    ['PINS', 'NASDAQ'],
    ['PTON', 'NASDAQ'],
    ['QCOM', 'NASDAQ'],
    ['QQQ', 'ARCA'],
    ['RUN', 'NASDAQ'],
    ['SBUX', 'ARCA'],
    ['SMH', 'ARCA'],
    ['SNAP', 'NASDAQ'],
    ['SQ', 'NASDAQ'],
    ['TGT', 'ARCA'],
    ['TWLO', 'NASDAQ'],
    ['UNP', 'ARCA'],
    ['XHB', 'ARCA'],
    ['Z', 'NASDAQ'],
    ['EDU', 'NASDAQ'],
    ['JD', 'NASDAQ'],
    ['NIO', 'NASDAQ'],
    ['PDD', 'NASDAQ']
]

SMA200_securities = [
    ['NEM', 'ARCA'],
    ['GLD', 'ARCA'],
    ['ADBE', 'NASDAQ'],
    ['COST', 'ARCA'],
    ['FSLY', 'NASDAQ'],
    ['MSFT', 'NASDAQ'],
    ['NFLX', 'NASDAQ'],
    ['NVDA', 'NASDAQ'],
    ['PG', 'ARCA'],
    ['TTD', 'NASDAQ'],
    ['TWTR', 'NASDAQ'],
    ['UPS', 'ARCA'],
    ['WMT', 'ARCA'],
    ['DOYU', 'NASDAQ'],
    ['JKS', 'NASDAQ']
]

# print charts for securities under the 9SMA
def ma_chart_9(tickerCapString, primeExchangeCapString, numDailyTicks):
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
    # create accompanying 9SMA plot points
    ma_length_9 = 9
    i = 0
    averages_9 = []
    while i < len(closing_prices) - ma_length_9 + 1:
        this_window = closing_prices[i : i + ma_length_9]
        window_average = round(sum(this_window) / ma_length_9, 2)
        averages_9.append(window_average)
        i += 1
    # create accompanying 20SMA plot points
    ma_length_20 = 20
    i = 0
    averages_20 = []
    while i < len(closing_prices) - ma_length_20 + 1:
        this_window = closing_prices[i : i + ma_length_20]
        window_average = round(sum(this_window) / ma_length_20, 2)
        averages_20.append(window_average)
        i += 1
    # create upper bollinger band plot points
    bb_length_upper = 20
    i = 0
    bb_upper = []
    while i < len(closing_prices) - bb_length_upper + 1:
        this_window = closing_prices[i : i + bb_length_upper]
        window_bb = round((sum(this_window) / bb_length_upper) + (2.5 * stdev(this_window)), 2)
        bb_upper.append(window_bb)
        i += 1
    # create lower bollinger band plot points
    bb_length_lower = 20
    i = 0
    bb_lower = []
    while i < len(closing_prices) - bb_length_lower + 1:
        this_window = closing_prices[i : i + bb_length_lower]
        window_bb = round((sum(this_window) / bb_length_upper) - (2.5 * stdev(this_window)), 2)
        bb_lower.append(window_bb)
        i += 1
    # create accompanying 50SMA plot points
    ma_length_50 = 50
    i = 0
    averages_50 = []
    while i < len(closing_prices) - ma_length_50 + 1:
        this_window = closing_prices[i : i + ma_length_50]
        window_average = round(sum(this_window) / ma_length_50, 2)
        averages_50.append(window_average)
        i += 1
    # create accompanying 200SMA plot points
    ma_length_200 = 200
    i = 0
    averages_200 = []
    while i < len(closing_prices) - ma_length_200 + 1:
        this_window = closing_prices[i : i + ma_length_200]
        window_average = round(sum(this_window) / ma_length_200, 2)
        averages_200.append(window_average)
        i += 1
    # if security is above significant MA pass, if security is below MA post chart
    if closing_prices[len(closing_prices)-1] < (1 * averages_9[len(averages_9)-1]):
        hits.append(tickerCapString)
        plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
        # plot candlestick stock chart against MA line
        util.barplot(bars[-numDailyTicks:], upColor='green', downColor='red')
        plt.plot(range(len(averages_9[-numDailyTicks:])), averages_9[-numDailyTicks:], c='#ed85ff', label='9SMA')
        plt.plot(range(len(averages_20[-numDailyTicks:])), averages_20[-numDailyTicks:], c='#ffbb00', label='20SMA')
        plt.plot(range(len(bb_upper[-numDailyTicks:])), bb_upper[-numDailyTicks:], c='#ff0000', label='2.5 Upper BB')
        plt.plot(range(len(bb_lower[-numDailyTicks:])), bb_lower[-numDailyTicks:], c='#ff0000', label='2.5 Lower BB')
        plt.plot(range(len(averages_50[-numDailyTicks:])), averages_50[-numDailyTicks:], c='#04ff00', label='50SMA')
        plt.plot(range(len(averages_200[-numDailyTicks:])), averages_200[-numDailyTicks:], c='#0000ff', label='200SMA')
        plt.title(f'''{tickerCapString} below the {ma_length_9}SMA... Buy Alert.''')
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
        # plt.savefig('test_chart.png')
    else:
        print(f'''{tickerCapString} not in buying range.''')

# print charts for securities under the 200SMA
def ma_chart_200(tickerCapString, primeExchangeCapString, numDailyTicks):
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
    # create upper bollinger band plot points
    bb_length_upper = 20
    i = 0
    bb_upper = []
    while i < len(closing_prices) - bb_length_upper + 1:
        this_window = closing_prices[i : i + bb_length_upper]
        window_bb = round((sum(this_window) / bb_length_upper) + (2.5 * stdev(this_window)), 2)
        bb_upper.append(window_bb)
        i += 1
    # create lower bollinger band plot points
    bb_length_lower = 20
    i = 0
    bb_lower = []
    while i < len(closing_prices) - bb_length_lower + 1:
        this_window = closing_prices[i : i + bb_length_lower]
        window_bb = round((sum(this_window) / bb_length_upper) - (2.5 * stdev(this_window)), 2)
        bb_lower.append(window_bb)
        i += 1
    # create accompanying 50SMA plot points
    ma_length_50 = 50
    i = 0
    averages_50 = []
    while i < len(closing_prices) - ma_length_50 + 1:
        this_window = closing_prices[i : i + ma_length_50]
        window_average = round(sum(this_window) / ma_length_50, 2)
        averages_50.append(window_average)
        i += 1
    # create accompanying 100SMA plot points
    ma_length_100 = 100
    i = 0
    averages_100 = []
    while i < len(closing_prices) - ma_length_100 + 1:
        this_window = closing_prices[i : i + ma_length_100]
        window_average = round(sum(this_window) / ma_length_100, 2)
        averages_100.append(window_average)
        i += 1
    # create accompanying 200SMA plot points
    ma_length_200 = 200
    i = 0
    averages_200 = []
    while i < len(closing_prices) - ma_length_200 + 1:
        this_window = closing_prices[i : i + ma_length_200]
        window_average = round(sum(this_window) / ma_length_200, 2)
        averages_200.append(window_average)
        i += 1
    # if security is above significant MA pass, if security is below MA post chart
    if closing_prices[len(closing_prices)-1] < (1 * (averages_200[len(averages_200)-1])):
        hits.append(tickerCapString)
        plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
        # plot candlestick stock chart against MA line
        util.barplot(bars[-numDailyTicks:], upColor='green', downColor='red')
        plt.plot(range(len(bb_upper[-numDailyTicks:])), bb_upper[-numDailyTicks:], c='#ff0000', label='2.5 Upper BB')
        plt.plot(range(len(bb_lower[-numDailyTicks:])), bb_lower[-numDailyTicks:], c='#ff0000', label='2.5 Lower BB')
        plt.plot(range(len(averages_50[-numDailyTicks:])), averages_50[-numDailyTicks:], c='#04ff00', label='50SMA')
        plt.plot(range(len(averages_200[-numDailyTicks:])), averages_200[-numDailyTicks:], c='#0000ff', label='200SMA')
        plt.title(f'''{tickerCapString} below the {ma_length_200}SMA... Buy Alert.''')
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
        # plt.savefig('test_chart.png')
    else:
        print(f'''{tickerCapString} not in buying range''')

def ma_chart_20(tickerCapString, primeExchangeCapString, numDailyTicks):
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
    # create accompanying 20SMA plot points
    ma_length_20 = 20
    i = 0
    averages_20 = []
    while i < len(closing_prices) - ma_length_20 + 1:
        this_window = closing_prices[i : i + ma_length_20]
        window_average = round(sum(this_window) / ma_length_20, 2)
        averages_20.append(window_average)
        i += 1
    # create upper bollinger band plot points
    bb_length_upper = 20
    i = 0
    bb_upper = []
    while i < len(closing_prices) - bb_length_upper + 1:
        this_window = closing_prices[i : i + bb_length_upper]
        window_bb = round((sum(this_window) / bb_length_upper) + (2.5 * stdev(this_window)), 2)
        bb_upper.append(window_bb)
        i += 1
    # create lower bollinger band plot points
    bb_length_lower = 20
    i = 0
    bb_lower = []
    while i < len(closing_prices) - bb_length_lower + 1:
        this_window = closing_prices[i : i + bb_length_lower]
        window_bb = round((sum(this_window) / bb_length_upper) - (2.5 * stdev(this_window)), 2)
        bb_lower.append(window_bb)
        i += 1
    # create accompanying 50SMA plot points
    ma_length_50 = 50
    i = 0
    averages_50 = []
    while i < len(closing_prices) - ma_length_50 + 1:
        this_window = closing_prices[i : i + ma_length_50]
        window_average = round(sum(this_window) / ma_length_50, 2)
        averages_50.append(window_average)
        i += 1
    # create accompanying 200SMA plot points
    ma_length_200 = 200
    i = 0
    averages_200 = []
    while i < len(closing_prices) - ma_length_200 + 1:
        this_window = closing_prices[i : i + ma_length_200]
        window_average = round(sum(this_window) / ma_length_200, 2)
        averages_200.append(window_average)
        i += 1
    # if security is above significant MA pass, if security is below MA post chart
    if closing_prices[len(closing_prices)-1] < (1 * averages_20[len(averages_20)-1]):
        hits.append(tickerCapString)
        plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
        # plot candlestick stock chart against MA line
        util.barplot(bars[-numDailyTicks:], upColor='green', downColor='red')
        plt.plot(range(len(averages_20[-numDailyTicks:])), averages_20[-numDailyTicks:], c='#ffbb00', label='20SMA')
        plt.plot(range(len(bb_upper[-numDailyTicks:])), bb_upper[-numDailyTicks:], c='#ff0000', label='2.5 Upper BB')
        plt.plot(range(len(bb_lower[-numDailyTicks:])), bb_lower[-numDailyTicks:], c='#ff0000', label='2.5 Lower BB')
        plt.plot(range(len(averages_50[-numDailyTicks:])), averages_50[-numDailyTicks:], c='#04ff00', label='50SMA')
        plt.plot(range(len(averages_200[-numDailyTicks:])), averages_200[-numDailyTicks:], c='#0000ff', label='200SMA')
        plt.title(f'''{tickerCapString} below the {ma_length_20}SMA... Buy Alert.''')
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
        # plt.savefig('test_chart.png')
    else:
        print(f'''{tickerCapString} not in buying range.''')


def ma_chart_50(tickerCapString, primeExchangeCapString, numDailyTicks):
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
    # create upper bollinger band plot points
    bb_length_upper = 20
    i = 0
    bb_upper = []
    while i < len(closing_prices) - bb_length_upper + 1:
        this_window = closing_prices[i : i + bb_length_upper]
        window_bb = round((sum(this_window) / bb_length_upper) + (2.5 * stdev(this_window)), 2)
        bb_upper.append(window_bb)
        i += 1
    # create lower bollinger band plot points
    bb_length_lower = 20
    i = 0
    bb_lower = []
    while i < len(closing_prices) - bb_length_lower + 1:
        this_window = closing_prices[i : i + bb_length_lower]
        window_bb = round((sum(this_window) / bb_length_upper) - (2.5 * stdev(this_window)), 2)
        bb_lower.append(window_bb)
        i += 1
    # create accompanying 50SMA plot points
    ma_length_50 = 50
    i = 0
    averages_50 = []
    while i < len(closing_prices) - ma_length_50 + 1:
        this_window = closing_prices[i : i + ma_length_50]
        window_average = round(sum(this_window) / ma_length_50, 2)
        averages_50.append(window_average)
        i += 1
    # create accompanying 100SMA plot points
    ma_length_100 = 100
    i = 0
    averages_100 = []
    while i < len(closing_prices) - ma_length_100 + 1:
        this_window = closing_prices[i : i + ma_length_100]
        window_average = round(sum(this_window) / ma_length_100, 2)
        averages_100.append(window_average)
        i += 1
    # create accompanying 200SMA plot points
    ma_length_200 = 200
    i = 0
    averages_200 = []
    while i < len(closing_prices) - ma_length_200 + 1:
        this_window = closing_prices[i : i + ma_length_200]
        window_average = round(sum(this_window) / ma_length_200, 2)
        averages_200.append(window_average)
        i += 1
    # if security is above significant MA pass, if security is below MA post chart
    if closing_prices[len(closing_prices)-1] < (1 * (averages_50[len(averages_50)-1])):
        hits.append(tickerCapString)
        plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
        # plot candlestick stock chart against MA line
        util.barplot(bars[-numDailyTicks:], upColor='green', downColor='red')
        plt.plot(range(len(bb_upper[-numDailyTicks:])), bb_upper[-numDailyTicks:], c='#ff0000', label='2.5 Upper BB')
        plt.plot(range(len(bb_lower[-numDailyTicks:])), bb_lower[-numDailyTicks:], c='#ff0000', label='2.5 Lower BB')
        plt.plot(range(len(averages_50[-numDailyTicks:])), averages_50[-numDailyTicks:], c='#04ff00', label='50SMA')
        plt.plot(range(len(averages_200[-numDailyTicks:])), averages_200[-numDailyTicks:], c='#0000ff', label='200SMA')
        plt.title(f'''{tickerCapString} below the {ma_length_50}SMA... Buy Alert.''')
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
        # plt.savefig('test_chart.png')
    else:
        print(f'''{tickerCapString} not in buying range''')



print(hits)
# cycle through list of 9SMA securities
for ticker in range(len(SMA9_securities)):
    if SMA9_securities[ticker][0] not in hits:
        ma_chart_9(SMA9_securities[ticker][0], SMA9_securities[ticker][1], 150)
print(hits)
# cycle through list of 20SMA securities
for ticker in range(len(SMA20_securities)):
    if SMA20_securities[ticker][0] not in hits:
        ma_chart_20(SMA20_securities[ticker][0], SMA20_securities[ticker][1], 150)
print(hits)
# cycle through list of 50SMA securities
for ticker in range(len(SMA50_securities)):
    if SMA50_securities[ticker][0] not in hits:
        ma_chart_50(SMA50_securities[ticker][0], SMA50_securities[ticker][1], 150)
print(hits)
# cycle through list of 200SMA securities
for ticker in range(len(SMA200_securities)):
    if SMA200_securities[ticker][0] not in hits:
        ma_chart_200(SMA200_securities[ticker][0], SMA200_securities[ticker][1], 150)
print(hits)
