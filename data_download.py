import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
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