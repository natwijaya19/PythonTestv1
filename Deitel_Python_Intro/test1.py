import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

aapl_df = yf.download('AAPL',
                      start='2000-01-01',
                      end='2021-06-12',
                      progress=False,
)
aapl_df.head()

print(aapl_df.head())
