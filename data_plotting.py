import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker,start_data, end_data, index_style, filename=None):
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.subplot(2, 1,1)
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.plot(dates, data['bb_high'].values, label='BB HIGH')
            plt.plot(dates, data['bb_low'].values, label='BB LOW')
            plt.title(f"{ticker} Цена акций с течением времени")
            plt.xlabel(' ')
            plt.ylabel("Цена")
            plt.subplot(2, 1, 2)
            plt.plot(dates, data['KN'].values, label='KN')
            plt.plot(dates, data['D'].values, label='D', linestyle='dotted')
            plt.xlabel("Дата")
            plt.ylabel("Стохастик, %")
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.subplot(2, 1, 1)
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.plot(data['Date'], data['bb_high'].values, label='BB HIGH')
        plt.plot(data['Date'], data['bb_low'].values, label='BB LOW')
        plt.title(f"{ticker} Цена акций с течением времени")
        plt.xlabel(' ')
        plt.ylabel("Цена")
        plt.subplot(2, 1, 2)
        plt.plot(data['Date'], data['KN'].values, label='KN')
        plt.plot(data['Date'], data['D'].values, label='D', linestyle='dotted')
        plt.xlabel("Дата")
        plt.ylabel("Стохастик, %")

    #plt.title(f"{ticker} Цена акций с течением времени")
    #plt.xlabel("Дата")
    #plt.ylabel("Цена")
    styles = plt.style.available
    plt.style.use(styles[index_style])
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{start_data}_{end_data}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")
