from pycoingecko import CoinGeckoAPI
from datetime import datetime, timedelta, date
import smtplib
import os

import smtplib

MY_EMAIL = "pythonbotmail040@gmail.com"
MY_PASSWORD = os.environ.get('EMAIL_PASS')

send_email_list = ['thijsgeertman@hotmail.com']
data = CoinGeckoAPI()

yesterday = date.today() - timedelta(days=1)
yesterday_formatted = yesterday.strftime('%d-%m-%Y')
print(yesterday_formatted)

coins = data.get_price(ids=['bitcoin', 'ethereum', 'litecoin', 'dogecoin'], vs_currencies='eur')
now_price = int(coins['bitcoin']['eur'])
eth_price = int(coins['ethereum']['eur'])
doge_price = (coins['dogecoin']['eur'])

yesterdays_price = data.get_coin_history_by_id(id=['bitcoin'], date=yesterday_formatted)
yes_price = int(yesterdays_price['market_data']['current_price']['eur'])

yesterdays_price_eth = data.get_coin_history_by_id(id=['ethereum'], date=yesterday_formatted)
yes_price_eth = int(yesterdays_price_eth['market_data']['current_price']['eur'])

yesterdays_price_doge = data.get_coin_history_by_id(id=['dogecoin'], date=yesterday_formatted)
yes_price_doge = (yesterdays_price_doge['market_data']['current_price']['eur'])

calculation_btc = (now_price - yes_price) / yes_price * 100
print(f"{calculation_btc}%")

calculation_eth = (eth_price - yes_price_eth) / yes_price_eth * 100
print(f"{calculation_eth}%")

calculation_doge = (doge_price - yes_price_doge) / yes_price_doge * 100
print(f"{calculation_doge}%")

if calculation_btc < -25 and calculation_eth < -25 and calculation_doge - 25:
    print("Wow alle coins zijn met 25% of meer gezakt! ⬇️📉")
elif calculation_btc < -15 and calculation_eth < -15 and calculation_doge - 15:
    print("Alle coins zijn met 15% gezakt 📉")
elif calculation_btc < -25:
    print("bitcoin is met 25% gedaald 📉")
elif calculation_doge < -25:
    print("Doge is met 25% gezakt 📉")
elif calculation_eth < -25:
    print("ETH is met 25% gezakt 📉")
elif calculation_btc > 25 and calculation_eth > 25 and calculation_doge > 25:
    print("Wow alle coins zijn met 25% gestegen. 📈")

if calculation_btc < -25 and calculation_eth < -25 and calculation_doge - 25:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="thijsgeertman@hotmail.com",
            msg="Wow alle coins zijn met 25% of meer gezakt! ⬇️📉"
        )
elif calculation_btc < -15 and calculation_eth < -15 and calculation_doge - 15:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="thijsgeertman@hotmail.com",
            msg="Alle coins zijn met 15% gezakt 📉"
        )
elif calculation_btc < -25:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="thijsgeertman@hotmail.com",
            msg="bitcoin is met 25% gedaald 📉"
        )
elif calculation_doge < -25:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="thijsgeertman@hotmail.com",
            msg="Doge is met 25% gedaald 📉"
        )
elif calculation_eth < -25:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="thijsgeertman@hotmail.com",
            msg="ETH is met 25% gedaald 📉"
        )
elif calculation_btc > 25 and calculation_eth > 25 and calculation_doge > 25:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="thijsgeertman@hotmail.com",
            msg="Wow alle coins zijn met 25% gestegen. 📈"
        )
