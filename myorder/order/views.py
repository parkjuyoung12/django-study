from django.shortcuts import render
from .models import Order
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return HttpResponseRedirect('/order/')

def index(request):
    return render(request, 'order/index.html')

# 주문 등록
def add_order(request):
    if request.method == 'GET':
        return render(request, 'order/add_order.html')
    else:
        Order.objects.create(
            order_text = request.POST['prouduct_name'],
            price = request.POST['price'],
            address = request.POST['adress'],
        )
        return HttpResponseRedirect('/order/')
    
# 주문 리스트
def list_order(request):
    order_list = Order.objects.all()

    context = {
        'order_list' : order_list
    }
    return render(request, 'order/list_order.html', context)

# 주문 검색
def search_order(request):
    order_list = request.POST['search_order']
    print(order_list)

    startwiht = request.POST['startwith']
    print(startwiht)

    if startwiht == 'on':
        print('with')
        order_list = Order.objects.filter(order_text__startswith = order_list) 

    check = request.POST['check'] # 제품으로 검색인지, 주소로 검색인지
    if check == 'text': # 제품으로 검색
        order_list = Order.objects.filter(order_text__contains = order_list) 
    else: # 주소로 검색
        order_list = Order.objects.filter(address__contains = order_list) 
    
    context = {
        'order_list' : order_list
    }

    return render(request, 'order/list_order.html', context)

# 주문 보기
def show_order(request, id):
    order = Order.objects.get(id = id)

    context = {
        'menu' : order.order_text.split(','),
        'order' : order
    }
    return render(request, 'order/show_order.html', context)

# 주문 수정
def update_order(request, id):
    order = Order.objects.get(id = id)

    if request.method == 'GET':
        context = {
            'order' : order
        }
        return render(request, 'order/update_order.html', context)
    elif request.method == 'POST':
        order.order_text = request.POST['prouduct_name']
        order.price = request.POST['price']
        order.address = request.POST['address']
        order.save()
        
        return HttpResponseRedirect('/order/list_order/')

# 주문 삭제
def delete_order(request, id):
    Order.objects.get(id = id).delete()

    return HttpResponseRedirect('/order/list_order')


    

        
    



