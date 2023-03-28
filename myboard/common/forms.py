from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

# UserCreationFrom에 있는 username, password1,2 3가지 속성 외 email을 추가하기 위해
# UserCreationFrom을 상속받는 UserForm을 작성
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    first_name = forms.CharField
    last_name = forms.CharField

    class Meta: # 폼의 정보를 담고 있는 내부 클래스
        model = User
        fields = ("username", "email", "first_name", "last_name")

class CustomChangeForm(UserChangeForm):

    class Meta:
        model = User    
        fields = ("email", "first_name", "last_name")