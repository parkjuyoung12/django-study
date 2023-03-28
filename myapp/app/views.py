from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# view.py의 함수에 들어있는 request 파라미터 : 요청 객체
def index(request):
    template = loader.get_template('app/index.html') # template폴더 안

    # dictionaray타입의 변수 context
    # 화면에 표시할때 넘겨줄 정보
    context = {}

    # 응답객체 안에 템블릿과 표시할 값(context), 요청(request)
    return HttpResponse(template.render(context, request))

def call1(request):
    template = loader.get_template('app/template.html')
    print('request : ', request)

    context = {}

    return HttpResponse(template.render(context, request))

# RSETful 방식으로 호출된 주소에 대한 함수
# 요청 객체 뒤의 파라미터에 해당하는 변수명 써줘야함
def call2(request, number):
    print('number : ', number)
    # 파이썬에서는 자료형이 다른것을 합칠수X
    # print('number : ' + number)

    template = loader.get_template('app/template.html')

    context = {}

    return HttpResponse(template.render(context, request))

def call3(request):
    # requset 객체에서 가져오는 모든 데이터는 str타입
    name = request.GET['name']
    age = request.GET['age']
    print("name :", name)
    print("age : ", age)   

    return HttpResponse("호출됨")

def call4(request):
    template = loader.get_template('app/template.html')

    context = {
        # 문자열 하나 보내기
        'item' : 'This text is sent from server.',
        'name' : '오승재',
        # 리스트 보내기
        'board_list' : [
            {'title' : '1등', 'writer' : '홍길동'},
            {'title' : '2등', 'writer' : '임꺽정'},
            {'title' : '3등', 'writer' : '장길산'},
        ],
        # 딕셔너리 보내기
        'mydata' : {
            'name' : '오승재',
            'age' : 27,
            'adress' : '광주'
        }
    }

    return HttpResponse(template.render(context, request))

def call5(request):

    str_list = ['피카츄', '파이리', '꼬부기']

    template = loader.get_template('app/tag.html')

    context = {
        'list' : str_list,
        'number' : 8
    }

    return HttpResponse(template.render(context, request))

def call6(request):
    template = loader.get_template('app/form.html')
    context = {}

    return HttpResponse(template.render(context, request))

# 폼에 입력된 데이터 가져오기
def call_submit(request):
    name = request.POST['name']
    age = request.POST['age']

    print("name : ", name)
    print("age : ", age)
    
    return HttpResponse("submit OK")

def call7(request):
    template = loader.get_template('app/tag.html')

    context = {
        'name' : '오승재', 
        'age' : 27,
        'adress' : '광주', 

    }

    return HttpResponse(template.render(context, request))
