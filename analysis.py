import csv
import statistics
import matplotlib.pyplot as plt

stocks = ["VOO","SPY","IVV","RSP","QQQ"]
#Pull stock data
for stock in stocks:
    stock_prices = []
    with open(f"{stock}STOCK.csv", "r") as infile:
        reader = csv.reader(infile)
        # save this dictReader object into a list of dictionaries to analyze
        stock_prices = list(reader)[1]



#find population st dev for each week

    i = 0

    stock_stdev = []
    while i < len(stock_prices):
        if i+4 >len(stock_prices):
            break
        day1 = float(stock_prices[i])
        day2 = float(stock_prices[i + 1])
        day3 = float(stock_prices[i + 2])
        day4 = float(stock_prices[i + 3])
        day5 = float(stock_prices[i + 4])
        i += 5
        stock_stdev.append(statistics.pstdev([day1,day2,day3,day4,day5]))
    

#create plot line


    plt.plot(stock_stdev, label = f"{stock}")
    plt.title("Standard Deviation for Top ETFs")
    plt.xlabel("Weeks")
    plt.ylabel("Standard Deviation")
    plt.legend(loc="upper left")
    plt.savefig(f"{stock}.png")


    
