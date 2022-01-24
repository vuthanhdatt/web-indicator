# STOCK INDICATOR TELGRAM BOT

## Problem
When come into technical analysis field, I realize that it's hard to find out which company in stock market met your indicator. How can I find which company have SMA14 price cut close price among over 1600 companies in Vietnam stock market? There maybe some paid services can help you, but it's **paid** services. So I create this project in order to help you find out which companies have met your indicator requirement. 
## Structure
```bash
├── .github
│   └── workflows
│       └──update.yml
├── assets
│   └── style.css
├── datas
│   ├── hose
│   ├── hnx
│   └── upcom
├── images
├── pages
│   ├── blogs
│   ├── blog.py
│   ├── chart.py
│   ├── home.py
│   └── price.py
├── Procfile
├── README.md
├── app.py
├── channel.py
├── explain.md
├── get_price.py
├── indicator.py
└── requirements.txt

```
## Demo
[Telegram](https://t.me/+TwX0gzHQEf85Yjhl) channel

[Web](https://bot-indicator.herokuapp.com/) app

![telegram-channel](https://github.com/vuthanhdatt/web-indicator/blob/main/images/demo-telegram.jpg)

![web-app](https://github.com/vuthanhdatt/web-indicator/blob/main/images/web-demo.png)
## How it build
### Datas
There is no Vietnam stock data in YahooFinance or other large finance data source. In this project, I get data from [Vietstock](https://finance.vietstock.vn/) websites. 
### Telegram Bot
To announce to user, I've created a telegram channel, then using [Telegram](https://github.com/python-telegram-bot/python-telegram-bot) to automatically send results to this channel
### Visualizing
To visualizing results, I use [Plotly](https://github.com/plotly/plotly.py) and [Dash](https://github.com/plotly/dash) to create a web app. Then using [Heroku](https://dashboard.heroku.com/) to hosting. 
### Updating Ability
To automatically update data and send message every day, I use [Github Action](https://github.com/features/actions).

****
For more technical detail, check my [explaination](https://github.com/vuthanhdatt/web-indicator/blob/main/explain.md).
