pip install quandl
import quandl
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader
%matplotlib inline
ex_gold = quandl.get("FRED/ID7108", authtoken="rArGtPqy3n1dzBFbscze")
date = ex_gold.index
price = ex_gold['Value']
plt.plot(date,price)
gld = web.DataReader("GLD","yahoo",).dropna()#jpy
print(gld)
date = gld.index
price = gld['Adj Close']
plt.plot(date,price)
spyd = web.DataReader("SPYD","yahoo").dropna()#jpy
print(spyd)
date = spyd.index
price = spyd['Adj Close']
plt.plot(date,price)
gold_reat = pd.DataFrame({'SPYD': spyd['Adj Close'], 'GLD': gld['Adj Close']})
print(gold_reat)
print(type(gold_reat.index))
gold_reat.index = pd.to_datetime(gold_reat.index)
print(type(gold_reat.index))
gold_reat.plot(title='gold vs. reat', grid=True)
plt.show()
import csv
mizuho_b =  web.DataReader('8411.JP',"stooq").dropna()#jpy
date = mizuho_b.index
price = mizuho_b['Close']
plt.plot(date,price)
import datetime as datetime
start=datetime.datetime(2000,1,1)
end =datetime.datetime(2020,10,12)
tickers = ["SPYD","GLD","FB"]
all_data = web.DataReader(tickers,'yahoo',start=start,end=end)
df = all_data["Adj Close"]
print(df)
df.index = pd.to_datetime(df.index)
print(type(df.index))
df.plot(title='reat vs. FB  vs gold', grid=True)
plt.show()
af_population = quandl.get("EIA/IES_93_44_33_5100", authtoken="rArGtPqy3n1dzBFbscze")
print(af_population)
jp_population = quandl.get("EIA/IES_93_44_33_JPN", authtoken="rArGtPqy3n1dzBFbscze")
print(jp_population)
date = af_population.index
price = af_population['Millions']
plt.plot(date,price)
date = jp_population.index
price = af_population['Millions']
plt.plot(date,price)

date = us_population.index
price = af_population['Millions']
plt.plot(date,price)
date = jp_population.index
price = af_population['Millions']
plt.plot(date,price)
date = us_population.index
price = af_population['Millions']
plt.plot(date,price)
from pandas_datareader import wb
df = wb.download(indicator='SP.POP.TOTL', country=['JP', 'US'],
                 start=1960, end=2021)
print(df)
df2 = df.unstack(level=0)
print(df2.head())
date = df2.index
price = df2['SP.POP.TOTL']
plt.plot(date,price)
list_tickers = ["SPYD","GLD","FB","AMZN","TSLA","JPM","PYPL"]
all_data = web.DataReader(list_tickers,'yahoo',start=start,end=end)
price = all_data["Adj Close"]
print(price)                      # グラフの表示
price.index = pd.to_datetime(price.index)
print(type(price.index)) 
price.plot(title='Amazon vs. Tesla  vs us_bank vs　paypl vs gold vs reat vs FB', grid=True)
plt.show()
%matplotlib notebook
%matplotlib qt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,
