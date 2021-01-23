from ib_insync import *

import pandas as pd

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

import matplotlib.pyplot as plt
import mplfinance as mpf
from matplotlib.pylab import date2num

ib = IB()
ib.connect('127.0.0.1', 4001, clientId=1)

def fetch_data(ticker, prime_exch, data_barcount):
    stock = Stock(ticker, 'SMART', 'USD', primaryExchange = prime_exch)
    bars = ib.reqHistoricalData(
        stock, endDateTime='', durationStr=data_barcount, #365days max
        barSizeSetting='1 day', whatToShow='MIDPOINT', useRTH=True)
    bars = util.tree(bars)
    return bars

aapl_df = fetch_data('AAPL', 'NASDAQ', '365 D')

def extract_closing(singlestock_bardata):
    closing_prices = []
    for day in range(len(aapl_df)):
        closing_prices.append((singlestock_bardata[day]['BarData']['close']))
        return closing_prices

aapl_closings = extract_closing(aapl_df)

def reformat_IBdata(fetched_data):
    reformatted_data = {}
    reformatted_data['Date'] = []
    reformatted_data['Open'] = []
    reformatted_data['High'] = []
    reformatted_data['Low'] = []
    reformatted_data['Close'] = []
    for dict in range(len(aapl_df)):
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

aapl_pdata = reformat_IBdata(aapl_df)

def plot_pdata(pdata):
    mpf.plot(pdata, type='candle', style='charles',
                title='AAPL, Last 90 Days',
                ylabel='Price ($)',
                mav=(9,20,50,200))
# #             # savefig='test-mplfiance.png')

plot_pdata(aapl_pdata)


