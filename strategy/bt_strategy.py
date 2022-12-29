import backtrader as bt
import backtrader.indicators as btind
import datetime


class MyStrategy(bt.Strategy):

    def __init__(self):
        self.sma = btind.SimpleMovingAverage(period=15)

    def prenext(self):  # Childhood
        # how long the strategy needs to mature
        pass

    def nextstart(self):
        pass

    def next(self):  # Adulthood
        if self.sma > self.data.close:
            pass
        elif self.sma < self.data.close:
            pass

    def stop(self):
        pass

    def notify_order(self):
        pass

    def notify_trade(self):
        pass

    def notify_cashvalue(self, cash, value):
        pass

    def notify_fund(self, cash, value, fundvalue, shares):
        pass

    def notify_store(self, msg, *args, **kwargs):
        pass

    def buy(self, data=None,
            size=None, price=None, plimit=None,
            exectype=None, valid=None, tradeid=0, oco=None,
            trailamount=None, trailpercent=None,
            parent=None, transmit=True,
            **kwargs):
        pass

    def sell(self, data=None,
             size=None, price=None, plimit=None,
             exectype=None, valid=None, tradeid=0, oco=None,
             trailamount=None, trailpercent=None,
             parent=None, transmit=True,
             **kwargs):
        pass

    def cancel(self, order):
        pass

    def buy_bracket(self, data=None, size=None, price=None, plimit=None,
                    exectype=bt.Order.Limit, valid=None, tradeid=0,
                    trailamount=None, trailpercent=None, oargs={},
                    stopprice=None, stopexec=bt.Order.Stop, stopargs={},
                    limitprice=None, limitexec=bt.Order.Limit, limitargs={},
                    **kwargs):
        pass

    def sell_bracket(self, data=None,
                     size=None, price=None, plimit=None,
                     exectype=bt.Order.Limit, valid=None, tradeid=0,
                     trailamount=None, trailpercent=None,
                     oargs={},
                     stopprice=None, stopexec=bt.Order.Stop, stopargs={},
                     limitprice=None, limitexec=bt.Order.Limit, limitargs={},
                     **kwargs):
        pass

    def order_target_size(self, data=None, target=0, **kwargs):
        pass

    def order_target_value(self, data=None, target=0.0, price=None, **kwargs):
        pass

    def order_target_percent(self, data=None, target=0.0, **kwargs):
        pass

    def setsizer(self, sizer):
        pass

    def getsizer(self):
        pass

    def getsizing(self, data=None, isbuy=True):
        pass

    def getpositions(self, broker=None):
        pass

    def getpositionbyname(self, name=None, broker=None):
        pass

    def getpositionsbyname(self, broker=None):
        pass

    def getdatanames(self):
        pass

    def getdatabyname(self, name):
        pass

    def add_timer(self, when,
                  offset=datetime.timedelta(), repeat=datetime.timedelta(),
                  weekdays=[], weekcarry=False,
                  monthdays=[], monthcarry=True,
                  allow=None,
                  tzdata=None, cheat=False,
                  *args, **kwargs):
        pass

    def notify_timer(self, timer, when, *args, **kwargs):
        pass


class MySingal(bt.Indicator):
    lines = ('signal', )
    params = (('period', 30), )

    def __init__(self):
        # >0 -> long indication, <0 -> short indication, ==0 -> no indication
        self.lines.signal = self.data - bt.indicators.SMA(period=self.p.period)