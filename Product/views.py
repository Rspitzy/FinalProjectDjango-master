from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .pythonScripts import spider, text
from .models import Products
import re

@login_required(login_url='login')
def index(request):

    products = Products.objects.filter(user=request.user)
    context = {'products': products}

    return render(request, 'products/index.html', context)


@login_required(login_url='login')
def search(request):
    system = request.POST.get('system')

    scraper = spider
    product_list = scraper.ScrapeSearch(system)
    #print(product_list)


    product_dictionarys = []

    keys = ['product_name', 'product_price', 'product_rating', 'product_url', 'product_img', 'product_index']

    for item in range(len(product_list[0])):

        values = [product_list[0][item], product_list[1][item], product_list[2][item], product_list[3][item], product_list[4][item], item]
        #print(values)
        dictionary = dict(zip(keys, values))
        product_dictionarys.append(dictionary)



    # text_user = text
    # text_user.send_text(system)

    context = {'system': system,
               'product_dict': product_dictionarys,
               }

    return render(request, 'products/search.html', context)

@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        #print(request.POST['product_name'])
        product_name = request.POST['product_name']

        price = request.POST['price']
        price = price.replace(',', '')
        fixed_price = re.findall(r'\d+', price)
        # print(fixed_price)
        price = fixed_price[0] +"." + fixed_price[1]

        # print(price)

        price_point = request.POST['price_point']
        price_point = price_point.replace(",", "").replace("$","")
        if price_point == "":
            price_point = None

        alert = request.POST['alert']
        if alert == 'true':
            alert = True
        else:
            alert = False
        # print(alert)
        # print(request.user.id)

        product_url = request.POST['product_url']
        product_img = request.POST['product_img']
        new_product = Products(user=request.user, product_name=product_name, price=price, price_point=price_point, alert=alert, product_url=product_url, product_img=product_img)
        new_product.save()


    return HttpResponse('')

@login_required(login_url='login')
def delete(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    return redirect('index')
