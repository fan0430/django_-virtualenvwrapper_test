from django.shortcuts import render, redirect
import logging
logger = logging.getLogger(__name__)
# Create your views here.
from .models import Coffee
from django.http import HttpResponse, HttpResponseNotFound

def home(request):
    print('进入 home 视图')
    template='home.html'
    return render(request, template)
def menu(request):
    print('进入 menu 视图')
    coffees = Coffee.objects.all()
    print('my_model_instance = ' + str(coffees))
    for _coffee in coffees:
        # print('__str__ =='+str(_coffee.__str__()))
        # print('get_absolute_url =='+str(_coffee.get_absolute_url()))
        print('get_absolute_url2 =='+str(_coffee.get_absolute_url2(2)))
        for field_name in Coffee.model_fields:
            field_value = getattr(_coffee, field_name)
            print(f"{field_name}: {field_value}")
    template = 'menu.html'
    return render(request, template, {'coffee':coffees})

    # 轉跳網址
    # return redirect(_coffee.get_absolute_url2(2))
    # return redirect('/catalog/home/')

# def other(request):
#     print('进入 other 视图')
#     template='other.html'
#     return render(request, template)
def other(request):
    print("request = "+str(request))
    _url = request.path
    print("_url = "+str(_url))
    return HttpResponse(f"The requested URL '{_url}' was not found.")
    # return HttpResponseNotFound('Page not found')
def add(request):
    print('进入 add 视图')
    coffee_instance = Coffee(name= "fan5", price = 5,)
    print(str(coffee_instance))
    coffee_instance.save()


    template='home.html'
    return render(request, template, {'str':'Add'})
def update(request):
    print('进入 update 视图')
    coffees = Coffee.objects.all()
    # content = coffees.filter(name = 'fan1', price = 2 )
    # print(str(content[0].id))
    # content.update(price = 2)
    content = coffees.filter(name__in = ['fan2', 'fan3']).values('name', 'id')
    print(content)


    # get 不能直接 update 可以用save 更新
    # content = Coffee.objects.get(name = 'fan2')
    # addPrice = content.price + 1
    # content.price = addPrice
    # content.save()

    # coffees = Coffee.objects.all()
    # content = coffees.filter(id = 3)
    # addPrice = content[0].price + 1
    # content.update(price = addPrice)

    # coffees = Coffee.objects.all()
    # content = coffees.filter(name = 'fan1')
    # addPrice = content[0].price + 1
    # print(content[0])
    # _con = content[0]
    # _con.price = addPrice
    # _con.save()
    # content.update(price = addPrice)


    template='home.html'

    return render(request, template, {'str':'Update'})