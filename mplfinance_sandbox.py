from ib_insync import *

import pandas as pd

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

import talib

import matplotlib.pyplot as plt
import mplfinance as mpf
from matplotlib.pylab import date2num

ib = IB()

ib.connect('127.0.0.1', 4001, clientId=1)

stock = Stock('AAPL', 'SMART', 'USD', primaryExchange = 'NASDAQ')
bars = ib.reqHistoricalData(
    stock, endDateTime='', durationStr='365 D', #365days max
    barSizeSetting='1 day', whatToShow='MIDPOINT', useRTH=True)

aapl_df = util.df(bars)

mpf.plot(aapl_df[1:5], type='candle', style='charles',
            title='AAPL, Last 90 Days',
            ylabel='Price ($)',
            ylabel_lower='Shares \nTraded',
            volume=True,
            mav=(9,20,50,200))
            # savefig='test-mplfiance.png')
