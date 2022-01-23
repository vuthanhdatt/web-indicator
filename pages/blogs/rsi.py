import dash
import dash_core_components as dcc
import dash_html_components as html

dash.register_page(__name__)

text = '''

## What Is the Relative Strength Index (RSI)?

The relative strength index (RSI) is a [momentum indicator](https://www.investopedia.com/investing/momentum-and-relative-strength-index/) used in technical analysis that measures the magnitude of recent price changes to evaluate overbought or oversold conditions in the price of a stock or other asset. The RSI is displayed as an oscillator (a line graph that moves between two extremes) and can have a reading from 0 to 100. The indicator was originally developed by J. Welles Wilder Jr. and introduced in his seminal 1978 book, “New Concepts in Technical Trading Systems.”

Traditional interpretation and usage of the RSI are that values of 70 or above indicate that a security is becoming overbought or overvalued and may be primed for a trend [reversal](https://www.investopedia.com/terms/r/reversal.asp) or corrective [pullback](https://www.investopedia.com/terms/p/pullback.asp) in price. An RSI reading of 30 or below indicates an oversold or [undervalued](https://www.investopedia.com/terms/u/undervalued.asp) condition.

### Key Takeaways

-   The relative strength index (RSI) is a popular momentum oscillator developed in 1978.
-   The RSI provides technical traders with signals about bullish and bearish price momentum, and it is often plotted beneath the graph of an asset’s price.
-   An asset is usually considered overbought when the RSI is above 70% and oversold when it is below 30%.

#### Relative Strength Index (RSI)

## The Formula for the RSI

The RSI is computed with a two-part calculation that starts with the following formula:

RSIstep one\=100−\[1001+Average gainAverage loss\]RSI\_{\\text{step one}} = 100- \\left\[ \\frac{100}{ 1 + \\frac{\\text{Average gain}}{\\text{Average loss} }} \\right\]

The average gain or loss used in the calculation is the average percentage gain or loss during a look-back period. The formula uses a positive value for the average loss. Periods with price losses are counted as 0 in the calculations of average gain, and periods when the price increases are counted as 0 for the calculation of average losses.

The standard is to use 14 periods to calculate the initial RSI value. For example, imagine the market closed higher seven out of the past 14 days with an average gain of 1%. The remaining seven days all closed lower with an average loss of −0.8%.

The calculation for the first part of the RSI would look like the following expanded calculation:

55.55\=100−\[1001+(1%14)(0.8%14)\]55.55 = 100 - \\left \[ \\frac {100 }{ 1 + \\frac{ \\left ( \\frac{ 1\\% }{ 14 } \\right) }{ \\left( \\frac{ 0.8\\% }{ 14 } \\right)} } \\right \]

Once there are 14 periods of data available, the second part of the RSI formula can be calculated. The second step of the calculation smooths the results.

RSIstep two\=100−\[1001+(Previous Average Gain×13) + Current Gain((Previous Average Loss×13) + Current Loss)\]RSI\_{\\text{step two}} = 100 - \\left \[ \\frac{ 100 }{ 1 + \\frac{ \\left ( \\text{Previous Average Gain} \\times 13 \\right ) \\ + \\ \\text{Current Gain} }{ \\left ( \\left ( \\text{Previous Average Loss} \\times 13 \\right ) \\ + \\ \\text{Current Loss} \\right ) } } \\right \]

## Calculation of the RSI

Using the formulas above, the RSI can be calculated, where the RSI line can then be plotted beneath an asset’s price chart.

The RSI will rise as the number and size of positive closes increase, and it will fall as the number and size of losses increase. The second part of the calculation smooths the result, so the RSI will only near 100 or 0 in a strongly [trending market](https://www.investopedia.com/terms/t/trending-market.asp).

Image by Sabrina Jiang © Investopedia 2021

As you can see in the above chart, the RSI indicator can stay in the overbought region for extended periods while the stock is in an [uptrend](https://www.investopedia.com/terms/u/uptrend.asp). The indicator may also remain in oversold territory for a long time when the stock is in a [downtrend](https://www.investopedia.com/terms/d/downtrend.asp). This can be confusing for new analysts, but learning to use the indicator within the context of the prevailing trend will clarify these issues.

## What Does the RSI Tell You?

The primary trend of the stock or asset is an important tool in making sure the indicator’s readings are properly understood. For example, well-known market technician Constance Brown, CMT, has promoted the idea that an oversold reading on the RSI in an uptrend is likely much higher than 30% and that an overbought reading on the RSI during a downtrend is much lower than the 70% level.1

As you can see in the following chart, during a downtrend, the RSI would peak near the 50% level rather than 70%, which could be used by investors to more reliably signal bearish conditions. Many investors will apply a horizontal [trendline](https://www.investopedia.com/terms/t/trendline.asp) between 30% and 70% levels when a strong trend is in place to better identify extremes. Modifying overbought or oversold levels when the price of a stock or asset is in a long-term [horizontal channel](https://www.investopedia.com/terms/h/horizontalchannel.asp) is usually unnecessary.

A related concept to using overbought or oversold levels appropriate to the trend is to focus on [trade signals](https://www.investopedia.com/terms/t/trade-signal.asp) and techniques that conform to the trend. In other words, using bullish signals when the price is in a bullish trend and bearish signals when a stock is in a bearish trend will help to avoid the many false alarms that the RSI can generate.

Image by Sabrina Jiang © Investopedia 2021

## Interpretation of RSI and RSI Ranges

Generally, when the RSI surpasses the horizontal 30 reference level, it is a bullish sign, and when it slides below the horizontal 70 reference level, it is a bearish sign. Put another way, one can interpret that RSI values of 70 or above indicate a security is becoming overbought or [overvalued](https://www.investopedia.com/terms/o/overvalued.asp) and may be primed for a trend [reversal](https://www.investopedia.com/terms/r/reversal.asp) or corrective price [pullback](https://www.investopedia.com/terms/p/pullback.asp). An RSI reading of 30 or below indicates an oversold or undervalued condition.

During trends, the RSI readings may fall into a band or range. During an uptrend, the RSI tends to stay above 30 and should frequently hit 70. During a downtrend, it is rare to see the RSI exceed 70, and the indicator frequently hits 30 or below. These guidelines can help determine trend strength and spot potential reversals. For example, if the RSI can’t reach 70 on a number of consecutive price swings during an uptrend, but then drops below 30, the trend has weakened and could be reversing lower. 

The opposite is true for a downtrend. If the downtrend is unable to reach 30 or below and then rallies above 70, that downtrend has weakened and could be reversing to the upside. Trend lines and moving averages are helpful tools to include when using the RSI in this way.

## Example of RSI Divergences

A bullish [divergence](https://www.investopedia.com/terms/d/divergence.asp) occurs when the RSI creates an oversold reading followed by a higher low that matches correspondingly lower lows in the price. This indicates rising bullish momentum, and a break above oversold territory could be used to trigger a new [long position](https://www.investopedia.com/terms/l/long.asp).

A bearish divergence occurs when the RSI creates an overbought reading followed by a lower high that matches corresponding higher highs on the price.

As you can see in the following chart, a bullish divergence was identified when the RSI formed higher lows as the price formed lower lows. This was a valid signal, but divergences can be rare when a stock is in a stable long-term trend. Using flexible oversold or overbought readings will help identify more potential signals.

Image by Sabrina Jiang © Investopedia 2021

## Example of RSI Swing Rejections

Another trading technique examines the RSI’s behavior when it is reemerging from overbought or oversold territory. This signal is called a bullish “swing rejection” and has four parts:

1.  The RSI falls into oversold territory.
2.  The RSI crosses back above 30%.
3.  The RSI forms another dip without crossing back into oversold territory.
4.  The RSI then breaks its most recent high.

As you can see in the following chart, the RSI indicator was oversold, broke up through 30%, and formed the rejection low that triggered the signal when it bounced higher. Using the RSI in this way is very similar to drawing trend lines on a price chart.



Like divergences, there is a bearish version of the swing rejection signal that looks like a mirror image of the bullish version. A bearish swing rejection also has four parts:

1.  The RSI rises into overbought territory.
2.  The RSI crosses back below 70%.
3.  The RSI forms another high without crossing back into overbought territory.
4.  The RSI then breaks its most recent low.

The following chart illustrates the bearish swing rejection signal. As with most trading techniques, this signal will be most reliable when it conforms to the prevailing long-term trend. Bearish signals during downward trends are less likely to generate false alarms.



## The Difference Between RSI and MACD

The [moving average convergence divergence](https://www.investopedia.com/terms/m/macd.asp) (MACD) is another trend-following momentum indicator that shows the relationship between two moving averages of a security’s price. The MACD is calculated by subtracting the 26-period [exponential moving average](https://www.investopedia.com/terms/e/ema.asp) (EMA) from the 12-period EMA. The result of that calculation is the MACD line.

A nine-day EMA of the MACD, called the “signal line,” is then plotted on top of the MACD line, which can function as a trigger for buy and sell signals. Traders may buy the security when the MACD crosses above its signal line and sell, or short, the security when the MACD crosses below the signal line.

The RSI was designed to indicate whether a security is [overbought](https://www.investopedia.com/terms/o/overbought.asp) or [oversold](https://www.investopedia.com/terms/o/oversold.asp) in relation to recent price levels. The RSI is calculated using average price gains and losses over a given period of time. The default time period is 14 periods, with values bounded from 0 to 100.

The MACD measures the relationship between two EMAs, while the RSI measures price change in relation to recent price highs and lows. These two indicators are often used together to provide [analysts](https://www.investopedia.com/terms/a/analyst.asp) with a more complete technical picture of a market.

These indicators both measure the momentum of an asset. However, they measure different factors, so they sometimes give contradictory indications. For example, the RSI may show a reading above 70 for a sustained period of time, indicating the security is [overextended](https://www.investopedia.com/terms/o/overextension.asp) to the buy side.

At the same time, the MACD could indicate that buying momentum is still increasing for the security. Either indicator may signal an upcoming trend change by showing divergence from price (the price continues higher while the indicator turns lower, or vice versa).

## Limitations of the RSI

The RSI compares bullish and bearish price momentum and displays the results in an oscillator that can be placed beneath a price chart. Like most technical indicators, its signals are most reliable when they conform to the long-term trend.

True reversal signals are rare and can be difficult to separate from false alarms. A false positive, for example, would be a bullish crossover followed by a sudden decline in a stock. A false negative would be a situation where there is a bearish crossover, yet the stock suddenly accelerated upward.

Since the indicator displays momentum, it can stay overbought or oversold for a long time when an asset has significant momentum in either direction. Therefore, the RSI is most useful in an oscillating market where the asset price is alternating between bullish and bearish movements.

## What Does the Relative Strength Index (RSI) Measure?

The Relative Strength Index (RSI) is a measurement used by traders to assess the price momentum of a stock or other security. The basic idea behind the RSI is to measure how quickly traders are bidding the price of the security up or down. The RSI plots this result on a scale of 0 to 100. Readings below 30 generally indicate that the stock is oversold, while readings above 70 indicate that it is overbought. Traders will often place this RSI chart below the price chart for the security, so they can compare its recent momentum against its market price.

## What Is an RSI Buy Signal?

Some traders will consider it a “buy signal” if a security’s RSI reading moves below 30, based on the idea that the security has been oversold and is therefore poised for a rebound. However, the reliability of this signal will depend in part on the overall context. If the security is caught in a significant downtrend, then it might continue trading at an oversold level for quite some time. Traders in that situation might delay buying until they see other confirmatory signals.

## What Is the Difference Between the RSI and Moving Average Convergence Divergence (MACD)?

RSI and moving average convergence divergence (MACD) are both measurements that seek to help traders understand a security’s recent trading activity, but they accomplish this goal in different ways. In essence, the MACD works by smoothing out the security’s recent price movements and comparing that medium-term trend line to another trend line showing its more recent price changes. Traders can then base their buy and sell decisions on whether the short-term trend line rises above or below the medium-term trend line.
'''

def layout():
    # ...
    return html.Div(dcc.Markdown(children= text), className='blog-post')