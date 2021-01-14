import requests
import datetime as dt
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

MY_STOCK_API = "41V23DS1BQ7GLDTJ"
MY_NEWS_API = "310bf093f57241f19c8cc9a7d15234a6"

stock_parameters = {
    "function":"TIME_SERIES_DAILY", 
    "symbol":STOCK,
    "apikey":MY_STOCK_API
}

today = dt.datetime.now().date()
yesterday = dt.datetime.now().date() - dt.timedelta(days=1)
the_day_before_yesterday = dt.datetime.now().date() - dt.timedelta(days=2)
print(str(yesterday))

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
tsla_stock_data = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_dict = tsla_stock_data.json()
yesterdays_close_price = float(stock_dict["Time Series (Daily)"][str(yesterday)]["4. close"])
the_day_before_yesterdays_close_price = float(stock_dict["Time Series (Daily)"][str(the_day_before_yesterday)]["4. close"])
stock_diff = (round(abs(yesterdays_close_price - the_day_before_yesterdays_close_price), 2))
stock_diff_percent = (stock_diff / yesterdays_close_price) * 100

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
if stock_diff_percent > 5:
    news_parameters = {
        "q":COMPANY_NAME,
        "apiKey":MY_NEWS_API
    }
    data = requests.get(NEWS_ENDPOINT, params=news_parameters)
    tsla_news = data.json()["articles"][:3]
    three_tsla_news = []
    for news in tsla_news:
        three_tsla_news.append(news["description"])

    print(three_tsla_news)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

