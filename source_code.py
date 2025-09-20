import requests
#import streamlit as st

user_currency = input("Enter Your currency ex 'inr': ").lower()
url = f"https://api.coingecko.com/api/v3/simple/price"  #URL for coingeko

#function to return cryto data
def get_rates(coin_name):
    params = {
        "ids": f"{coin_name}",        
        "vs_currencies": f"{user_currency}",           
        "include_market_cap": "false",     
        "include_24hr_change": "false"     
    }
    response = requests.get(url,params=params)
    if response.status_code == 200:
        cryto_data = response.json()
        return cryto_data
    else:
        return response.status_code

while True:
    coin_name = input("Enter Cryto currency name (Enter quit to stop): ").lower()
    if coin_name == "quit":
        break
    else:
        data = get_rates(coin_name)
        print(f"The Current Price of {coin_name.upper()} is {data[coin_name][user_currency]} {user_currency.upper()}")

