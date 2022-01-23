import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from dash import Input, Output, callback
from pandas import DataFrame, Series

from ta.trend import PSARIndicator, EMAIndicator
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands

dash.register_page(__name__)


def load_com(exchange: str) -> list:
    with open(f'datas/{exchange}/com.txt') as f:
        content = f.read()
        com = content.split(',')
        f.close()
    return com[:-1]


exchange_com_dict = dict(HOSE=load_com(
    'hose'), HNX=load_com('hnx'), UPCOM=load_com('upcom'))
exchanges = list(exchange_com_dict.keys())

# Available indicator
indis = ['sma-14', 'sma-50', 'sma-200', 'par','rsi','bb','ema-14','ema-50','ema-200']


def process(data: DataFrame) -> DataFrame:
    '''
    Adjust open, high, low price base on adjust close price

    Parameters
    ----------
    data : DataFrame


    Returns
    -------
    DataFrame

    '''
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
    data.set_index('Date', inplace=True)
    data = data.replace('-', np.nan)
    data = data.astype('float64')
    data['Open'] = round(data['Open']*(data['Adj Close']/data['Close']), -2)
    data['Low'] = round(data['Low']*(data['Adj Close']/data['Close']), -2)
    data['High'] = round(data['High']*(data['Adj Close']/data['Close']), -2)
    data['Close'] = round(data['Close']*(data['Adj Close']/data['Close']), -2)
    return data


def SMA(df: DataFrame, day: int) -> Series:
    return df.Close.rolling(day).mean().tail(100)


def eliminate_date(df: DataFrame) -> list:
    '''
    eliminate_date : Eliminate date-off

    Parameters
    ----------
    df : DataFarame

    Returns
    -------
    list
        List of day-off
    '''
    avail = list(df.tail(100).index.strftime('%Y-%m-%d'))
    all = list(pd.date_range(avail[0], avail[-1]).strftime('%Y-%m-%d'))
    eliminate = []
    for date in all:
        if date not in avail:
            eliminate.append(date)

    return eliminate


def volume_color(df: DataFrame) -> list:
    '''
    volume_color : Asign volume bar color base on previous value

    Parameters
    ----------
    df : DataFrame


    Returns
    -------
    list

    '''
    vol = df['Volume'].tail(100).to_list()
    col = []
    for i in range(len(vol)):
        if i == 0:
            col.append('#26A69A')
        else:

            if vol[i] > vol[i-1]:
                col.append('#26A69A')
            else:
                col.append('#EF5350')
    return col


def layout(com='AAA', exchange='HOSE', indi=indis[0]):
    return html.Div([
        html.Div(
            [dcc.Dropdown(
                id='exchange',
                options=[
                    {"label": x, "value": x} for x in exchanges
                ],
                value=exchange,
                clearable=False,
            ),
                dcc.Dropdown(
                id='com',
                value=com,
                clearable=False,
            ),
                dcc.Dropdown(
                id='indicator',
                options=[
                    {"label": x, "value": x} for x in indis
                ],
                value=[indi],
                clearable=False,
                multi=True,

            )
            ]),
        dcc.Graph(className='plot', id='chart'),
        dcc.Graph(className='rsi-fig', id='rsi-chart',config=dict(displayModeBar =False))
    ])


@callback(Output('com', 'options'), Input('exchange', 'value'))
def update_exchange_com(name):
    return [{'label': i, 'value': i} for i in exchange_com_dict[name]]


@callback(Output("chart", "figure"),Output('rsi-chart', 'figure'), Input("exchange", "value"), Input("com", "value"), Input('indicator', 'value'))
def update_bar_chart(exchange, com, indis):
    exchange_lower=exchange.lower()
    path = f'https://raw.githubusercontent.com/vuthanhdatt/web-indicator/main/datas/{exchange_lower}/{com}.csv'
    df = pd.read_csv(path, index_col=0)
    df = process(df)
    col = volume_color(df)
    max_vol = df['Volume'].tail(100).max()

    figdata = [go.Candlestick(x=df.tail(100).index,
                              open=df.tail(100)['Open'],
                              high=df.tail(100)['High'],
                              low=df.tail(100)['Low'],
                              close=df.tail(100)['Close'], showlegend=False),
               go.Bar(x=df.tail(100).index, y=df['Volume'].tail(100), yaxis='y2', marker=dict(color=col, opacity=0.3), showlegend=False)]

    for indi in indis:
        if indi.startswith('sma'):
            day = int(indi.split('-')[1])
            figdata.append(go.Scatter(x=df.tail(100).index, y=SMA(
                df, day), line=dict(width=1), name=indi))
            
        if indi.startswith('ema'):
            day = int(indi.split('-')[1])
            indi_ema = EMAIndicator(df['Close'],day)
            ema = indi_ema.ema_indicator().tail(100)
            figdata.append(go.Scatter(x=df.tail(100).index,y=ema, line=dict(width=1), name=indi))
        if indi == 'par':
            indi_par = PSARIndicator(df['High'], df['Low'], df['Close'])
            par = indi_par.psar().tail(100)
            figdata.append(go.Scatter(x=df.tail(100).index, y=par,
                           mode='markers', marker=dict(size=2.5), name='Parabolic'))
        if indi == 'bb':
            indi_bb = BollingerBands(df['Close'])
            bbh = indi_bb.bollinger_hband().tail(100)
            bbm = indi_bb.bollinger_mavg().tail(100)
            bbl = indi_bb.bollinger_lband().tail(100)
            figdata.extend([go.Scatter(x=df.tail(100).index, y=bbh, line=dict(width=1,color='#507EFF'), name='Parabolic1',showlegend=False),
                           go.Scatter(x=df.tail(100).index, y=bbm,
                            line=dict(width=1,color='#F49D5C'), name='2',fill='tonexty',fillcolor='rgba(232,239,243,0.5)',showlegend=False),
                           go.Scatter(x=df.tail(100).index, y=bbl,
                            line=dict(width=1,color='#507EFF'), name='Bollinger Band',fill='tonexty',fillcolor='rgba(232,239,243,0.5)')
                           ])


    fig = go.Figure(data=figdata)

    fig.update_traces(increasing_fillcolor='#26A69A', increasing_line=dict(color='#26A69A', width=0.5),
                      decreasing_fillcolor='#EF5350', decreasing_line=dict(color='#EF5350', width=0.5), line=dict(width=0.5), selector=dict(type='candlestick'))


    fig.update_layout(title=dict(text=f'{com} 100 DAYS CHART',x=0.5),
                      paper_bgcolor='#ffffff',
                      plot_bgcolor='#ffffff',
                      modebar=dict(add=['drawopenpath', 'eraseshape'], remove=['lasso'], orientation='v'), xaxis_rangeslider_visible=False,
                      yaxis=dict(
        title="Price",
        titlefont=dict(
            color="#1f77b4"
        ),
        tickfont=dict(
            color="#1f77b4"
        )
    ),
        yaxis2=dict(

        anchor="free",
        overlaying="y",
        side="left",
        position=0.15,
        range=[0, max_vol*6],
        visible=False,
        fixedrange=True
    ))
    fig.update_yaxes(showgrid=False)
    fig.update_xaxes(
        rangebreaks=[
            dict(values=eliminate_date(df))
        ]
    )
    rsi_indi = RSIIndicator(df['Close'])
    rsi = rsi_indi.rsi()
    df['low-rsi'] = 30
    df['high-rsi'] =70
    rsi_fig = go.Figure(data= [go.Scatter(x=df.tail(100).index, y=rsi.tail(100), line=dict(width=1), name='rsi'),
    go.Scatter(x=df.tail(100).index, y=df['low-rsi'].tail(100), line=dict(width=1,dash='dash'), showlegend=False),
    go.Scatter(x=df.tail(100).index, y=df['high-rsi'].tail(100), line=dict(width=1,dash='dash'), showlegend=False)])
    
    rsi_fig.update_layout(title=dict(text=f'{com} 100 DAYS CHART',x=0.5),
                      paper_bgcolor='#ffffff',
                      plot_bgcolor='#ffffff',)
    dummy_rsi = go.Figure(data= [], layout={
                      'paper_bgcolor':'#ffffff',
                      'plot_bgcolor':'#ffffff',
                      'yaxis':dict(visible=False),
                      'xaxis':dict(visible=False)}
    )
    if 'rsi' in indis:
        return fig, rsi_fig
    
    return fig, dummy_rsi
