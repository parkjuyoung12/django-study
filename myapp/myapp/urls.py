# myapp에 대한 URL 설정 파일
"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 변수명 이대로! 바꾸면X
urlpatterns = [
    # path('url', 실행할 기능)
    path("admin/", admin.site.urls),

    # app/라는 주소가 실행되면 app 폴더의 urls를 참조 
    # /를 꼭 붙히자!
    path('app/', include('app.urls')), 
    
    path('friend/', include('friend.urls')),
]
# 리스트