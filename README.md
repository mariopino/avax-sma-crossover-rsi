# Backtesting a mixed SMA crossover and RSI strategy on the AVAX-USD pair

Backtesting a mixed SMA crossover and RSI strategy on the [AVAX-USD](https://finance.yahoo.com/quote/AVAX-USD/) pair using [Backtesting.py](https://kernc.github.io/backtesting.py/) Python library.

The script does the following:

- Download daily OHLCV data from Yahoo Finance
- Initial run with predefined parameters
- Optimization
- Run with optimized parameters
- Generates a candle chart with indicators and trades (SMACrossRSIRSI_n1-XX,n2-YY_.html)
- Generates a Heatmap for the different combination of slow and fast moving averages (SMACrossRSIRSI.html)
- Export trades to CSV file (trades.csv)

The best results were achieved using a 5% stop loss for both SHORT and LONG trades.

# Installation

## Clone repository:

```
git clone https://github.com/mariopino/avax-sma-crossover-rsi.git
cd avax-sma-crossover-rsi
```

## Create virtual environment

### VSCode

To create local environments in VS Code using virtual environments or Anaconda, you can follow these steps: open the Command Palette (Ctrl+Shift+P), search for the Python: Create Environment command, and select it, then select Venv.

Select and activate an environment

Use the `Python: Select Interpreter` command from the Command Palette (Ctrl+Shift+P) and then select `.\.venv\Scripts\python.exe`.

### Linux

```
python -m venv myvenv
source myvenv/bin/activate
```

## Install dependencies

```
pip install backtesting
pip install yfinance
pip install pandas-ta
```

# Execute script

## Windows

```
python.exe SMACrossRSI.py
```

## Linux

```
python SMACrossRSI.py
```

# Results:

```
Initial Backtest Results (n1=46, n2=100, rsi_window=14, rsi_upper_bound=50, rsi_lower_bound=40):

Start                     2025-03-24 00:00...
End                       2025-04-22 09:15...
Duration                     29 days 09:15:00
Exposure Time [%]                     93.9759
Equity Final [$]                  13106.12053
Equity Peak [$]                   14127.33723
Commissions [$]                    1284.73897
Return [%]                           31.06121
Buy & Hold Return [%]                -6.99276
Return (Ann.) [%]                  2587.00774
Volatility (Ann.) [%]              2444.05351
CAGR [%]                           2778.46836
Sharpe Ratio                          1.05849
Sortino Ratio                        67.06917
Calmar Ratio                        199.77149
Alpha [%]                            27.98318
Beta                                 -0.44017
Max. Drawdown [%]                   -12.94983
Avg. Drawdown [%]                    -2.02811
Max. Drawdown Duration       12 days 15:30:00
Avg. Drawdown Duration        0 days 14:49:00
# Trades                                   26
Win Rate [%]                         53.84615
Best Trade [%]                       17.18526
Worst Trade [%]                       -5.0313
Avg. Trade [%]                         1.4567
Max. Trade Duration           5 days 18:15:00
Avg. Trade Duration           1 days 01:29:00
Profit Factor                         3.30559
Expectancy [%]                        1.54364
SQN                                   1.78369
Kelly Criterion                       0.36007
_strategy                         SMACrossRSIRSI

...

Optimized Backtest Results (n1=46, n2=118, rsi_upper_bound=50, rsi_lower_bound=40):

Start                     2025-03-24 00:00...
End                       2025-04-22 09:15...
Duration                     29 days 09:15:00
Exposure Time [%]                    93.23175
Equity Final [$]                  13848.15093
Equity Peak [$]                   14427.48158
Commissions [$]                    1008.18299
Return [%]                           38.48151
Buy & Hold Return [%]                -7.12936
Return (Ann.) [%]                  5151.29911
Volatility (Ann.) [%]              4323.33761
CAGR [%]                            5604.8653
Sharpe Ratio                          1.19151
Sortino Ratio                       138.49667
Calmar Ratio                        409.49585
Alpha [%]                             35.1394
Beta                                 -0.46878
Max. Drawdown [%]                   -12.57961
Avg. Drawdown [%]                    -1.64145
Max. Drawdown Duration        5 days 07:30:00
Avg. Drawdown Duration        0 days 11:34:00
# Trades                                   20
Win Rate [%]                             50.0
Best Trade [%]                       17.99077
Worst Trade [%]                      -3.06642
Avg. Trade [%]                        2.05611
Max. Trade Duration           9 days 05:45:00
Avg. Trade Duration           1 days 08:53:00
Profit Factor                         4.86504
Expectancy [%]                        2.15773
SQN                                   2.06529
Kelly Criterion                       0.38674
_strategy                 SMACrossRSIRSI(n1=4...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object

Best Run Trades:

     Type                 EntryTime                  ExitTime  EntryPrice  ExitPrice          PnL  ReturnPct        Duration
0   Short 2025-03-25 07:30:00+00:00 2025-03-25 09:30:00+00:00   21.879070  21.996344   -53.476639  -0.536007 0 days 02:00:00
1    Long 2025-03-25 09:30:00+00:00 2025-03-26 03:15:00+00:00   21.996344  22.715353   322.835220   3.268768 0 days 17:45:00
2   Short 2025-03-26 03:15:00+00:00 2025-04-04 09:00:00+00:00   22.715353  18.628687  1826.739750  17.990766 9 days 05:45:00
3    Long 2025-04-04 09:00:00+00:00 2025-04-04 10:30:00+00:00   18.628687  18.057453  -366.160833  -3.066420 0 days 01:30:00
4   Short 2025-04-04 10:30:00+00:00 2025-04-07 20:15:00+00:00   18.057453  16.697563   868.969700   7.530907 3 days 09:45:00
5    Long 2025-04-07 20:15:00+00:00 2025-04-08 08:15:00+00:00   16.697563  16.899672   149.560204   1.210406 0 days 12:00:00
6   Short 2025-04-08 08:15:00+00:00 2025-04-09 16:30:00+00:00   16.899672  17.019749   -88.496847  -0.710529 1 days 08:15:00
7    Long 2025-04-09 16:30:00+00:00 2025-04-10 03:15:00+00:00   17.019749  18.048292   744.665474   6.043235 0 days 10:45:00
8   Short 2025-04-10 03:15:00+00:00 2025-04-11 03:15:00+00:00   18.048292  18.473244  -306.390070  -2.354525 1 days 00:00:00
9    Long 2025-04-11 03:15:00+00:00 2025-04-11 23:15:00+00:00   18.473244  19.064592   405.073824   3.201109 0 days 20:00:00
10  Short 2025-04-11 23:15:00+00:00 2025-04-12 13:45:00+00:00   19.064592  19.262508  -134.978733  -1.038134 0 days 14:30:00
11   Long 2025-04-12 13:45:00+00:00 2025-04-13 04:45:00+00:00   19.262508  20.148838   589.409218   4.601320 0 days 15:00:00
12  Short 2025-04-13 04:45:00+00:00 2025-04-17 02:15:00+00:00   20.148838  18.891827   833.398567   6.238630 3 days 21:30:00
13   Long 2025-04-17 02:15:00+00:00 2025-04-17 02:45:00+00:00   18.891827  18.866774   -18.739662  -0.132613 0 days 00:30:00
14  Short 2025-04-17 02:45:00+00:00 2025-04-17 05:30:00+00:00   18.866774  19.171453  -226.986504  -1.614902 0 days 02:45:00
15   Long 2025-04-17 05:30:00+00:00 2025-04-17 14:15:00+00:00   19.171453  19.077293   -67.701097  -0.491147 0 days 08:45:00
16  Short 2025-04-17 14:15:00+00:00 2025-04-19 02:15:00+00:00   19.077293  19.242401  -118.217133  -0.865467 1 days 12:00:00
17   Long 2025-04-19 02:15:00+00:00 2025-04-20 04:15:00+00:00   19.242401  19.833817   414.582199   3.073501 1 days 02:00:00
18  Short 2025-04-20 04:15:00+00:00 2025-04-21 04:45:00+00:00   19.833817  19.904352   -49.233891  -0.355633 1 days 00:30:00
19   Long 2025-04-21 04:45:00+00:00 2025-04-21 17:00:00+00:00   19.904352  20.135508   159.497223   1.161331 0 days 12:15:00
```