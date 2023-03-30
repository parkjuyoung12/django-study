from django.db import models
from django.utils import timezone # 시간정보 모듈
from django.contrib.auth.models import User # DB auth_user 테이블과 매핑

# Create your models here.

class Board(models.Model):
    # 번호는 pk 설정 안하면 장고가 자동으로 id 부여해줌
    ### 필드와 필드 사이에 컴마 금지 ###
    title = models.CharField(max_length = 100) # 제목
    content = models.TextField(null = False, blank = False) # 내용
    # writer = models.CharField(max_length= 10) # 글쓴이
    input_date = models.DateTimeField(default = timezone.now) # 작성일
    view_count = models.IntegerField(default = 0)
    # DB에는 필드이름_기본키 이름으로 열이 생성됨
    author = models.ForeignKey(User, on_delete = models.CASCADE) # 로그인 정보로 글쓴이

    # Java의 tostring이랑 비슷
    # 객체정보를 문자열로 돌려줌
    # admin페이지에서 글 제목으로 보려고
    def __str__(self):
        return f'{self.id} ~ {self.title}'

# 댓글 정보를 포함하는 모델
class Reply(models.Model):
    # pk : 장고가 알아서 만들어줌(id)
    # 게시글 번호(fk)
    board_obj = models.ForeignKey(Board, on_delete = models.CASCADE)
    # 사용자(fk)
    user = models.ForeignKey(User, on_delete = models.CASCADE) # 사용자는 지워져도 댓글삭제X, null로 바뀜
    # 댓글내용
    reply_content = models.TextField(null = False, blank = False)
    # 작성시간
    input_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.reply_content