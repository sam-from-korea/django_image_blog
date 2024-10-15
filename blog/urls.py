from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # 장고가post_detail 뷰로 보내, 게시글을 볼 수 있게 urls.py수정
]