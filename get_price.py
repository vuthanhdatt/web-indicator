import pandas as pd
import aiohttp
import asyncio
import logging
from datetime import date
import ast
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

start_date = '2000-01-01'
today = date.today().strftime("%Y-%m-%d")
########### FOR LOGGING ##############
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s","%d-%m-%y %H:%M:%S")
ch.setFormatter(formatter)
logger.addHandler(ch)
############GET COMPANY#####################



def get_all_com_token(cookies, headers):
    '''
    Get token session to make request to api
    '''
    sess = requests.Session()
    url = 'https://finance.vietstock.vn/doanh-nghiep-a-z?page=1'
    r= sess.get(url,headers=headers, cookies=cookies)
    soup = BeautifulSoup(r.content, 'html5lib')
    token = soup.findAll('input', attrs={'name':'__RequestVerificationToken'})[0]['value']
    return token

def make_all_com_form(exchange,token, page):
    '''
    Make form to call to api
    '''
    catID = {'all': '0' ,'hose':'1','hnx':'2','upcom':'5'}
 
    f = {'catID': catID[exchange],
    'industryID': '0',
    'page':str(page),
    'pageSize': '50',
    'code':'',
    'businessTypeID':'0',
    'orderBy': 'Code',
    'orderDir': 'ASC',
    '__RequestVerificationToken':token}
    return f

def get_all_com(exchange, cookies, headers):
    '''
    Return all companies on choosen exchange.
    
    '''
    url = 'https://finance.vietstock.vn/data/corporateaz'
    token = get_all_com_token(cookies,headers)
    page = 1
    result = []
    while True:
        f = make_all_com_form(exchange, token, page)
        r = requests.post(url, headers=headers,cookies=cookies,data=f)
        if len(r.json()) != 0:
            for com in r.json():
                result.append(com['Code'])
            page +=1
        else:
            break
    return result

##############GET PRICE#######################
def make_price_history_form(symbol, start, end):
    '''
    Making form to requests to market_price_url
    Paramaters
    ----------
    symbol: string, company symbol
    start: starting date
    end: ending date
    Retruns
    -------
    dict
    '''

    form = {'Code': symbol,
            'OrderBy': '',
            'OrderDirection': 'desc',
            'FromDate': start,
            'ToDate': end,
            'ExportType': 'excel',
            'Cols': 'MC,DC,CN,TN,GDC,TKLGD',
            'ExchangeID': 1}

    return form


def make_price_history_df(df):
    '''
    Formating price df 
    Paramaters
    ----------
    df: DataFrame, df reading from price_history_url
    Return
    ------
    DataFrame
    '''
    cols = ['Date', 'Volume', 'Open', 'Close', 'High',
           'Low', 'Adj Close']
    df.columns = cols
    # df = df.set_index('Date')
    df = df.reindex(['Date','High', 'Low', 'Open', 'Close', 'Volume',
                    'Adj Close',], axis='columns')
    df = df.reindex(index=df.index[::-1])
    df.reset_index(inplace=True, drop=True)
    df.fillna('-', inplace=True)
    return df
async def get_price_history(symbol,start,end):

    '''
    Take price history of specific company from start to end, coming with user cookies.
    Paramaters
    ----------
    symbol: string, company symbol, etc. 'fts', 'hpg'...
    start: string, starting date
    end: string, ending date
    cookies: dict, user cookies
    
    Return
    ------
    DataFrame
    '''
    url = 'https://finance.vietstock.vn/data/ExportTradingResult'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40'}
    form = make_price_history_form(symbol,start,end)
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, data=form) as response:
            html = await response.text()
            df = pd.read_html(html)[1]
            result = make_price_history_df(df)    
    return result
async def get_price(exchange, com_list):
    '''
    Async requests to data source to upload to Github, return dict of DataFrame
    to use in gsheet requests
    '''
    df_dict = {}
    semaphore = asyncio.Semaphore(10)
    async def single_file(com):
        async with semaphore:
            logger.info(f'{com, exchange} DONE!')
            result = await get_price_history(com,start_date,today)
            result.to_csv(f'datas/{exchange}/{com}.csv')
            df_dict[com] = result

    coros = [single_file(com) for com in com_list]
    await asyncio.gather(*coros)
    return df_dict

def write_com(exchange,coms):
    with open(f'datas/{exchange}/com.txt', 'w') as f:
        for com in coms:
            f.write(com+',')
        f.close()


if __name__ == '__main__':

    cookie = ast.literal_eval(os.getenv('COOKIES'))
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40'}
    
    
    hose_com = get_all_com('hose', cookie, header)
    logger.info('Load all com hose')
    hnx_com = get_all_com('hnx',cookie,header)
    logger.info('Load all com hnx')
    upcom_com = get_all_com('upcom',cookie, header)
    logger.info('Load all com upcom')


    write_com('hose',hose_com)
    write_com('hnx',hnx_com)
    write_com('upcom',upcom_com)


   
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_price('hose',hose_com))
    loop.run_until_complete(get_price('hnx',hnx_com))
    loop.run_until_complete(get_price('upcom',upcom_com))
