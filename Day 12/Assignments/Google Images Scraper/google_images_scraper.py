import json, os
import requests as rq
from tqdm import tqdm
from bs4 import BeautifulSoup
from time import time

def query_request(query):
    query = "+".join(query.split())
    head={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    
    response = rq.get(url, headers=head)

    soup = BeautifulSoup(response.text, 'html.parser')

    return soup
    pass

def get_image(img_url):
    try:
        image_respons = rq.get(img_url)
        return image_respons
    except:
        return False
    pass


def main():
    query = input("Enter the Query: ")
    store_dir = "Scraped_Images/" + "_".join(query.split())

    result_soup = query_request(query)
    print("Got HTML Page")
    ignore_list = ['php']
    images_list = []
    for div in result_soup.find_all('div', {'class': 'rg_meta'}):
        link, img_type = json.loads(div.text)['ou'], json.loads(div.text)['ity']
        images_list.append((link, img_type))

    # print(len(images_list), "Images Found!")
    # for (img, Typ) in images_list:
    #     print(img, Typ)

    if not os.path.exists(store_dir):
        os.makedirs(store_dir)

    success, skipped, failed = 0, 0, 0
    for img_url, img_type in tqdm(images_list):
        if img_type in ignore_list:           
            skipped += 1
            continue

        result = get_image(img_url)
        if result:
            if len(img_type) == 0:
                with open(store_dir+"/img_"+str(int(time()))[-5:]+".jpg", "wb") as img:
                    for chunk in result:
                        img.write(chunk)
            else:
                with open(store_dir+"/img_"+str(int(time()))[-5:]+"."+img_type, "wb") as img:
                    for chunk in result:
                        img.write(chunk)
            success += 1
        else:
            failed += 1

    print("Download Done! ")
    print("Downloaded :", success)
    print("Skipped :", skipped)
    print("Failed :", failed)
    print("Total :", success + failed + skipped)

if __name__ == "__main__":
    main()