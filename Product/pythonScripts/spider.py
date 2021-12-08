from bs4 import BeautifulSoup as bs
import requests


def ScrapeSearch(product_search):
    my_url = "https://www.newegg.com/p/pl?d=" + product_search + "&N=4814"
    r = requests.get(my_url)
    soup = bs(r.content, features="html.parser")

    containers = soup.findAll('div', {'class': 'item-container'})

    names = []
    prices = []
    ratings = []
    urls = []
    img_urls = []
    product_item = [names, prices, ratings, urls, img_urls]

    for i, container in enumerate(containers, start=1):
        name = container.find('img')['title']
        names.append(name)

        try:
            rating = container.find('i')['class'][1]
        except:
            rating = 'No ratings'
        ratings.append(rating)

        try:
            price = container.find('li', 'price-current').text.replace('|', '').replace('–', '').strip()
        except:
            price = 'Not Available'
        prices.append(price)

        url = container.find('a')['href']
        urls.append(url)

        img_url = container.find('img')['src']
        img_urls.append(img_url)
        #print(img_urls)

    return product_item


