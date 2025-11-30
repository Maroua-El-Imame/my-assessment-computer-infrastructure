#!/usr/bin/env python3

import yfinance as yf
import pandas as pd
import datetime as dt
import os
import glob
import matplotlib.pyplot as plt


def get_data():
    df = yf.download(['META', 'AAPL','AMZN','NFLX','GOOG'], period ='5d', interval='1h')
    df.to_csv(f"data/{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv", index=True, sep=',')

get_data()



def plot_data():
    list_of_files = glob.glob('data/*csv')
    latest_file = max(list_of_files, key=os.path.getctime)
    df = pd.read_csv(latest_file, header=[0,1],index_col= 0, parse_dates=True)
    os.makedirs("plots", exist_ok=True)
    timestamp = dt.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"plots/{timestamp}.png"
    df['Close'].plot(
         ylabel= 'Close prices',  
         xlabel= 'Dates',  
         title= 'Data of the last 5 days for the five FAAANG stocks',
         rot= 15 )
    plt.savefig(fname=filename)

plot_data()
