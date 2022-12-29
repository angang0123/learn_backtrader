import yfinance as yf


if __name__ == '__main__':

    data = yf.download('TSLA', start='2021-01-01', end='2021-12-31')
    data.to_csv('tsla.txt')