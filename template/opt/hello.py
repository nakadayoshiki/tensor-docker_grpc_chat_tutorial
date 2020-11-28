import mplfinance as mpf
import pandas_datareader as pdr
import datetime

start = '1/1/10'
end = datetime.date.today()
df = pdr.stooq.StooqDailyReader('^SPX', start, end).read()
print(df)
