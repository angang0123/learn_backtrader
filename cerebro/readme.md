# Cerebro

This class is the cornerstone of *backtrader* because it serves as a central point for:
1. Gathering all inputs (*Data Feeds*), actors (*Strategies*), spectators (*Observers*), critics (*Analyzers*) and documenters (*Writers*) ensuring the show still goes on at any moment.
2. Execute the backtesting/or live data feeding/trading.
3. Returning the results.
4. Giving access to the plotting facilities.

## Gathering input
1. Start by creating a *cerebro*:

> cerebro = bt.Cerebro(**kwargs)

2. Add Data Feeds:

> data = bt.BacktraderCSVData(dataname='mypath.days')
> 
> cerebro.adddata(data)

3. Add Strategies:

Unlike the *data feeds* which are already an instance of a class, *cerebro* takes directly the *Strategy* class and the arguments to pass to it (for optimization later).

If no optimization is run:

> cerebro.addstragegy(MyStrategy, myparam1=value1, myparam2=value2)

When optimizing the parameters have to be added as iterables.

> cerebro.optstrategy(MyStrategy, myparam1=range(10, 20))

4. Other elements

- addwriter
- addanalyzer
- addobserver (or addobservermulti)

5. Changing the broker

Default broker can be overriden:

> broker = MyBroker()
> cerebro.broker = broker

6. Receive notification


## Execute the backtesting

> result = cerebro.run(**kwargs)


## Giving access to the plotting facilities

> Cerebro.plot()


## Backtesting Logic

1. Deliver any store notifications
2. Ask data feeds to deliver the next set of ticks/bars
3. Notify the strategy about queued broker notifications of orders, trades and cash/value
4. Tell the broker to accept queued orders and execute the pending orders with the new data
5. Call the strategies' *next* method to let the strategy evaluate the new data
6. Tell any *writer* to write the data to its target

