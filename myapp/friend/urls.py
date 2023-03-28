# 장고의 기본 라이브러리
from django.urls import path

# 현재 패키지(.)에서 views를 import
from.import views

urlpatterns = [
    # 해당하는 주소가 입력된다면~
    path('', views.index), #myapp의 urls.py
    path('add_friend/', views.add_friend), # (주소가 실행이 되면, 함수 호출)
    path('create_friend/', views.create_friend),
    path('show_all/', views.show_all),
    path('search_name/', views.search_name),
    # <타입:이름> path converter(str, int, slug, uuid, path)
    #이름은 views와 같게 아무거나 해도 됨
    path('delete_friend/<int:id>/', views.delete_friend), 
    path('update_friend/<int:id>/', views.update_friend)
]