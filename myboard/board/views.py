from django.shortcuts import render
from .models import Board
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

# localhost:8000으로 왔을때 board로 연결
def home(request):
    return HttpResponseRedirect('/board/')

# 게시판 목록 보기
def index(request):
    print('indext() 실행')

    # 반환되는 queryset에 대해서 order_by함수 이용하면 특정 필드 기준으로 정렬
    # order_by에 들어가는 필드 이름 앞에 -를 붙히면 내림차순(DESC) 아니면 오름차순(ASC)
    # board_list = Board.objects.all().order_by('-id')

    result = None # 필터링된 리스트
    
    context = { }

    # request.GET : GET 방식으로 보낸 데이터들을 딕셔너리 타입으로 저장
    print(request.GET)

    # 검색 조건과 검색 키워드가 있어야 필터링 실행
    if 'searchType' in request.GET and 'searchWord' in request.GET:
        search_Type = request.GET['searchType'] # GET안의 문자열은
        search_Word = request.GET['searchWord'] # HTML의 name속성

        print("search_Type : {}, search_Word : {}".format(search_Type, search_Word))

        # match : Jave의 switch 비슷
        if search_Type == 'title':
             # 검색 기준이 제목일 때
            result = Board.objects.filter(title__contains = search_Word)
        elif search_Type == 'writer': # 검색 기준이 글쓴이일 때
            result = Board.objects.filter(writer__contains = search_Word)
        elif search_Type == 'content': # 검색 기능이 내용일 때
            result = Board.objects.filter(content__contains = search_Word)

        # 검색을 했을때만 검색 기준과 키워드를 context에 넣는다
        context['searchType'] = search_Type
        context['searchWord'] = search_Word
        
    else: # QueryDict에 검색 조건과 키워드가 없을 때
        result = Board.objects.all()

    # 검색 결과 또는 전체 목록을 id 내림차순 정렬
    result = result.order_by('-id')

    # context['board_list'] = result

    # 페이징 넣기
    # Paginator(목록, 목록에 보여줄 개수)
    paginator = Paginator(result, 10)

    # Paginator 클래스를 이용해서 자른 목록의 단위에서
    # 몇번째 단위를 보여줄 것인지 정한다
    page_obj = paginator.get_page(request.GET.get('page'))

    # 페이징한 일부 목록을 반환
    context['page_obj'] = page_obj
    
    return render(request, 'board/index.html', context)

# 글 읽기
def read(request, id):
    print("id : ", id)

    board = Board.objects.get(id = id)

    # 조회수 올리기
    board.view_count += 1
    board.save()

    context = {
        'board' : board
    }

    return render(request, 'board/read.html', context)

# 글 쓰기
# 내가 따로 만든 로그인 URL이 있다면 login_url 키워드 변수를 적어야한다
@login_required(login_url='common:login')
def write(request):
    if request.method == 'GET': # 요청방식이 GET이면 화면 표시
        return render(request, 'board/board_form.html')
    else: # 요청방식이 POST일 때 할일
        # 폼의 데이터를 DB에 저장
        title = request.POST['title']
        content = request.POST['content']
        author = request.user # 요청에 들어있는 User 객체

        # 현재 세션정보의 writer라는 키를 가진 데이터 취득
        # session_writer =  request.session.get('writer')
        # if not session_writer: # 세션에 정보가 없는 경우
        #     # 폼에서 가져온 writer 값 세션에 저장
        #     request.session['writer'] = request.POST['writer']
        # print("session_writer : ", session_writer)

        # 방법1, 객체.save() 
        # board = Board(
        #     title = title,
        #     writer = writer,
        #     content = content 
        # )
        # board.save() # db에 insert
            
        # 방법2, 모델.objects.create(값)   
        Board.objects.create(
        title = title,
        author = author, # user 객체 저장
        # writer = request.session.get('writer'), # 세션에 있는 값 저장
        content = content
        )

        return HttpResponseRedirect('/board/')
    
# 글 수정
@login_required(login_url='common:login')
def update(request, id):
    board = Board.objects.get(id = id)
    
    # 로그인 정보가 맞지 않을 때
    if board.author.username != request.user.username:
        return HttpResponseRedirect('/board/')
    
    if request.method == 'GET':
        context = {'board' : board }
        return render(request , 'board/board_update.html', context)
    else:
        board.title = request.POST['title']
        # board.writer = request.POST['writer']
        board.content = request.POST['content']
        board.save() # save를 해야 DB에 반영됨!!!

        # 수정 후에 해당 글로 다시 이동
        redirect_url  = '/board/' + str(id) + '/'
        return HttpResponseRedirect(redirect_url)
        
# 글 삭제
@login_required(login_url='common:login')
def delete(request, id):
    print("id : ", id)
    # 해당 객체를 가져오기
    board = Board.objects.get(id = id)

    # 글 작성자의 id와 접속한 사람의 id가 같을때
    if board.author.username == request.user.username:
        board.delete()
    # 다를때
    return HttpResponseRedirect('/board/')





