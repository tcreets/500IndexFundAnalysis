import time
import requests
from config import key
import csv


stocks = ["VOO","SPY","IVV","RSP","QQQ"]
for stock in stocks:
    url = f"https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/2021-03-29/2022-03-25?adjusted=true&limit=300&apiKey={key}"
    data = requests.get(url)
    json_data = data.json()
    results_data = json_data["results"]
    ticker = json_data["ticker"]
    prices = [result["c"] for result in results_data]
    dates =  [time.strftime('%Y-%m-%d', time.localtime(result["t"]/1000)) for result in results_data]
    with open(f"{stock}STOCK.csv", "w", newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows([dates, prices])

