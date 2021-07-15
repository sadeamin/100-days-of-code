import requests
from requests.api import patch
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

api_key = "VK1WW2MMK0PDCZ51"
news_api_key = "c6745ed7f6e54ec5bec8c22f9ed4eb33"

""" 

Examples (click for JSON output)
IBM (United States)
https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo

https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=demo


e.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)

"""

parameter = {
    "function" :"TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME, 
    "apikey": api_key
}


## STEP 1: Use https://www.alphavantage.co/documentation/#daily
    
responce = requests.get(url=STOCK_ENDPOINT, params=parameter)
responce.raise_for_status()
data = responce.json()['Time Series (Daily)']

# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

data_list = [v for k, v in data.items()]
yesterday_data = data_list[0]
yesterday_close_data = float(yesterday_data['4. close'])
# print(yesterday_close_data)

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_close_data = float(day_before_yesterday_data['4. close'])
# print(day_before_yesterday_close_data)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(yesterday_close_data - day_before_yesterday_close_data)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
    



#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / yesterday_close_data) * 100
print(diff_percent)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

news_parameter = {
    "apiKey": news_api_key,
    "qinTitle": COMPANY_NAME
}

if abs(diff_percent) > 0.12:
    news_responce = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    articles = news_responce.json()["articles"]
    # print(articles)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    formatted_articles = [f"{STOCK_NAME}: {up_down}{int(diff_percent)}% \n Headline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]
    
    
    #TODO 9. - Send each article as a separate message via Twilio. 

    account_sid = "ACd06fb7ca26f0747854632a9545ed1ab5"
    auth_token = "ef067d6d51f4c3ee00864fcb880b28e4"

    client = Client(account_sid, auth_token)



    #Optional TODO: Format the message like this: 
    for article in formatted_articles:
        message = client.messages.create(
            body=article, 
            from_='+15752686391', 
            to='+880 1749-319102'
                                        )

        print(message.status)



"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

