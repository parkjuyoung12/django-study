from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_order/', views.add_order),
    path('list_order/', views.list_order),
    path('search_order/', views.search_order),
    path('list_order/<int:id>/', views.show_order),
    path('list_order/<int:id>/update/', views.update_order),
    path('list_order/<int:id>/delete/', views.delete_order),
]
