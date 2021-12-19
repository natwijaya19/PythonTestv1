#%%
# Using Pandas-Datareader
import pandas_datareader as pdr

# Request data via Yahoo public API
datapdr = pdr.get_data_yahoo ('NVDA')

# Display info
print(datapdr.info())
#%%
# Using yfinance
import yfinance as yf

# Request historical data for past 5 years
datayf = yf.Ticker('NVDA').history(period='5y')

# Show info
print(datayf.info())

#%%



