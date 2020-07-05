from bs4 import BeautifulSoup
import requests as rq
from tqdm import tqdm
from time import time
import os

def get_request(url):
    # print(url)
    try:
        head={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
        response = rq.get(url, headers=head)
        return response
    except Exception as e:
        print(e)
        return response

def make_soup(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')
    return soup

def main():
    keywords = input("Enter the Pexel Search query: ").split()

    query = "%20".join(keywords)
    url = "https://www.pexels.com/search/"+query+"/"
    response = get_request(url)

    pexel_soup = make_soup(response.text)

    images = pexel_soup.find_all('img', {'class': 'photo-item__img'})
    img_src_list = []
    for img in images:
        img_src = img['src'].split("?")[0]
        # print(img_src)
        img_src_list.append(img_src)
    
    #Create Images Link Text File
    with open("_".join(keywords)+".txt", "a+") as file:
        for link in img_src_list:
            file.write(link+"\n")

    
    path = "./Pexel_Scraped_Images/" + "_".join(keywords)
    
    if not os.path.exists(path):
        os.mkdir(path)

    #Downloading images   
    for img in tqdm(img_src_list):
        img_data = get_request(img)
        
        with open(path + "/img_"+str(int(time()))+".jpg" , "wb") as img:
            for chunk in img_data:
                img.write(chunk)
            
    print("Done!")

if __name__ == "__main__":
    main()