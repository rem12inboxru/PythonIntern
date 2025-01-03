import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def create_and_save_plot(data, ticker,start_data, end_data, index_style, filename=None):
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.subplot(3, 1, (1, 2))
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.plot(dates, data['bb_high'].values, label='BB HIGH')
            plt.plot(dates, data['bb_low'].values, label='BB LOW')
            plt.title(f"{ticker} Цена акций с течением времени")
            plt.xlabel(' ')
            plt.ylabel("Цена")
            plt.legend()
            plt.subplot(3, 1, 3 )
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
        plt.subplot(3, 1, (1, 2))
        plt.figure(figsize=(10, 4))
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.plot(data['Date'], data['bb_high'].values, label='BB HIGH')
        plt.plot(data['Date'], data['bb_low'].values, label='BB LOW')
        plt.title(f"{ticker} Цена акций с течением времени")
        plt.xlabel(' ')
        plt.ylabel("Цена")
        plt.legend()
        plt.subplot(3, 1, 3)
        #plt.figure(figsize=(10, 6))
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


def create_and_save_plotly(data, ticker):

    fig = make_subplots(rows=2, cols=1, row_heights=[4, 1])

    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Цена закрытия'), 1, 1)

    fig.add_trace(go.Scatter(x=data.index, y=data['Moving_Average'], mode='lines', name='Moving Average'),1,1)
    fig.add_trace(go.Scatter(x=data.index, y=data['bb_high'], mode='lines', name='BB HIGH'),1,1)
    fig.add_trace(go.Scatter(x=data.index, y=data['bb_low'], mode='lines', name='BB LOW'), 1, 1)

    fig.add_trace(go.Scatter(x=data.index, y=data['KN'], mode='lines', name='KN'), 2, 1)
    fig.add_trace(go.Scatter(x=data.index, y=data['D'], mode='lines + markers', name='D'),2, 1)

    fig.update_layout(title=f'Стоимость акций {ticker}')
    fig.update_xaxes(title='Дата', col=1, row=1)
    fig.update_xaxes(title='Дата', col=1, row=2)
    fig.update_yaxes(title='Цена', col=1, row=1)
    fig.update_yaxes(title='Стохастик, %', col=1, row=2)

    filename_int = f'{ticker} интерактивный график'
    fig.write_html(filename_int)

    fig.show()
