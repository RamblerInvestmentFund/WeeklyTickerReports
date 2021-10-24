import slack
import pandas as pd
import os
import requests
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from finviz import Screener
from datetime import date

def price_hist(stock):
    hist = stock.history(period='6mo', interval='1d')
    df = pd.DataFrame(data=hist, columns=['Close'])
    df.reset_index(inplace=True)

    # Plot
    plt.plot(df['Date'], df['Close'], color='#800000')
    plt.title(f'{TICKER} Price History')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.savefig('./rif-logos/price-chart.png')

def financials(ticker, stock):
    fs = stock.financials
    df = pd.DataFrame(data=fs)
    curr_year = int(date.today().year)
    gross = [df.loc['Gross Profit'][i]/1000000 for i in range(4)]
    dt = [f'5/31/{curr_year}', f'5/31/{curr_year-1}', f'5/31/{curr_year-2}', f'5/31/{curr_year-3}']
    sns.barplot(data=df, x=dt, y=gross, color='#FEBD18')
    plt.title(f'{ticker} Gross Profit')
    plt.xlabel('Date')
    plt.ylabel('Profits (millions)')
    plt.show()

TICKER = 'MSFT'
stock = yf.Ticker(TICKER)
financials(TICKER, stock)



