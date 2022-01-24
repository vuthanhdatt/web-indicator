# Explain
I will explain in detail all technical solutions I've used in this project here.

# Table of Contents
1. [Datas](#datas)
2. [Telegram Bot](#telegram-bot)
3. [Visualizing](#visualizing)
4. [Updating Ability](#updating-ability)

***
## Datas
Let's go to the first part, preparing datas. Unlike other countries that have developed financial markets, users can easily get stock data from Yahoo Finance or other large data sources. In Vietnam, it’s quite hard to get this data free easily. There are some available packages can get trading data, for example [vnquant](https://github.com/phamdinhkhanh/vnquant), but they don’t have `Adjust Close` price, which is very important for technical analysis. In order to solve this problem, I've been looking for some stock websites in Vietnam like cafef, vndirect and decide to crawl from data from Vietstock.  All code for getting price data is in the [`get_price.py`](https://github.com/vuthanhdatt/web-indicator/blob/main/get_price.py) file. Now I will explain each small part in this file.
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
Since each [page](https://finance.vietstock.vn/doanh-nghiep-a-z?page=1) only returns maximum 50 companies, while there are over 1600 companies in the stock market. To get all the companies, I create a function and loop until there is no companies return. This function returns a list of all companies in the chosen exchange.
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
This part is divided into 2 files, [`indicator.py`](https://github.com/vuthanhdatt/web-indicator/blob/main/indicator.py) for calculate indicators and [`channel.py`](https://github.com/vuthanhdatt/web-indicator/blob/main/channel.py) for sending messages to users in the channel.
### Calculate
I use [ta](https://technical-analysis-library-in-python.readthedocs.io/en/latest/) package, which has `add_all_ta_features` method to calculate all common indicators. For processing data, I create `process` function. This function will adjust open, high and low prices based on adjusted close prices.
```py
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
```
Then I create a function, which loops through all companies in the chosen exchange. This function will check if a company meets the requirement or not. For example:
```py
if indi['momentum_rsi'][-1] >70:
    overbought.append(com)
```

Above code will check if the company overbought or not. Based on this logic, I can use as many indicators as I wish like this.
```py
if indi['volatility_bbhi'][-1] == 1:
    bbh.append(com)
if indi['volatility_bbli'][-1] == 1:
    bbl.append(com)
if df['Close'][-2] <df['sma14'][-2] and df['Close'][-1] >df['sma14'][-1]:
    sma_up.append(com)
if df['Close'][-2] >df['sma14'][-2] and df['Close'][-1] <df['sma14'][-1]:
    sma_down.append(com)
``` 
Although ta package has the `add_all_ta_features` method to calculate common indicators, it doesn't allow user change parameter. For example with SMA indicator, there are two default results is sma_slow and sma_fast, which calculate SMA12 and SMA26.

![sma-default](https://raw.githubusercontent.com/vuthanhdatt/web-indicator/main/images/sma-default.png) 

But I want to calculate SMA14 so I use `SMAIndicator` method directly to calculate this indicator.
```py
indi['sma14'] = SMAIndicator(df['Close'],14).sma_indicator()
```

### Sending message
Finally, I create `com_to_text` function to bring the match company into the markdown type since when sending messages, I use markdown format.  At first, I’m about to send all the results in one message, but it led to a problem. It’s too long and some last company will not be linked.

![not-link-msg](https://raw.githubusercontent.com/vuthanhdatt/web-indicator/main/images/not-link-msg.png)

Therefore I divide the message into small parts and store it into a list.
```py
texts = [f''' *Update {today}*
_HOSE_, Parabolic SAR
- Company {com_to_text(hose_indi['psar_up'],'HOSE',"par")} stop going down and reverse
- Company {com_to_text(hose_indi['psar_down'],'HOSE',"par")} stop going up and reverse
''',
f'''
_HNX_, Parabolic SAR
- Company {com_to_text(hnx_indi['psar_up'],'HNX',"par")} stop going down and reverse
- Company {com_to_text(hnx_indi['psar_down'],'HNX',"par")} stop going up and reverse

''',
f'''
_UPCOM_, Parabolic SAR
- Company {com_to_text(upcom_indi['psar_up'],'UPCOM',"par")} stop going down and reverse
- Company {com_to_text(upcom_indi['psar_down'],'UPCOM',"par")} stop going up and reverse

'''
```
Then loop through that list to send individual message to channel.
```py
for text in texts:
    bot.send_message(chat_id='-1001453202586',text=text,parse_mode='Markdown',disable_web_page_preview=True)
```

## Visualizing
When users get an alert message in telegram, maybe they want to check if this company actually met this indicator or not. I use [Dash](https://github.com/plotly/dash) and [Plotly](https://github.com/plotly/plotly.py) to create a web app that can visualize candlestick charts and indicators. Therefore, users can simply click on a company link in Telegram message, it will lead to my web app with this indicator. In this web app, I also create a blog page, which will provide technical analysis articles, like [this](https://bot-indicator.herokuapp.com/blog/par).


### Pages
In pages folder, there are 3 files [`blog.py`](https://github.com/vuthanhdatt/web-indicator/blob/main/pages/blog.py), [`chart.py`](https://github.com/vuthanhdatt/web-indicator/blob/main/pages/chart.py), [`home.py`](https://github.com/vuthanhdatt/web-indicator/blob/main/pages/home.py) and [`blogs`](https://github.com/vuthanhdatt/web-indicator/tree/main/pages/blogs) folder. Each file contain layout of each page in my web app. In `blogs` folder, there is layout of technical analysis articles in blog pages. I will focus on `chart.py` page, which used to visualize chart and indicator.
### Chart
In here, I have a list containing all indicators I want to visualize.
```py
indis = ['sma-14', 'sma-50', 'sma-200', 'par','rsi','bb','ema-14','ema-50','ema-200']
```

Then, I created  layout for this page.

```py
def layout(com='AAA', exchange='HOSE', indi=indis[0]):
    return html.Div([])
```


Dash use [callback](https://dash.plotly.com/basic-callbacks) to update figures, it will be very complicated if I go into detail how I use callback to update my chart. But basically, it will check the input has which indicator, for example, if user chooses a par indicator, it will calculate then append par data to figure data.
```py
if indi == 'par':
    indi_par = PSARIndicator(df['High'], df['Low'], df['Close'])
    par = indi_par.psar().tail(100)
    figdata.append(go.Scatter(x=df.tail(100).index, y=par,
                    mode='markers', marker=dict(size=2.5), name='Parabolic'))
```

With this logic, I also can put as many indicators into the chart as I wish.

### Web app
Finally, I put all these pages into [`app.py`](https://github.com/vuthanhdatt/web-indicator/blob/main/app.py), this file is a container of all pages and helps make layout for this web app. I also modify default css in styles.css, it’s not relevant to this subject so I will not go into detail here. For hosting, I use [heroku](https://www.heroku.com/) and modify in `Procfile`

```web: gunicorn app:server```

## Updating Ability

Now, this bot may be helpful for us to find a company, but if it can send messages only one time, it will be very useless. To solve this problem, I’ve used GIthub Action to automate, calculate and send messages everyday.
### Set up job
Github action using workflow to running action, each workflow contains many jobs. My workflow is in [`.github\workflows\update.yml`](https://github.com/vuthanhdatt/web-indicator/blob/main/.github/workflows/update.yml) file. I will explain detail how it work here.
Fisrtly, I have this code to specify when my bot will run. It will run on 8:15 UTC(15:15 GMT +7 Hanoi) everyday except weekend.
```yml
on:
  schedule:
    - cron: "15 8 * * 1-5" #Run at 8:15 UTC every day except weekend
```
Then I choose Ubuntu for running environment

```yml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
```

Then it will checkout my Github repo and set up python 3.9.7 environment
```yml
- name: Checkout repo content
    uses: actions/checkout@v2 # checkout the repository content to github runner

- name: Setup python
    uses: actions/setup-python@v2
    with:
        python-version: '3.9.7' # install the python version needed
```
Then it install all requirements package.
```yml
- name: Install python packages
    run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
```
Running `get_prcie.py` file to get today data.
```yml
- name: Get today price
    env:
        COOKIES: ${{secrets.COOKIES}}
    run: python get_price.py
```
Then commit and push data back to my repository. I use [action user](https://github.com/actions-user) to auto commit.
```yml 
- name: Commit files
    run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add -A
        git commit -m "Auto update data" -a
    - name: Push changes
    uses: ad-m/github-push-action@v0.6.0
    with:
        github_token: ${{secrets.ACCESS_TOKEN_GITHUB}}
        branch: main 
```
Finally, I will run `channel.py` file to calculate and send message with new data to Telegram channel.
```yml
- name: Send message to Telegram channel
    env:
        TOKEN: ${{secrets.TOKEN}}
    run: python channel.py
```









