from django.apps import AppConfig

# 어플리케이션 설정용 클래스
class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"
