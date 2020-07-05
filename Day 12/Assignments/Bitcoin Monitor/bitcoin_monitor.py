from bs4 import BeautifulSoup
import requests as rq
from datetime import datetime
import os
from time import sleep, time

session = rq.Session()

def get_BTC_price():
    head={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    url = "https://cryptowat.ch/assets/btc"
    site_html = session.get(url, headers=head)

    soup = BeautifulSoup(site_html.text, 'html.parser')
    span = soup.find('span', {'class': 'woobJfK-Xb2EM1W1o8yoE'})
    
    return span.text

def write_to_file(data):
    current_data_time = data['date-time']
    log_count = data['log']
    btc_price = data['btc']

    line = ",".join([log_count, current_data_time, "$"+btc_price, "\n"])
    try:
        if not os.path.exists("BTC_Monitor_logs.csv"):
            with open("BTC_Monitor_logs.csv", 'w+') as file:
                file.write("Log, Data Time, BTC_Price\n")
        
        with open('BTC_Monitor_logs.csv', 'a+') as file:
            file.write(line)
            return True

    except Exception as e:
        print(e)
        return False

def logger(interval, duration):
    data = {}
    
    dur_start = time()
    dur_end = time()

    if interval > duration*60:
        print("ERROR : Invalid Parametrs!")
        return False

    for _ in range(duration*60 // interval):

        data['date-time'] = datetime.now().strftime("%D %T")
        data['log'] = str(0) if 'log' not in data else str(int(data['log']) + 1)
        data['btc'] = get_BTC_price()

        if write_to_file(data):
            print(data['log'], "\t", data['date-time'], "\t", data['btc'], end="\r")
        else:
            print(data['log'], "\t", data['date-time'], "\t", "Error", end="\r")
       
        sleep(interval)
        dur_end = time()
    return True
        

def main():
    interval = int(input("Enter logging interval (sec): "))
    duration = int(input("Enter logging duration (min): "))
    if logger(interval, duration):
        print("\nLogging Done!")
    else:
        print("Aborted!")
    

if __name__ == "__main__":
    main()