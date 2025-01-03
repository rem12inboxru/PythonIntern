import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker, start_data, end_data):
    #stock = yf.Ticker(ticker)
    data = pd.DataFrame()
    # data = stock.history(period=period)
    data1 = yf.download(ticker, start_data, end_data)
    data['Close'] = data1['Close']
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    average_price = data['Close'].mean(axis='index')
    print(f'Среднее значение колонки "Close" : {average_price}\n')


def notify_if_strong_fluctuations(data, threshold):
    threshold = float(input('Введите допустимое значение колебаний цены акций: '))
    min_price_close = data['Close'].min()
    max_price_close = data['Close'].max()
    try:
        fluctuation = ((max_price_close - min_price_close) / min_price_close) * 100
        fluctuation1 = round(fluctuation, 2)
        if fluctuation1 > threshold:
            print(f'Колебания цены превысили заданное значение на {fluctuation1 - threshold} процентов.')
    except Exception:
        print(f'Минимальная цена закрытия равна нулю. Непредвиденная ошибка')


def export_data_to_csv(data, filename):
    data_price = pd.DataFrame(data)
    return data_price.to_csv(filename, sep=',', index=False)


def calculate_bollinger(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    std = data['Close'].rolling(window=window_size).std()
    data['bb_high'] = data['Moving_Average'] + 2 * std
    data['bb_low'] = data['Moving_Average'] - 2 * std
    return data


def ind_stoch(data, window_size=5):
    close_stoch = list(data['Close'])
    y = []
    for i in close_stoch:
        x = ((i - min(close_stoch)) / (max(close_stoch) - min(close_stoch))) * 100
        y.append(x)
    data['KN'] = y
    data['D'] = data['KN'].rolling(window=window_size).mean()
    return data
