from bs4 import BeautifulSoup as bs
import requests
from Product.models import Products
from .text import send_text
from Account.models import Profile


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

def ScrapeProduct():

    products = Products.objects.all()
    #print(products.values_list('product_url'))
    print('hello')

    #send_text('work', 'plz','im dying','yes')

    for i in products:

        my_url = i.product_url
        r = requests.get(my_url)
        soup = bs(r.content, features="html.parser")
        price = soup.find('li', 'price-current').find('strong').text + soup.find('li', 'price-current').find('sup').text

        #print(price)
        price = price.replace(",", "")

        product = Products.objects.get(id=i.id)
        product.price = price
        product.save()


        user_id = i.user_id
        phone_number = Profile.objects.get(user_id=user_id).phone_number
        try:
            if i.alert == True and i.sent_text == False:
                print(i.id)
                i.sent_text = True
                i.save()

                #print(phone_number)

                product = Products.objects.get(id=i.id)
                send_text(product.product_name, str(product.price), product.product_url, str(phone_number))

        except:
            pass

    print('done')
    # for i in products:
    #     #print(i.product_url)
    #
    #     my_url = i.product_url
    #     r = requests.get(my_url)
    #     soup = bs(r.content, features="html.parser")
    #     price = soup.find('li', 'price-current').find('strong').text + soup.find('li', 'price-current').find('sup').text
    #
    #     #print(price)
    #     price = price.replace(",", "")
    #
    #     product = Products.objects.get(id=i.id)
    #     product.price = price
    #     product.save()
    #
    #
    #
    #     if product.alert == True and product.sent_text == False:
    #         print('Price: ' + price)
    #         print('price_point: ' + str(product.price_point))
    #         #product.sent_text = True
    #         #product.save()
    #         if float(price) >= int(product.price_point):
    #             product.sent_text = True
    #             product.save()
    #             user_id = product.user_id
    #             phone_number = Profile.objects.get(user_id=user_id).phone_number
    #             # print(user_id)
    #             # print(phone_number)
    #             send_text(product.product_name, price, product.product_url, phone_number)



        # try:
        #     print('Price: ' + price)
        #     print('price_point: ' + product.price_point)
        #     # if float(price) >= int(product.price_point):
        #     #     product.sent_text = True
        #     #     product.save()
        #     #     user_id = product.user_id
        #     #     phone_number = Profile.objects.get(user_id=user_id).phone_number
        #     #     send_text(product.product_name, price, product.product_url, phone_number)
        # except:
        #     pass
