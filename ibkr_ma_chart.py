from ib_insync import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statistics import stdev
from datetime import date
today_date = date.today().strftime('%m-%d-%y')


ib = IB()

# use this for IB Gateway
ib.connect('127.0.0.1', 4001, clientId=1)

# # use this for TWS Workstation
# ib.connect('127.0.0.1', 7497, clientId=1)

#removes duplicate chart posts
hits = []

# list of securities to cycle through
SMA9_securities = [
    ['MSOS', 'ARCA'],
    ['CGC', 'NASDAQ'],
    ['CRON', 'NASDAQ'],
    ['BHP', 'NYSE'],
    ['ESTC', 'NYSE'],
    ['ETSY', 'NASDAQ'],
    ['FNV', 'NYSE'],
    ['GDX', 'ARCA'],
    ['GOLD', 'NYSE'],
    ['IWM', 'ARCA'],
    ['JO', 'ARCA'],
    ['TLRY', 'NASDAQ'],
    ['TLT', 'NASDAQ'],
    ['BABA', 'NYSE'],
    ['BGNE', 'NASDAQ'],
    ['BILI', 'NASDAQ'],
    ['DQ', 'NYSE'],
    ['FUTU', 'NASDAQ'],
    ['FXI', 'ARCA'],
    ['GDS', 'NASDAQ'],
    ['HTHT', 'NASDAQ'],
    ['IQ', 'NASDAQ'],
    ['JMIA', 'NYSE'],
    ['KWEB', 'ARCA'],
    ['MCHI', 'NASDAQ'],
    ['NIU', 'NASDAQ'],
    ['NTES', 'NASDAQ'],
    ['SOL', 'NYSE'],
    ['TAL', 'NYSE'],
    ['VNET', 'NASDAQ'],
    ['ZLAB', 'NASDAQ'],
    ['ZTO', 'NYSE'],
    ['MU', 'NASDAQ'],
    ['LRCX', 'NASDAQ'],
    ['KLAC', 'NASDAQ'],
    ['TDOC', 'NYSE'],
    ['GRWG', 'NASDAQ'],
    ['PLUG', 'NASDAQ'],
    ['FCEL', 'NASDAQ'],
    ['TSLA', 'NASDAQ'],
    ['XPEV', 'NYSE'],
    ['LI', 'NASDAQ'],
    ['CHWY', 'NYSE'],
    ['BIDU', 'NASDAQ'],
    ['CTEC', 'NASDAQ'],
    ['XLE', 'ARCA'],
    ['UUP', 'ARCA'],
    ['USO', 'ARCA'],
    ['SPCE', 'NYSE'],
    ['IRDM', 'NASDAQ'],
    ['RIOT', 'NASDAQ'],
    ['DDD', 'NYSE'],
    ['IBB', 'NASDAQ'],
    ['ATVI', 'NASDAQ'],
    ['MARA', 'NASDAQ'],
    ['DADA', 'NASDAQ']
]

SMA20_securities = [
    ['CAT', 'NYSE'],
    ['VFF', 'NASDAQ'],
    ['OIH', 'ARCA'],
    ['XLF', 'ARCA'],
    ['CRWD', 'NASDAQ'],
    ['RIO', 'NYSE'],
    ['DIA', 'ARCA'],#############
    ['EBAY', 'NASDAQ'],
    ['EEM', 'ARCA'],
    ['FVRR', 'NYSE'],
    ['XPER', 'NASDAQ'],
    ['ROKU', 'NASDAQ'],
    ['SPY', 'ARCA'],
    ['XRT', 'ARCA'],
    ['ZS', 'NASDAQ'],
    ['VIPS', 'NYSE'],
    ['MLM', 'NYSE'],
    ['TAN', 'ARCA'],
    ['PYPL', 'NASDAQ'],
    ['APPS', 'NASDAQ'],
    ['PENN', 'NASDAQ'],
    ['MELI', 'NASDAQ'],
    ['JPM', 'NYSE'],
    ['ENPH', 'NASDAQ'],
    ['PBW', 'ARCA'],
    ['ICLN', 'NASDAQ'],
    ['SPWR', 'NASDAQ'],
    ['BLNK', 'NASDAQ'],
    ['LMND', 'NYSE'],
    ['CYBR', 'NASDAQ'],
    ['SKLZ', 'NYSE'],
    ['NXPI', 'NASDAQ'],
    ['ARKK', 'ARCA'],
    ['MGNI', 'NASDAQ'],
    ['IWB', 'ARCA'],
    ['YOLO', 'ARCA'],
    ['THCX', 'ARCA'],
    ['MJ', 'ARCA'],
    ['APHA', 'NASDAQ'],
    ['TLRY', 'NASDAQ'],
    ['MAXR', 'NYSE'],
    ['SRAC', 'NASDAQ'],
    ['DE', 'NYSE']
]

SMA50_securities = [
    ['SLV', 'ARCA'],
    ['AAPL', 'NASDAQ'],
    ['BBY', 'NYSE'],
    ['CSIQ', 'NASDAQ'],
    ['DDOG', 'NASDAQ'],
    ['UUUU', 'AMEX'],
    ['CCJ', 'NYSE'],
    ['NXE', 'AMEX'],
    ['DECK', 'NYSE'],
    ['DOCU', 'NASDAQ'],
    ['FSLR', 'NASDAQ'],
    ['GPS', 'NYSE'],
    ['HD', 'NYSE'],
    ['LOW', 'NYSE'],
    ['NET', 'NYSE'],
    ['PINS', 'NYSE'],
    ['PTON', 'NASDAQ'],
    ['QCOM', 'NASDAQ'],
    ['QQQ', 'NYSE'],
    ['RUN', 'NASDAQ'],
    ['SBUX', 'NASDAQ'],
    ['SMH', 'NASDAQ'],
    ['SNAP', 'NYSE'],
    ['SQ', 'NYSE'],
    ['TGT', 'NYSE'],
    ['TWLO', 'NYSE'],
    ['UNP', 'NYSE'],
    ['XHB', 'ARCA'],
    ['Z', 'NASDAQ'],
    ['EDU', 'NYSE'],
    ['JD', 'NASDAQ'],
    ['NIO', 'NYSE'],
    ['PDD', 'NASDAQ'],
    # ['FUBO', 'NYSE'],
    ['IGV', 'BATS'],
    ['TEAM', 'NASDAQ'],
    ['SEDG', 'NASDAQ'],
    ['INTU', 'NASDAQ'],
    ['GOOGL', 'NASDAQ'],
    ['NVAX', 'NASDAQ'],
    ['OKTA', 'NASDAQ'],
    ['SE', 'NYSE'],
    ['CHDN', 'NASDAQ'],
    ['CGC', 'NASDAQ'],
    ['IIPR', 'NYSE'],
    ['ONEM', 'NASDAQ'],
    ['ANTM', 'NYSE'],
    ['FTCH', 'NYSE'],
    # ['PLTR', 'NYSE'],
    ['ACB', 'NYSE'],
    ['ZI', 'NASDAQ'],
    ['SHOP', 'NYSE'],
    ['LAZR', 'NASDAQ'],
    ['CRSR', 'NASDAQ'],
    ['MDB', 'NASDAQ'],
    ['FTNT', 'NASDAQ'],
    ['BZH', 'NYSE'],
    ['XLK', 'ARCA']
]

SMA200_securities = [
    ['NEM', 'NYSE'],
    ['GLD', 'ARCA'],
    ['ADBE', 'NASDAQ'],
    ['COST', 'ARCA'],
    ['FSLY', 'NYSE'],
    ['MSFT', 'NASDAQ'],
    ['NFLX', 'NASDAQ'],
    ['NVDA', 'NASDAQ'],
    ['PG', 'NYSE'],
    ['TTD', 'NASDAQ'],
    ['TWTR', 'NYSE'],
    ['UPS', 'NYSE'],
    ['WMT', 'NYSE'],
    ['DOYU', 'NASDAQ'],
    ['JKS', 'NYSE'],
    ['NFLX', 'NASDAQ'],
    ['FB', 'NASDAQ'],
    ['CRM', 'NYSE'],
    ['AMZN', 'NASDAQ'],
    ['ZM', 'NASDAQ'],
    ['MRNA', 'NASDAQ'],
    ['AMD', 'NASDAQ']
]


# post buy charts for securities under the 200SMA
def ma_chart_9(tickerCapString, primeExchangeCapString, numDailyTicks):

    # create a contract for the security being charted
    stock = Stock(tickerCapString, 'SMART', 'USD', primaryExchange = primeExchangeCapString)
    bars = ib.reqHistoricalData(
        stock, endDateTime='', durationStr='365 D', #365days max
        barSizeSetting='1 day', whatToShow='MIDPOINT', useRTH=True)

    # convert to indexable dictionary:
    tree = util.tree(bars)

    # create a list of closing prices from pulled data to calculate MA plot pts
    closing_prices = []
    for day in range(len(tree)):
        closing_prices.append((tree[day]['BarData']['close']))

    # create 9SMA plot points for comparison
    ma_length_9 = 9
    i = 0
    averages_9 = []
    while i < len(closing_prices) - ma_length_9 + 1:
        this_window = closing_prices[i : i + ma_length_9]
        window_average = round(sum(this_window) / ma_length_9, 2)
        averages_9.append(window_average)
        i += 1

    # if security is above significant MA pass, if security is below MA post chart
    if closing_prices[len(closing_prices)-1] < (1 * averages_9[len(averages_9)-1]):
        hits.append(tickerCapString)

        # build other MAs to build chart if buy chart is to be posted
        # create 20SMA plot points
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

        # create 50SMA plot points
        ma_length_50 = 50
        i = 0
        averages_50 = []
        while i < len(closing_prices) - ma_length_50 + 1:
            this_window = closing_prices[i : i + ma_length_50]
            window_average = round(sum(this_window) / ma_length_50, 2)
            averages_50.append(window_average)
            i += 1

        # create 200SMA plot points
        ma_length_200 = 200
        i = 0
        averages_200 = []
        while i < len(closing_prices) - ma_length_200 + 1:
            this_window = closing_prices[i : i + ma_length_200]
            window_average = round(sum(this_window) / ma_length_200, 2)
            averages_200.append(window_average)
            i += 1

        # generate chart and buy recomendation
        plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
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
        # plt.show()
        plt.savefig(f'''{tickerCapString}_{ma_length_9}_{today_date}.pdf''', bbox_inches='tight')
    else:
        print(f'''{tickerCapString} not in buying range.''')



# post buy charts for securities under the 200SMA
def ma_chart_200(tickerCapString, primeExchangeCapString, numDailyTicks):

    # create a contract for the security being charted
    stock = Stock(tickerCapString, 'SMART', 'USD', primaryExchange = primeExchangeCapString)
    bars = ib.reqHistoricalData(
        stock, endDateTime='', durationStr='365 D', #365days max
        barSizeSetting='1 day', whatToShow='MIDPOINT', useRTH=True)

    # convert to indexable dictionary:
    tree = util.tree(bars)

    # create a list of closing prices from pulled data to calculate MA plot pts
    closing_prices = []
    for day in range(len(tree)):
        closing_prices.append((tree[day]['BarData']['close']))

    # create 200SMA plot points for comparison
    ma_length_200 = 200
    i = 0
    averages_200 = []
    while i < len(closing_prices) - ma_length_200 + 1:
        this_window = closing_prices[i : i + ma_length_200]
        window_average = round(sum(this_window) / ma_length_200, 2)
        averages_200.append(window_average)
        i += 1

    # if security is above significant MA pass, if security is below post buy chart/
    # add to hits list to avoid duplicates
    if closing_prices[len(closing_prices)-1] < (1 * (averages_200[len(averages_200)-1])):
        hits.append(tickerCapString)

        # build other MAs to build chart if buy chart is to be posted
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

        # create 50SMA plot points
        ma_length_50 = 50
        i = 0
        averages_50 = []
        while i < len(closing_prices) - ma_length_50 + 1:
            this_window = closing_prices[i : i + ma_length_50]
            window_average = round(sum(this_window) / ma_length_50, 2)
            averages_50.append(window_average)
            i += 1

        # generate chart and buy recomendation
        plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
        util.barplot(bars[-numDailyTicks:], upColor='green', downColor='red')
        plt.plot(range(len(bb_upper[-numDailyTicks:])), bb_upper[-numDailyTicks:], c='#ff0000', label='2.5 Upper BB')
        plt.plot(range(len(bb_lower[-numDailyTicks:])), bb_lower[-numDailyTicks:], c='#ff0000', label='2.5 Lower BB')
        plt.plot(range(len(averages_50[-numDailyTicks:])), averages_50[-numDailyTicks:], c='#04ff00', label='50SMA')
        plt.plot(range(len(averages_200[-numDailyTicks:])), averages_200[-numDailyTicks:], c='#0000ff', label='200SMA')
        plt.title(f'''{tickerCapString} below the {ma_length_200}SMA... Buy Alert.''')
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.legend()
        plt.savefig(f'''{tickerCapString}_{ma_length_200}_{today_date}.pdf''', bbox_inches='tight')
        # plt.show()
        # plt.savefig('test_chart.png')
    else:
        print(f'''{tickerCapString} not in buying range''')



# post buy charts for securities under the 20SMA
def ma_chart_20(tickerCapString, primeExchangeCapString, numDailyTicks):

    # create a contract for the security being charted
    stock = Stock(tickerCapString, 'SMART', 'USD', primaryExchange = primeExchangeCapString)
    bars = ib.reqHistoricalData(
        stock, endDateTime='', durationStr='365 D', #365days max
        barSizeSetting='1 day', whatToShow='MIDPOINT', useRTH=True)

    # convert to indexable dictionary:
    tree = util.tree(bars)

    # create a list of closing prices from pulled data to calculate MA plot pts
    closing_prices = []
    for day in range(len(tree)):
        closing_prices.append((tree[day]['BarData']['close']))

    # create 20SMA plot points for comparison
    ma_length_20 = 20
    i = 0
    averages_20 = []
    while i < len(closing_prices) - ma_length_20 + 1:
        this_window = closing_prices[i : i + ma_length_20]
        window_average = round(sum(this_window) / ma_length_20, 2)
        averages_20.append(window_average)
        i += 1

    # if security is above significant MA pass, if security is below post buy chart/
    # add to hits list to avoid duplicates
    if closing_prices[len(closing_prices)-1] < (1 * averages_20[len(averages_20)-1]):
        hits.append(tickerCapString)

        # build other MAs to build chart if buy chart is to be posted
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

        # create 50SMA plot points
        ma_length_50 = 50
        i = 0
        averages_50 = []
        while i < len(closing_prices) - ma_length_50 + 1:
            this_window = closing_prices[i : i + ma_length_50]
            window_average = round(sum(this_window) / ma_length_50, 2)
            averages_50.append(window_average)
            i += 1

        # create 200SMA plot points
        ma_length_200 = 200
        i = 0
        averages_200 = []
        while i < len(closing_prices) - ma_length_200 + 1:
            this_window = closing_prices[i : i + ma_length_200]
            window_average = round(sum(this_window) / ma_length_200, 2)
            averages_200.append(window_average)
            i += 1

        # generate chart and buy recomendation
        plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
        util.barplot(bars[-numDailyTicks:], upColor='green', downColor='red')
        plt.plot(range(len(averages_20[-numDailyTicks:])), averages_20[-numDailyTicks:], c='#ffbb00', label='20SMA')
        plt.plot(range(len(bb_upper[-numDailyTicks:])), bb_upper[-numDailyTicks:], c='#ff0000', label='2.5 Upper BB')
        plt.plot(range(len(bb_lower[-numDailyTicks:])), bb_lower[-numDailyTicks:], c='#ff0000', label='2.5 Lower BB')
        plt.plot(range(len(averages_50[-numDailyTicks:])), averages_50[-numDailyTicks:], c='#04ff00', label='50SMA')
        plt.plot(range(len(averages_200[-numDailyTicks:])), averages_200[-numDailyTicks:], c='#0000ff', label='200SMA')
        plt.title(f'''{tickerCapString}, {ma_length_20}SMA SUPPORT, BUY ALERT.''')
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.legend()
        # plt.show()
        plt.savefig(f'''{tickerCapString}_{ma_length_20}_{today_date}.pdf''', bbox_inches='tight')
    else:
        print(f'''{tickerCapString} not in buying range.''')



# post buy charts for securities under the 50SMA
def ma_chart_50(tickerCapString, primeExchangeCapString, numDailyTicks):

    # create a contract for the security being charted
    stock = Stock(tickerCapString, 'SMART', 'USD', primaryExchange = primeExchangeCapString)
    bars = ib.reqHistoricalData(
        stock, endDateTime='', durationStr='365 D', #365days max
        barSizeSetting='1 day', whatToShow='MIDPOINT', useRTH=True)

    # convert to indexable dictionary:
    tree = util.tree(bars)

    # create a list of closing prices from pulled data to calculate MA plot pts
    closing_prices = []
    for day in range(len(tree)):
        closing_prices.append((tree[day]['BarData']['close']))

    # create 50SMA plot points for comparison
    ma_length_50 = 50
    i = 0
    averages_50 = []
    while i < len(closing_prices) - ma_length_50 + 1:
        this_window = closing_prices[i : i + ma_length_50]
        window_average = round(sum(this_window) / ma_length_50, 2)
        averages_50.append(window_average)
        i += 1

    # if security is above significant MA pass, if security is below post buy chart/
    # add to hits list to avoid duplicates
    if closing_prices[len(closing_prices)-1] < (1 * (averages_50[len(averages_50)-1])):
        hits.append(tickerCapString)

        # build other MAs to build chart if buy chart is to be posted
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

        # create 200SMA plot points
        ma_length_200 = 200
        i = 0
        averages_200 = []
        while i < len(closing_prices) - ma_length_200 + 1:
            this_window = closing_prices[i : i + ma_length_200]
            window_average = round(sum(this_window) / ma_length_200, 2)
            averages_200.append(window_average)
            i += 1

        # generate chart and buy recomendation
        plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
        util.barplot(bars[-numDailyTicks:], upColor='green', downColor='red')
        plt.plot(range(len(bb_upper[-numDailyTicks:])), bb_upper[-numDailyTicks:], c='#ff0000', label='2.5 Upper BB')
        plt.plot(range(len(bb_lower[-numDailyTicks:])), bb_lower[-numDailyTicks:], c='#ff0000', label='2.5 Lower BB')
        plt.plot(range(len(averages_50[-numDailyTicks:])), averages_50[-numDailyTicks:], c='#04ff00', label='50SMA')
        plt.plot(range(len(averages_200[-numDailyTicks:])), averages_200[-numDailyTicks:], c='#0000ff', label='200SMA')
        plt.title(f'''{tickerCapString}, {ma_length_50}SMA SUPPORT, BUY ALERT.''')
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.legend()
        # plt.show()
        plt.savefig(f'''{tickerCapString}_{ma_length_50}_{today_date}.pdf''', bbox_inches='tight')
    else:
        print(f'''{tickerCapString} not in buying range''')


while True:
    print(hits)
    # cycle through list of 9SMA securities
    for ticker in range(len(SMA9_securities)):
        if SMA9_securities[ticker][0] not in hits:
            ma_chart_9(SMA9_securities[ticker][0], SMA9_securities[ticker][1], 150)
            ib.sleep(1)

    print(hits)
    # cycle through list of 20SMA securities
    for ticker in range(len(SMA20_securities)):
        if SMA20_securities[ticker][0] not in hits:
            ma_chart_20(SMA20_securities[ticker][0], SMA20_securities[ticker][1], 150)
            ib.sleep(1)

    print(hits)
    # cycle through list of 50SMA securities
    for ticker in range(len(SMA50_securities)):
        if SMA50_securities[ticker][0] not in hits:
            ma_chart_50(SMA50_securities[ticker][0], SMA50_securities[ticker][1], 150)
            ib.sleep(1)
    print(hits)

    # cycle through list of 200SMA securities
    for ticker in range(len(SMA200_securities)):
        if SMA200_securities[ticker][0] not in hits:
            ma_chart_200(SMA200_securities[ticker][0], SMA200_securities[ticker][1], 150)
            ib.sleep(1)

