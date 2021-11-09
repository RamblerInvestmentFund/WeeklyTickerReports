import finviz as fv
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re
import pytz
import datetime
from datetime import date

pytz.utc

def market_profile(ticker):
    # Declare finviz object
    stock_info = fv.get_stock(ticker)
    # Create a mkt profile of select statistics
    mkt_profile = {
    'Price':float(stock_info['Price']),
    'Beta':float(stock_info['Beta']),
    'Market Cap':str(stock_info['Market Cap']),
    'P/E':float(stock_info['P/E']),
    'P/B':float(stock_info['P/B']),
    'EPS (ttm)':float(stock_info['EPS (ttm)']),
    'ROE':str(stock_info['ROE']),
    'ROI':str(stock_info['ROI'])}

    # Reticulate variables
    PRICE = mkt_profile['Price']
    BETA = mkt_profile['Beta']
    MARKET_CAP = mkt_profile['Market Cap']
    P_E = mkt_profile['P/E']
    P_B = mkt_profile['P/B']
    EPS = mkt_profile['EPS (ttm)']
    ROE = str(mkt_profile['ROE'])
    ROI = str(mkt_profile['ROI'])

    # Remove % sign (Latex doesn't like compiling these for some reason)
    ROE = ROE[:-1]
    ROI = ROI[:-1]
    mkt = pd.DataFrame.from_dict(mkt_profile, orient='index', columns=[''])

def ticker_news(ticker):
    # Format ticker news
    news = fv.get_news(ticker)

    story1_date=news[0][0]
    story1_short=news[0][1]
    story1_link=news[0][2]

    story2_date=news[1][0]
    story2_short=news[1][1]
    story2_link=news[1][2]

    story3_date=news[2][0]
    story3_short=news[2][1]
    story3_link=news[2][2]

    story4_date=news[3][0]
    story4_short=news[3][1]
    story4_link=news[3][2]

    story5_date=news[3][0]
    story5_short=news[3][1]
    story5_link=news[3][2]


def price_chart(df, ticker, file_name):
    # Plot
    print(df['Close'])
    fig = plt.plot(df['Date'], df['Close'], color='#800000')
    plt.title(f'{ticker} Price History')
    #plt.show(bbox_inches='tight')
    plt.savefig(file_name, bbox_inches='tight')


def bar_plots(df, x, y, color, title, file_name):
    fig = plt.figure(figsize = (5, 4))
    ax = sns.barplot(data=df, x=x, y=y, color=color)
    sns.despine()
    plt.bar_label(ax.containers[0])
    plt.title(title, pad=15)
    plt.savefig(file_name, bbox_inches='tight')


def stacked_bar(df, x, y1, y2, color, title, file_name):
    fig, ax = plt.subplots(figsize=(5,4))

    ax.bar(x, y1, color=color[0], label='Revenue')
    ax.bar(x, y2, color=color[1], bottom=y1, label='Earnings')

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.bar_label(ax.containers[1])
    ax.set_title(title, pad=15)
    ax.legend()
    plt.savefig(file_name, bbox_inches='tight')


def main():

    TICKER = 'MSFT'

    ### Finviz call ###

    market_profile(TICKER)

    ### yfinance calls ###

    stock = yf.Ticker(TICKER)
    # Stock objects
    hist = stock.history(period='6mo', interval='1d')
    fin = stock.financials
    bal = stock.balance_sheet
    cash = stock.cashflow
    earn = stock.earnings
    splits = stock.splits
    # Create data frames
    price_data = pd.DataFrame(data=hist, columns=['Close'])
    price_data.reset_index(inplace=True)
    financial_data = pd.DataFrame(data=fin)
    balance_data = pd.DataFrame(data=bal)
    cashflow_data = pd.DataFrame(data=cash)
    earnings_data = pd.DataFrame(data=earn)

    # Stock Summary and News
    summary = stock.info['longBusinessSummary']

    # Date x-axis data
    #curr_year = date.today().year
    year = str(datetime.datetime.today().strftime('%Y'))
    curr_year=int(year)
    dt = ['{}'.format(curr_year), '{}'.format(curr_year-1), '{}'.format(curr_year-2), '{}'.format(curr_year-3)]
    
    # Financials
    gross = [financial_data.loc['Gross Profit'][i]/1000000 for i in range(4)]
    ebit = [financial_data.loc['Ebit'][i]/1000000 for i in range(4)]
    debt_short = [balance_data.loc['Short Long Term Debt'][i]/1000000 for i in range(4)]
    debt_long = [balance_data.loc['Long Term Debt'][i]/1000000 for i in range(4)]
    revenue = [earnings_data.iloc[i][0]/1000000 for i in range(4)]
    earnings = [earnings_data.iloc[i][1]/1000000 for i in range(4)]

    operating_cash = cashflow_data.loc['Total Cash From Operating Activities']
    capital_expend = cashflow_data.loc['Capital Expenditures']
    fcf = []
    # Calculate Free Cash Flows (operating cash - capex)
    for (op_cash, capex) in zip(operating_cash, capital_expend):
        fcf.append(op_cash/1000000 - capex/1000000)

    ### Save charts ###

    # Financial
    price_chart(price_data, TICKER, './rif-logos/price-chart.png')
    bar_plots(financial_data, dt, gross, '#FEBD18', 'Gross Profit ($ millions)', './rif-logos/gross-profit.png')
    bar_plots(financial_data, dt, ebit, '#800000', 'EBIT ($ millions)', './rif-logos/ebit.png')

    # Balance sheet
    bar_plots(balance_data, dt, debt_short, '#800000', 'Short Long Term Debt ($ millions)', './rif-logos/debt_short.png')
    bar_plots(balance_data, dt, debt_long, '#FEBD18', 'Long Term Debt ($ millions)', './rif-logos/debt_long.png')

    # Cashflow
    bar_plots(cashflow_data, dt, fcf, '#FEBD18', 'Free Cash Flow ($ millions)', './rif-logos/fcf.png')

    # Earnings data
    #stacked_bar(earnings_data, dt, revenue, earnings, ('#800000','#363636'), 'Revenue/Earnings ($ millions)', './rif-logos/revenue_earnings.png')
    

if __name__=='__main__':
    main()