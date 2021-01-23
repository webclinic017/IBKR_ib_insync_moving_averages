from ib_insync import *
import pandas as pd
from statistics import stdev
from datetime import datetime
import mplfinance as mpf

def fetch_data(ticker, prime_exch, data_barcount):
    stock = Stock(ticker, 'SMART', 'USD', primaryExchange = prime_exch)
    bars = ib.reqHistoricalData(
        stock, endDateTime='', durationStr=data_barcount, #365days max
        barSizeSetting='1 day', whatToShow='MIDPOINT', useRTH=True)
    bars = util.tree(bars)
    return bars

def extract_closing(singlestock_bardata):
    closing_prices = []
    for day in range(len(aapl_df)):
        closing_prices.append((singlestock_bardata[day]['BarData']['close']))
    return closing_prices

def create_masubplot(length, closing_prices):
    ma_length = length
    i = 0
    averages = {'data':[]}
    while i < len(closing_prices) - ma_length + 1:
        this_window = closing_prices[i : i + ma_length]
        window_average = round(sum(this_window) / ma_length, 2)
        averages['data'].append(window_average)
        i += 1
    return averages

def create_upperbb_subplot(closing_prices, period, std):
    length = period
    i = 0
    bb = {'data':[]}
    while i < len(closing_prices) - length + 1:
        this_window = closing_prices[i : i + length]
        window_bb = round((sum(this_window) / length) + (2.5 * stdev(this_window)), 2)
        bb['data'].append(window_bb)
        i += 1
    return bb

def create_lowerbb_subplot(closing_prices, period, std):
    length = period
    i = 0
    bb = {'data':[]}
    while i < len(closing_prices) - length + 1:
        this_window = closing_prices[i : i + length]
        window_bb = round((sum(this_window) / length) - (2.5 * stdev(this_window)), 2)
        bb['data'].append(window_bb)
        i += 1
    return bb

def reformat_IBdata(fetched_data, numofdays):
    reformatted_data = {}
    reformatted_data['Date'] = []
    reformatted_data['Open'] = []
    reformatted_data['High'] = []
    reformatted_data['Low'] = []
    reformatted_data['Close'] = []
    for dict in range(len(aapl_df)-numofdays,len(aapl_df)):
        reformatted_data['Date'].append(datetime.strptime(str(aapl_df[dict]['BarData']['date']), '%Y-%m-%d'))
        reformatted_data['Open'].append(aapl_df[dict]['BarData']['open'])
        reformatted_data['High'].append(aapl_df[dict]['BarData']['high'])
        reformatted_data['Low'].append(aapl_df[dict]['BarData']['low'])
        reformatted_data['Close'].append(aapl_df[dict]['BarData']['close'])
    # print("reformatted data:", reformatted_data)
    pdata = pd.DataFrame.from_dict(reformatted_data)
    pdata.set_index('Date', inplace=True)
    return pdata
    print(pdata)

def plot_pdata(pdata, sma9, sma20, sma50, sma200, lowerbb, upperbb, numofdays):
    sma9dict = mpf.make_addplot(sma9['data'][-numofdays:], color='#c87cff')
    sma20dict = mpf.make_addplot(sma20['data'][-numofdays:], color='#f28c06')
    sma50dict = mpf.make_addplot(sma50['data'][-numofdays:], color='#3a7821')
    sma200dict = mpf.make_addplot(sma200['data'][-numofdays:], color='#483e8b')
    lowerbbdict = mpf.make_addplot(lowerbb['data'][-numofdays:], color='#b90c0c')
    upperbbdict = mpf.make_addplot(upperbb['data'][-numofdays:], color='#b90c0c')
    mpf.plot(pdata, type='candle', style='charles',
                addplot=[sma9dict, sma20dict, sma50dict, sma200dict, lowerbbdict, upperbbdict],
                figscale=.9,
                tight_layout=False)
                # savefig='test-mplfiance.png')


ib = IB()
ib.connect('127.0.0.1', 4001, clientId=1)

aapl_df = fetch_data('AAPL', 'NASDAQ', '365 D')
aapl_closings = extract_closing(aapl_df)
aapl_9sma = create_masubplot(9, aapl_closings)
aapl_20sma = create_masubplot(20, aapl_closings)
aapl_50sma = create_masubplot(50, aapl_closings)
aapl_200sma = create_masubplot(200, aapl_closings)
aapl_lowerbb = create_lowerbb_subplot(aapl_closings, 20, 2.5)
aapl_upperbb = create_upperbb_subplot(aapl_closings, 20, 2.5)
aapl_pdata = reformat_IBdata(aapl_df, 120)
plot_pdata(aapl_pdata, aapl_9sma, aapl_20sma, aapl_50sma, aapl_200sma, aapl_lowerbb, aapl_upperbb, 120)
