# Cerebro

This class is the cornerstone of *backtrader* because it serves as a central point for:
1. Gathering all inputs (*Data Feeds*), actors (*Strategies*), spectators (*Observers*), critics (*Analyzers*) and documenters (*Writers*) ensuring the show still goes on at any moment.
2. Execute the backtesting/or live data feeding/trading.
3. Returning the results.
4. Giving access to the plotting facilities.

## Gathering input
1. Start by creating a *cerebro*:

> cerebro = bt.Cerebro(**kwargs)
> 
> 