import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

dash.register_page(__name__)




def layout():
    # ...
    return html.Div([
    dbc.Card(
    [
        dbc.CardBody(
           [
            html.H4("How to use telegram bot indicator", className="card-title"),
            html.P(
                'An easy way to determine which company match your indicator',
                className="card-text",
            ),
            dbc.Button("Read more", color="primary",href='/blogs/register')
        ]
        ),
        dbc.CardBody(
           [
            html.H4("What is Relative Strength Index(RSI)?", className="card-title"),
            html.P(
                "The relative strength index (RSI) is a momentum indicator used in technical analysis that measures the magnitude of recent price changes to evaluate overbought or oversold conditions in the price of a stock or other asset. "
                ,
                className="card-text",
            ),
            dbc.Button("Read more", color="primary",href='/blogs/rsi')
        ]
        ),
        dbc.CardBody(
           [
            html.H4("Introduction to the Parabolic SAR", className="card-title"),
            html.P(
                "The parabolic SAR attempts to give traders an edge by highlighting the direction an asset is moving, as well as providing entry and exit points."
                ,
                className="card-text",
            ),
            dbc.Button("Read more", color="primary",href='/blogs/par')
        ]
        )
    ],)
],className='blog')