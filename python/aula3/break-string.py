#
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here

for headline in headlines:
    if len(news_ticker) >= 140:
        break
    elif len(news_ticker) + len(headline) > 140:
        index = len(headline) -(len(news_ticker) + len(headline) - 140)
        news_ticker += headline[:int(index)]
    else:
        news_ticker += headline + " "
        
print(len(news_ticker))        
print(news_ticker)
