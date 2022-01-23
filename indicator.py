from datetime import date

import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import pandas as pd
from ta import add_all_ta_features
from ta.trend import SMAIndicator


def process(data, day):
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
    data.set_index('Date',inplace=True)
    data = data.replace('-',np.nan)
    data = data.astype('float64')
    data = data.tail(day)
    data['Open'] = round(data['Open']*(data['Adj Close']/data['Close']),-2)
    data['Low'] = round(data['Low']*(data['Adj Close']/data['Close']),-2)
    data['High'] = round(data['High']*(data['Adj Close']/data['Close']),-2)
    data['Close'] = round(data['Close']*(data['Adj Close']/data['Close']),-2)
    return data

def com_to_text(coms,exchange, indi):
    n = []
    for com in coms:
        m = '[' +com +']' +f'(https://bot-indicator.herokuapp.com/chart?exchange={exchange}&com={com.upper()}&indi={indi})'
        n.append(m)
    s = ', '
    return s.join(n)

# if __name__ == '__main__':
# today = date.today().strftime("%Y-%m-%d")
today = '2022-01-21'
ytd = '2022-01-20'





def calculate(exchange):
    indis = {}
    psar_down = []
    psar_up = []
    overbought = []
    oversell = []
    bbh=[]
    bbl=[]
    sma_up=[]
    sma_down = []
    with open(f'datas/{exchange}/com.txt') as f:
        content = f.read()
        coms = content.split(',')
        f.close()

    coms = coms[:-1]
    for com in coms:
        df = pd.read_csv(f'datas/{exchange}/{com}.csv',index_col=0)
        df = process(df,100)
        if df.shape[0] >30:
            indi = add_all_ta_features(
            df, open="Open", high="High", low="Low", close="Close", volume="Volume", fillna=True)
            indi['sma14'] = SMAIndicator(df['Close'],14).sma_indicator()
            if indi['trend_psar_down_indicator'][today] == 1:
                psar_down.append(com)
            if indi['trend_psar_up_indicator'][today]== 1:
                psar_up.append(com)
            if indi['momentum_rsi'][today] >70:
                overbought.append(com)
            if indi['momentum_rsi'][today] <30:
                oversell.append(com)   
            if indi['volatility_bbhi'][today] == 1:
                bbh.append(com)
            if indi['volatility_bbli'][today] == 1:
                bbl.append(com)
            if df['Close'][ytd] <df['sma14'][ytd] and df['Close'][today] >df['sma14'][today]:
                sma_up.append(com)
            if df['Close'][ytd] >df['sma14'][ytd] and df['Close'][today] <df['sma14'][today]:
                sma_down.append(com)
            
    indis['psar_up'] = psar_up
    indis['psar_down'] = psar_down
    indis['overbought'] = overbought
    indis['oversell'] = oversell
    indis['bbh'] = bbh
    indis['bbl'] = bbl
    indis['sma_up'] = sma_up
    indis['sma_down'] = sma_down




    return indis

hose_indi = calculate('hose')

text = f''' *Cập nhật ngày {today}*
_HOSE_
- Company {com_to_text(hose_indi['psar_up'],'HOSE',"par")} stop going down and reverse
- Company {com_to_text(hose_indi['psar_down'],'HOSE',"par")} stop going up and reverse
- Company {com_to_text(hose_indi['overbought'],'HOSE',"rsi")} is overbought
- Company {com_to_text(hose_indi['oversell'],'HOSE',"rsi")} is oversell
- Company {com_to_text(hose_indi['bbh'], 'HOSE', 'bb') } have close price higher than bollinger high band
- Company {com_to_text(hose_indi['bbl'], 'HOSE', 'bb') } have close price lower than bollinger low band
- Company {com_to_text(hose_indi['sma_up'], 'HOSE', 'sma-14') } cut and have close price higher than sma 14 days
- Company {com_to_text(hose_indi['sma_down'], 'HOSE', 'sma-14') } cut and have close price lower than sma 14 days


'''
print(text)