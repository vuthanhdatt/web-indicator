# Explain
I will explain in detail all technical solutions I've used in this project here.

# Table of Contents
1. [Datas](#datas)
2. [Telegram Bot](#telegram-bot)
3. [Visualizing](#visualizing)
4. [Updating Ability](#updating-ability)
5. [Improvement](#improvement)

***
## Datas
Let's go to the first part, preparing datas. Unlike other countries that have developed financial markets, users can easily get stock data from Yahoo Finance or other large data sources. In Vietnam, it’s quite hard to get this data free easily. There are some available packages can get trading data, for example [vnquant](https://github.com/phamdinhkhanh/vnquant), but they don’t have `Adjust Close` price, which is very important for technical analysis. In order to solve this problem, I've been looking for some stock websites in Vietnam like cafef, vndirect and find out I can get full data from Vietstock.  All code for getting price data is in the [`get_price.py`](https://github.com/vuthanhdatt/web-indicator/blob/main/get_price.py) file. Now I will explain each small part in this file.
### Get token
Firstly, Vietstock uses [CFSR](https://en.wikipedia.org/wiki/Cross-site_request_forgery) token to prevent Cross-site request forgery attack. This token change every new session, so I create a function to capture this request token in current session.
```py
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
```
This function return token for the current session, so I can use this token append into my header request. 
### Get all company in stock market
Since each page only returns 50 companies, while there are over 1600 companies in the stock market. To get all the companies, I create a function and loop until there is no companies return. This function returns a list of all companies in the chosen exchange.
```python
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
```
### Get price all companies 
After get all companies, I create a function to get price from these companies. This function use [asynchronous](https://docs.python.org/3/library/asyncio.html) to improve receive datas speed.

```py
async def get_price(exchange, com_list):

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
```
Finally, I run function above to get price.
```py
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_price('hose',hose_com))
    loop.run_until_complete(get_price('hnx',hnx_com))
    loop.run_until_complete(get_price('upcom',upcom_com))

```

## Telegram Bot



## Visualizing





## Updating Ability





## Improvement