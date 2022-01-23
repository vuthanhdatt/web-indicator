import dash
import dash_core_components as dcc
import dash_html_components as html

dash.register_page(__name__)

text = '''

The parabolic SAR attempts to give traders an edge by highlighting the direction an asset is moving, as well as providing entry and exit points. In this article, we'll look at the basics of this indicator and show you how you can incorporate it into your trading strategy. We'll also look at some of the drawbacks of the indicator.

### Key Takeaways

-   The parabolic SAR indicator, developed by J. Welles Wilder Jr., is used by traders to determine trend direction and potential reversals in price.
-   The technical indicator uses a trailing stop and reverse method called "SAR," or stop and reverse, to identify suitable exit and entry points. 
-   The parabolic SAR indicator appears on a chart as a series of dots, either above or below an asset's price, depending on the direction the price is moving.
-   A dot is placed below the price when it is trending upward, and above the price when it is trending downward.

## The Indicator

The parabolic SAR is a [technical indicator](https://www.investopedia.com/terms/t/technicalindicator.asp) used to determine the price direction of an asset, as well as draw attention to when the price direction is changing. Sometimes known as the "stop and reversal system," the [parabolic](https://www.investopedia.com/ulta-beauty-reports-earnings-as-a-parabolic-bubble-pops-4688885) SAR was developed by J. Welles Wilder Jr., creator of the relative strength index (RSI).1

On a chart, the indicator appears as a series of dots placed either above or below the price bars. A dot below the price is deemed to be a bullish signal. Conversely, a dot above the price is used to illustrate that the bears are in control and that the momentum is likely to remain downward. When the dots flip, it indicates that a potential change in price direction is under way. For example, if the dots are above the price, when they flip below the price, it could signal a further rise in price.

As the price of a stock rises, the dots will rise as well, first slowly and then picking up speed and accelerating with the trend. The SAR starts to move a little faster as the trend develops, and the dots soon catch up to the price.

The following chart shows that the indicator works well for capturing profits during a trend, but it can lead to many false signals when the price moves sideways or is trading in a [choppy market](https://www.investopedia.com/terms/c/choppymarket.asp). The indicator would have kept the trader in the trade while the price rose. When the price is moving sideways, the trader should expect more losses and/or small profits. 

Image by Sabrina Jiang © Investopedia 2020

The following chart shows a downtrend, and the indicator would have kept the trader in a short trade (or out of longs) until the pullbacks to the upside began. When the downtrend resumed, the indicator got the trader back in.

The parabolic SAR is also a method for setting stop-loss orders. When a stock is rising, move the stop-loss to match the parabolic SAR indicator. The same concept applies to a short trade—as the price falls, so will the indicator. Move the stop-loss to match the level of the indicator after every price bar.

Image by Sabrina Jiang © Investopedia 2020

This indicator is mechanical and will always be giving new signals to get long or short. It is up to the trader to determine which trades to take and which to leave alone. For example, during a downtrend, it is better to take only the short sales like those shown in the chart above, as opposed to taking the [buy signals](https://www.investopedia.com/terms/b/buy-signal.asp) as well.

## Indicators to Complement to the Parabolic SAR

In trading, it is better to have several indicators confirm a certain signal than to rely solely on one specific indicator. Complement the SAR trading signals by using other indicators such as a stochastic, moving average, or the ADX.

For example, SAR sell signals are much more convincing when the price is trading below a long-term moving average. The price below a long-term moving average suggests that the sellers are in control of the direction and that the recent SAR sell signal could be the beginning of another [wave](https://www.investopedia.com/terms/e/elliottwavetheory.asp) lower. 

Similarly, if the price is above the moving average, focus on taking the buy signals (dots move from above to below). The SAR indicator can still be used as a stop-loss, but since the longer-term trend is up, it is not wise to take short positions.

Image by Sabrina Jiang © Investopedia 2020

A counter-argument to the parabolic SAR is that using it can result in a lot of trades. The chart above shows multiple trades. Some traders would argue that using the moving average alone would have captured the entire up move all in one trade. Therefore, the parabolic SAR is typically used by active traders who want to catch a high-momentum move and then get out of the trade.

The parabolic SAR performs best in markets with a steady trend. In ranging markets, the parabolic SAR tends to whipsaw back and forth, generating false trading signals.

The parabolic SAR is 'always on,' and constantly generating signals, whether there is a quality trend or not. Therefore, many signals may be of poor quality because no significant trend is present or develops following a signal.

## The Bottom Line

The parabolic SAR is used to gauge a stock's direction and for placing stop-loss orders. The indicator tends to produce good results in a trending environment, but it produces many [false signals](https://www.investopedia.com/terms/f/false-signal.asp) and losing trades when the price starts moving sideways. To help filter out some of the poor trade signals, only trade in the direction of the dominant trend. Some other technical tools, such as the moving average, can aid in this regard.
'''

def layout():
    # ...
    return html.Div(dcc.Markdown(children= text), className='blog-post')