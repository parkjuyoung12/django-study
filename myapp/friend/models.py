from django.db import models

#'''모델'''
# 데이터베이스의 정보를 저장하는 객체
# ORM 방식으로 장고를 이용할때 필요한 클래스(Jave의 vo랑 비슷한 느낌)
# django.db.models.Model 클래스를 상속받는 하위 클래스
# 모델객체를 생성하게 되면 장고에서 해당 모델에 대한 DB 접근 API 자동으로 실행

# 모델 - DB의 매핑 관계
# 장고 모델 - Table
# 모델 속성 - Table의 column
# 모델 객체(1개) - Table의 row

# 모델 선언
class Friend(models.Model): #(상속받고 싶은 클래스 이름)
    # 열 선언
    # 짧은 문자열에 대해서 CharField를 사용(최대 길이 필순)
    friend_name = models.CharField(max_length = 10)
    # IntegerField : 정수 저장
    friend_age = models.IntegerField()
    # 긴 문자열에 대해서 TextField(비어있어도 OK)
    friend_bigo = models.TextField(null = True, blank = True)

    # 필드 옵션
    # null과 blank의 차이
    # null은 DB를 위한 항목, blank는 데이터 검증에 대한 항목
    # primary_key = True > 해당 필드를 기본키로 설정
    
    # 마이그레이션... migration : 작성된 모델을 토대로 DB에 DDL을 실행하는 것
    # 하위 앱을 settinig.py에 등록 해야지 사용할 수 있다

    # 1. 마이그레이션 파일 생성 (py manage.py makemigrations [앱 이름])
    # 2. 적용 (py manage.py migrate 앱 이름)
