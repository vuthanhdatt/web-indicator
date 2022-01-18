import pandas as pd
from ta import add_all_ta_features
import numpy as np
from datetime import date


def process(data, day):
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date',inplace=True)
    data = data.replace('-',np.nan)
    data = data.astype('float64')
    data = data.tail(day)
    data['Open'] = round(data['Open']*(data['Adj Close']/data['Close']),-2)
    data['Low'] = round(data['Low']*(data['Adj Close']/data['Close']),-2)
    data['High'] = round(data['High']*(data['Adj Close']/data['Close']),-2)
    data['Close'] = round(data['Close']*(data['Adj Close']/data['Close']),-2)
    return data

def com_to_text(l):
    n = []
    for c in l:
        m = '[' +c +']' +f'(https://www.tradingview.com/chart/?symbol=HOSE%3A{c.upper()})'
        n.append(m)
    s = ', '
    return s.join(n)

# if __name__ == '__main__':
today = date.today().strftime("%Y-%m-%d")
# today = '2021-12-23'


all_com_indi = []
psar_down_com = []
psar_up_com = []

with open('datas/hose/com.txt') as f:
    content = f.read()
    hose_com = content.split(',')
    f.close()

hose_com = hose_com[:-1]
for com in hose_com:

    df = pd.read_csv(f'datas/hose/{com}.csv',index_col=0)
    df = process(df,100)
    if df.shape[0] >30:
        indi = add_all_ta_features(
        df, open="Open", high="High", low="Low", close="Close", volume="Volume", fillna=True)
        if indi['trend_psar_down_indicator'][today].values == 1:
            psar_down_com.append(com)
        if indi['trend_psar_up_indicator'][today].values == 1:
            psar_up_com.append(com)

text = f'*Cập nhật ngày {today}*\n\
- công ty {com_to_text(psar_down_com)} đang đảo chiều giảm theo chỉ số parabolic\n \
- công ty {com_to_text(psar_up_com)} đang đảo chiều tăng theo chỉ số parabolic'
print(text)