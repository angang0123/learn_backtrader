import backtrader as bt
import backtrader.feeds as btfeeds

comm_datafeed_params = {'dataname': None,
                        'name': '',
                        # 'fromdate': btfeeds.mindate,
                        # 'todate': btfeeds.maxdate,
                        'timeframe': bt.TimeFrame.Days,
                        'compression': 1,
                        'sessionstart': None,
                        'sessionend': None}

csv_datafeed_params = {'headers': True,
                       'separator': ','}


if __name__ == '__main__':
    # from yahoo finance csv
    # data = btfeeds.YahooFinanceCSVData(dataname='wheremydatacsvis.csv')
    data = btfeeds.YahooFinanceData(dataname='TSLA')

    cerebro = bt.Cerebro()

    cerebro.adddata(data)