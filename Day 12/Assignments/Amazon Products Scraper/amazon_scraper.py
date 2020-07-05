import requests as rq
from bs4 import BeautifulSoup
import os

session = rq.Session()

def get_requests(url):
    head={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    print(url)
    try:
        response = session.get(url, headers=head)
        return response
    except:
        return response

def make_soup(html_data):
    data = BeautifulSoup(html_data, "html.parser")
    return data
    pass

def main():
    price = input("Enter the price of phone: ")
    url = "https://www.amazon.in/s?k=phones+under+" + price
    result = get_requests(url)
    
    if result:
        amazon_soup = make_soup(result.text)
        
        phone_name_spans = amazon_soup.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'})
        offer_prices_spans = amazon_soup.find_all('span', {'class': 'a-price'})
        actual_prices_spans = amazon_soup.find_all('span', {'class': 'a-price a-text-price'})
        
        file_name = "phone_under_"+str(price) + ".txt"
        try:                
            for i, j, k in zip(phone_name_spans, offer_prices_spans, actual_prices_spans):
                offer_price = j.find('span', {'class':'a-offscreen'}).text
                actual_price = k.find('span', {'class':'a-offscreen'}).text

                line = " ".join([i.text, offer_price, actual_price, "\n"])

                with open(file_name, 'a+', encoding="utf-8") as file:
                    file.write(line)

            print("\nDone!\n")
        except Exception as e:
            print(e)

    else:
        print("Problem :",result.status_code)


if __name__ == "__main__":
    main()
