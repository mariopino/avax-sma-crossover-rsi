from backtesting import Backtest, Strategy
from backtesting.lib import crossover, plot_heatmaps
from backtesting.test import SMA
import yfinance as yf
import numpy as np
import pandas as pd
import pandas_ta as ta

# Set up parameters
cash = 10000  # Initial cash amount in USD
commission = 0.002  # Commission per trade
exclusive_orders = True  # Only one order at a time

# Download and prepare AVAX-USD data from Yahoo Finance
ticker_name = "AVAX-USD"
data = yf.download(ticker_name, interval='15m', period='30d', auto_adjust=True)
data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# Initial run params
n1 = 46  # Fast SMA
n2 = 100  # Slow SMA
rsi_window = 14  # RSI window
rsi_upper_bound = 50 # Upper bound for RSI
rsi_lower_bound = 40 # Lower bound for RSI

# Uncomment the following line to see the data before running the backtest
# print(data.tail())

class SMACrossRSI(Strategy):

    n1 = n1
    n2 = n2
    rsi_window = rsi_window
    rsi_upper_bound = rsi_upper_bound
    rsi_lower_bound = rsi_lower_bound

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

        # Compute RSI using TA
        close = pd.Series(self.data.Close, index=self.data.index)
        rsi = ta.rsi(close, window=rsi_window)
        self.rsi = self.I(lambda: rsi)

    def next(self):
        if crossover(self.sma1, self.sma2) and self.rsi[-1] > rsi_upper_bound:
            # Check if we are not already in a position
            if not self.position.is_long:
                # Close any existing short position
                if self.position.is_short:
                    self.position.close()
                # Enter long position
                self.buy(sl=self.data.Close[-1] * 0.95)
                # self.buy()

        elif crossover(self.sma2, self.sma1) or self.rsi[-1] < rsi_lower_bound:
            # Check if we are not already in a position
            if not self.position.is_short:
                # Close any existing long position
                if self.position.is_long:
                    self.position.close()
                # Enter short position
                self.sell(sl=self.data.Close[-1] * 1.05)
                # self.sell()

# Initialize the backtest
bt = Backtest(data, SMACrossRSI, cash=cash, commission=commission, exclusive_orders=exclusive_orders)

# Print results of the backtest
print(f"\nInitial Backtest Results (n1={n1}, n2={n2}, rsi_window={rsi_window}, rsi_upper_bound={rsi_upper_bound}, rsi_lower_bound={rsi_lower_bound}):\n")
print(bt.run())

# Run optimization
if __name__ == '__main__':
    optimization_results, heatmap = bt.optimize(
        n1=range(40, 52, 2),  # Fast SMA from 40 to 50, step 2
        n2=range(80, 152, 2),  # Slow SMA from 80 to 150, step 2
        #rsi_window=range(5, 31, 2),  # RSI window from 5 to 30, step 2
        rsi_upper_bound=range(50, 62, 2),  # RSI upper bound from 50 to 60, step 2
        rsi_lower_bound=range(40, 52, 2),  # RSI lower bound from 40 to 50, step 2
        maximize='Return [%]',  # Maximize Return
        constraint=lambda p: p.n1 < p.n2 and p.rsi_upper_bound > p.rsi_lower_bound,  # Constraint: n1 < n2 and rsi_upper_bound > rsi_lower_bound
        return_heatmap=True # Return heatmap data
    )

# Print optimization results
best_n1 = optimization_results._strategy.n1
best_n2 = optimization_results._strategy.n2
best_rsi_upper_bound = optimization_results._strategy.rsi_upper_bound
best_rsi_lower_bound = optimization_results._strategy.rsi_lower_bound

print(f"\nOptimized Backtest Results (n1={best_n1}, n2={best_n2}, rsi_upper_bound={best_rsi_upper_bound}, rsi_lower_bound={best_rsi_lower_bound}):\n")
print(optimization_results)

# Run the backtest with the best parameters
best_run = bt.run(n1=best_n1, n2=best_n2, rsi_upper_bound=best_rsi_upper_bound, rsi_lower_bound=best_rsi_lower_bound)

# Plot the results of the best run
bt.plot()

# Copy the trades DataFrame
trades = best_run['_trades'].copy()

# Add the trade type
trades['Type'] = np.where(trades['Size'] > 0, 'Long', 'Short')

# Compute return in percentage
trades['ReturnPct'] = np.where(
    trades['Type'] == 'Long',
    (trades['ExitPrice'] - trades['EntryPrice']) / trades['EntryPrice'] * 100,
    (trades['EntryPrice'] - trades['ExitPrice']) / trades['EntryPrice'] * 100
)

# Cleanup and reorder columns
useful_cols = ['Type', 'EntryTime', 'ExitTime', 'EntryPrice', 'ExitPrice', 'PnL', 'ReturnPct', 'Duration']
trades = trades[useful_cols]

# Print the trades
print("\nBest Run Trades:\n")
print(trades.to_string())

# Save trades to a CSV file
trades.to_csv('trades.csv', index=False)

# Plot Heatmap
plot_heatmaps(heatmap, agg='mean')