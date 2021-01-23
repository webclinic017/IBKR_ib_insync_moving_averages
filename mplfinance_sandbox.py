from ib_insync import *
import pandas as pd
from statistics import stdev
from datetime import datetime
import mplfinance as mpf
from datetime import date
today_date = date.today().strftime('%m-%d-%y')

SMA9_securities = [
    ['MSOS', 'ARCA'],
    ['CGC', 'NASDAQ'],
    ['ESTC', 'NYSE'],
    ['ETSY', 'NASDAQ'],
    # ['FNV', 'NYSE'],
    # ['GDX', 'ARCA'],
    # ['GOLD', 'NYSE'],
    ['IWM', 'ARCA'],
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
    ['ZLAB', 'NASDAQ'],
    ['ZTO', 'NYSE'],
    ['MU', 'NASDAQ'],
    ['LRCX', 'NASDAQ'],
    ['KLAC', 'NASDAQ'],
    ['TDOC', 'NYSE'],
    ['XPEV', 'NYSE'],
    ['BIDU', 'NASDAQ'],
    ['CTEC', 'NASDAQ'],
    ['UUP', 'ARCA'],
    ['SPCE', 'NYSE'],
    ['IRDM', 'NASDAQ'],
    ['DDD', 'NYSE'],
    ['IBB', 'NASDAQ'],
    ['ATVI', 'NASDAQ'],
    ['DADA', 'NASDAQ']
]

SMA20_securities = [
    ['CAT', 'NYSE'],
    ['VFF', 'NASDAQ'],
    ['RIOT', 'NASDAQ'],
    ['CRON', 'NASDAQ'],
    ['XLF', 'ARCA'],
    ['CRWD', 'NASDAQ'],
    ['RIO', 'NYSE'],
    ['BHP', 'NYSE'],
    ['DIA', 'ARCA'],
    ['EBAY', 'NASDAQ'],
    ['CHWY', 'NYSE'],
    ['MARA', 'NASDAQ'],
    ['EEM', 'ARCA'],
    ['FVRR', 'NYSE'],
    ['VNET', 'NASDAQ'],
    ['GRWG', 'NASDAQ'],
    ['FCEL', 'NASDAQ'],
    ['XPER', 'NASDAQ'],
    ['ROKU', 'NASDAQ'],
    ['USO', 'ARCA'],
    ['SPY', 'ARCA'],
    ['XRT', 'ARCA'],
    ['ZS', 'NASDAQ'],
    ['VIPS', 'NYSE'],
    ['PLUG', 'NASDAQ'],
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
    ['JO', 'ARCA'],
    ['FSLR', 'NASDAQ'],
    ['GPS', 'NYSE'],
    ['HD', 'NYSE'],
    ['LOW', 'NYSE'],
    ['LI', 'NASDAQ'],
    ['NET', 'NYSE'],
    ['PINS', 'NYSE'],
    ['PTON', 'NASDAQ'],
    ['OIH', 'ARCA'],
    ['XLE', 'ARCA'],
    ['TSLA', 'NASDAQ'],
    ['QCOM', 'NASDAQ'],
    ['QQQ', 'NYSE'],
    ['RUN', 'NASDAQ'],
    ['BLNK', 'NASDAQ'],
    ['SBUX', 'NASDAQ'],
    ['SMH', 'NASDAQ'],
    ['SNAP', 'NYSE'],
    ['SQ', 'NYSE'],
    ['TGT', 'NYSE'],
    ['TWLO', 'NYSE'],
    ['UNP', 'NYSE'],
    ['XHB', 'ARCA'],
    ['Z', 'NASDAQ'],
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
    ['NEM', 'NYSE'],
    ['MDB', 'NASDAQ'],
    ['FTNT', 'NASDAQ'],
    ['BZH', 'NYSE'],
    ['XLK', 'ARCA']
]

SMA200_securities = [
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
    ['EDU', 'NYSE'],
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

hits = []

def fetch_data(ticker, prime_exch, data_barcount):
    stock = Stock(ticker, 'SMART', 'USD', primaryExchange = prime_exch)
    bars = ib.reqHistoricalData(
        stock, endDateTime='', durationStr=data_barcount, #365days max
        barSizeSetting='1 day', whatToShow='MIDPOINT', useRTH=True)
    bars = util.tree(bars)
    return bars

def extract_closing(singlestock_bardata):
    closing_prices = []
    for day in range(len(singlestock_bardata)):
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
    for dict in range(len(fetched_data)-numofdays,len(fetched_data)):
        reformatted_data['Date'].append(datetime.strptime(str(fetched_data[dict]['BarData']['date']), '%Y-%m-%d'))
        reformatted_data['Open'].append(fetched_data[dict]['BarData']['open'])
        reformatted_data['High'].append(fetched_data[dict]['BarData']['high'])
        reformatted_data['Low'].append(fetched_data[dict]['BarData']['low'])
        reformatted_data['Close'].append(fetched_data[dict]['BarData']['close'])
    # print("reformatted data:", reformatted_data)
    pdata = pd.DataFrame.from_dict(reformatted_data)
    pdata.set_index('Date', inplace=True)
    return pdata
    print(pdata)

def plot_pdata(pdata, sma9, sma20, sma50, sma200, lowerbb, upperbb, numofdays, ticker, defining_ma):
    sma9dict = mpf.make_addplot(sma9['data'][-numofdays:], color='#c87cff')
    sma20dict = mpf.make_addplot(sma20['data'][-numofdays:], color='#f28c06')
    sma50dict = mpf.make_addplot(sma50['data'][-numofdays:], color='#3a7821')
    sma200dict = mpf.make_addplot(sma200['data'][-numofdays:], color='#483e8b')
    lowerbbdict = mpf.make_addplot(lowerbb['data'][-numofdays:], color='#b90c0c')
    upperbbdict = mpf.make_addplot(upperbb['data'][-numofdays:], color='#b90c0c')
    mpf.plot(pdata, type='candle', style='charles',
                addplot=[sma9dict, sma20dict, sma50dict, sma200dict, lowerbbdict, upperbbdict],
                figscale=.9,
                tight_layout=False,
                savefig=f'''{ticker}_{defining_ma}SMA-RETEST_{today_date}.pdf''')




ib = IB()
ib.connect('127.0.0.1', 4001, clientId=1)

for security in range(len(SMA9_securities)):
    fetched_data = fetch_data(SMA9_securities[security][0], SMA9_securities[security][1], '365 D')
    closing_prices = extract_closing(fetched_data)
    sma9 = create_masubplot(9, closing_prices)
    if closing_prices[len(closing_prices)-1] < (1 * sma9['data'][len(sma9['data'])-1]):
        hits.append(SMA9_securities[security][0])
        sma20 = create_masubplot(20, closing_prices)
        sma50 = create_masubplot(50, closing_prices)
        sma200 = create_masubplot(200, closing_prices)
        lowerbb = create_lowerbb_subplot(closing_prices, 20, 2.5)
        upperbb = create_upperbb_subplot(closing_prices, 20, 2.5)
        pdata = reformat_IBdata(fetched_data, 120)
        plot_pdata(pdata, sma9, sma20, sma50, sma200, lowerbb, upperbb, 120, SMA9_securities[security][0], 9)
    else:
        print(f'''{SMA9_securities[security][0]} not in buying range.''')
print(hits)

for security in range(len(SMA20_securities)):
    fetched_data = fetch_data(SMA20_securities[security][0], SMA20_securities[security][1], '365 D')
    closing_prices = extract_closing(fetched_data)
    sma20 = create_masubplot(20, closing_prices)
    if closing_prices[len(closing_prices)-1] < (1 * sma20['data'][len(sma20['data'])-1]):
        hits.append(SMA20_securities[security][0])
        sma9 = create_masubplot(9, closing_prices)
        sma50 = create_masubplot(50, closing_prices)
        sma200 = create_masubplot(200, closing_prices)
        lowerbb = create_lowerbb_subplot(closing_prices, 20, 2.5)
        upperbb = create_upperbb_subplot(closing_prices, 20, 2.5)
        pdata = reformat_IBdata(fetched_data, 120)
        plot_pdata(pdata, sma9, sma20, sma50, sma200, lowerbb, upperbb, 120, SMA20_securities[security][0], 20)
    else:
        print(f'''{SMA20_securities[security][0]} not in buying range.''')
print(hits)

for security in range(len(SMA50_securities)):
    fetched_data = fetch_data(SMA50_securities[security][0], SMA50_securities[security][1], '365 D')
    closing_prices = extract_closing(fetched_data)
    sma50 = create_masubplot(50, closing_prices)
    if closing_prices[len(closing_prices)-1] < (1 * sma50['data'][len(sma50['data'])-1]):
        hits.append(SMA50_securities[security][0])
        sma9 = create_masubplot(9, closing_prices)
        sma20 = create_masubplot(20, closing_prices)
        sma200 = create_masubplot(200, closing_prices)
        lowerbb = create_lowerbb_subplot(closing_prices, 20, 2.5)
        upperbb = create_upperbb_subplot(closing_prices, 20, 2.5)
        pdata = reformat_IBdata(fetched_data, 120)
        plot_pdata(pdata, sma9, sma20, sma50, sma200, lowerbb, upperbb, 120, SMA50_securities[security][0], 50)
    else:
        print(f'''{SMA50_securities[security][0]} not in buying range.''')
print(hits)

for security in range(len(SMA200_securities)):
    fetched_data = fetch_data(SMA200_securities[security][0], SMA200_securities[security][1], '365 D')
    closing_prices = extract_closing(fetched_data)
    sma200 = create_masubplot(200, closing_prices)
    if closing_prices[len(closing_prices)-1] < (1 * sma200['data'][len(sma200['data'])-1]):
        hits.append(SMA200_securities[security][0])
        sma9 = create_masubplot(9, closing_prices)
        sma20 = create_masubplot(20, closing_prices)
        sma50 = create_masubplot(50, closing_prices)
        lowerbb = create_lowerbb_subplot(closing_prices, 20, 2.5)
        upperbb = create_upperbb_subplot(closing_prices, 20, 2.5)
        pdata = reformat_IBdata(fetched_data, 120)
        plot_pdata(pdata, sma9, sma20, sma50, sma200, lowerbb, upperbb, 120, SMA200_securities[security][0], 200)
    else:
        print(f'''{SMA200_securities[security][0]} not in buying range.''')
print(hits)
