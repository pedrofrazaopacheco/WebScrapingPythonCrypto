from bs4 import BeautifulSoup as bs
import requests

coins_file = open("Coins notebook.txt", "a")
coins_file.write("\n")
import datetime

x = str(datetime.datetime.now())
coins_file.write("\nTime: " + x[:-7])
weekday = datetime.date.today().weekday()

total_dollar = 0
total_euro = 0

def weather(url):
    link = requests.get(url)
    soup_new = bs(link.content, "html.parser")
    today = str(soup_new.find(class_="bk-focus__qlook"))
    location = str(soup_new.find_all(class_="headline-banner__title"))
    def title(quote):
        start = quote.find('title="') + len('title="')
        end = quote.find('."')
        substring = quote[start:end]
        title_str = " | Weather: " + substring
        return title_str
    def number(quote):
        start = quote.find('<div class="h2">') + len('<div class="h2">')
        end = quote.find('°C</div><')
        substring = quote[start:end]
        number_str = " | Temperature Right Now: " + substring + "°C"
        return number_str
    def max_min(quote):
        start = quote.find('Forecast:') + len('Forecast:')
        end = quote.find('°C</span><br/>')
        substring = quote[start:end]
        max_min_str = " | Max & Min: " + substring[1:]
        return max_min_str
    print("Location: " + location[47:-6] + title(today) + number(today) + max_min(today))
    coins_file.write("\n" + "  " + "Location: " + location[47:-6] + title(today) + number(today) + max_min(today))

def crypto(url, new, qt):
    global total_euro, total_dollar
    link = requests.get(url)
    soup_new = bs(link.content, "html.parser")
    quote_new = str(soup_new.find_all(class_="priceValue"))
    global status
    if True:
        try:
            percent_new = str(soup_new.find_all(class_="sc-15yy2pl-0 gEePkg"))
            if ">" in percent_new[-22]:
                status = "  +" + percent_new[-21:-17] + " % within 24 hours"
            elif ">" in percent_new[-23]:
                status = "  +" + percent_new[-22:-17] + " % within 24 hours"
            else:
                status = "  +" + percent_new[-23:-17] + " % within 24 hours"
        except:
            try:
                percent_new = str(soup_new.find_all(class_="sc-15yy2pl-0 feeyND"))
                if ">" in percent_new[-22]:
                    status = "  -" + percent_new[-21:-17] + " % within 24 hours"
                elif ">" in percent_new[-23]:
                    status = "  -" + percent_new[-22:-17] + " % within 24 hours"
                else:
                    status = "  -" + percent_new[-23:-17] + " % within 24 hours"
            except:
                pass
    try:
        balance = str(round(qt * float(quote_new[26:-7]), 2))
        balance_euro = str(round(float(balance) * 0.85, 2))
        margin_error = str(round(float(balance_euro) * 0.01, 2))
        new_print = new.title() + " price is at: " + quote_new[25:-7] + status + " | Balance: $" + balance + " | Balance €" \
                    + balance_euro + " (with a margin error of €" + margin_error + ")"
        print(new_print)
        coins_file.write("\n" + "  " + new_print)
        total_dollar += float(balance)
        total_euro += float(balance_euro)
        return
    except:
        pass
    try:
        balance = str(round(qt * float(quote_new[26:28] + quote_new[29: -7]), 2))
        balance_euro = str(round(float(balance) * 0.85, 2))
        margin_error = str(round(float(balance_euro) * 0.01, 2))
        new_print = new.title() + " price is at: " + quote_new[25:-7] + status + " | Balance: $" + balance + " | Balance €" \
                    + balance_euro + " (with a margin error of €" + margin_error + ")"
        print(new_print)
        coins_file.write("\n" + "  " + new_print)
        total_dollar += float(balance)
        total_euro += float(balance_euro)
        return
    except:
        pass
    try:
        balance = str(round(qt * float(quote_new[26:27] + quote_new[28: -7]), 2))
        balance_euro = str(round(float(balance) * 0.85, 2))
        margin_error = str(round(float(balance_euro) * 0.01, 2))
        new_print = new.title() + " price is at: " + quote_new[25:-7] + status + " | Balance: $" + balance + " | Balance €" \
                    + balance_euro + " (with a margin error of €" + margin_error + ")"
        print(new_print)
        coins_file.write("\n" + "  " + new_print)
        total_dollar += float(balance)
        total_euro += float(balance_euro)
        return
    except:
        pass

def yahoo_stock(url):
    link = requests.get(url)
    soup_new = bs(link.content, "html.parser")
    name = str(soup_new.find_all(class_="D(ib) Fz(18px)"))
    price = str(soup_new.find_all(class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"))
    variation = str(soup_new.find_all(class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)"))
    market_cap = str(soup_new.find('td', {'data-test': 'MARKET_CAP-value'}))
    if "<" in market_cap[130:139] and "B" in market_cap[130:139]:
        print("Stock:", name[45:-6], "| Price:", price[75:-8], "| Market Cap:", market_cap[130:137], "| Variation:",
              variation[93:-8])
        coins_file.write("\n" + "  " + "Stock: " + name[45:-6] + "| Price: " + price[75:-8] + " | Market Cap:" +
                         market_cap[130:137] + "| Variation: " + variation[93:-8])
    elif "B" in market_cap[130:139]:
        print("Stock:", name[45:-6], "| Price:", price[75:-8], "| Market Cap:", market_cap[130:138], "| Variation:",
              variation[93:-8])
        coins_file.write("\n" + "  " + "Stock: " + name[45:-6] + "| Price: " + price[75:-8] + " | Market Cap:" +
                         market_cap[130:138] + "| Variation: " + variation[93:-8])
    else:
        print("Stock:", name[45:-6], "| Price:", price[75:-8], "| Market Cap:", market_cap[130:136], "| Variation:",
              variation[93:-8])
        coins_file.write("\n" + "  " + "Stock: " + name[45:-6] + "| Price: " + price[75:-8] + " | Market Cap:" +
                         market_cap[130:136] + "| Variation: " + variation[93:-8])

def user_choice():
    print()
    print("Do you want to put any link?")
    print("Option 1: Yes")
    print("Option 2: No")
    op = int(input("Please the number with the corresponding option: "))
    if op == 1:
        user_link = input("Please insert your link: ")
        user_coin_name = input("Please insert the coin name (lowercase): ")
        qt = float(input("Please input your quantity"))
        crypto(user_link, user_coin_name, qt)
        user_choice()
    elif op == 2:
        pass

def stock_greeting(x):
    print("Stocks")
    x = int(x[11:13] + x[14:16])
    if 1430 <= x < 2100 and (weekday < 5):
        print("The market is open!")
    else:
        print("The market is closed")

print("Bons dias Pedrinho! Here's your briefing: ")
print()

weather("https://www.timeanddate.com/weather/@2271985")

print()
print("Crypto")
coins_file.write("\n")
crypto("https://coinmarketcap.com/currencies/bitcoin/", "bitcoin", 0)
crypto("https://coinmarketcap.com/currencies/ethereum/", "ethereum", 0)
crypto("https://coinmarketcap.com/currencies/enjin-coin/", "enjin", 0)
crypto("https://coinmarketcap.com/currencies/kusama/", "ksm", 0)
crypto("https://coinmarketcap.com/currencies/cardano/", "ada", 0)
crypto("https://coinmarketcap.com/currencies/coti/", "coti", 0)

print("Total $ " + str(round(total_dollar, 2)) + " | Total € " + str(round(total_euro, 2)))
print()

stock_greeting(x)

coins_file.write("\n")
yahoo_stock("https://finance.yahoo.com/quote/AAPL?p=AAPL")
yahoo_stock("https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch")
yahoo_stock("https://finance.yahoo.com/quote/AMZN?p=AMZN")
yahoo_stock("https://finance.yahoo.com/quote/GOOG?p=GOOG")
yahoo_stock("https://finance.yahoo.com/quote/FB?p=FB")
yahoo_stock("https://finance.yahoo.com/quote/TSLA?p=TSLA")
yahoo_stock("https://finance.yahoo.com/quote/NFLX?p=NFLX")

input("Press ENTER to exit: ")

# https://www.youtube.com/watch?v=eMOA1pPVUc4
