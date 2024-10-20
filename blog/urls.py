from django.urls import path
from . import views
from django.urls import include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Post', views.blogImage)
 
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('api_root/', include(router.urls)),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # 장고가 post_detail 뷰로 보내, 게시글을 볼 수 있게 urls.py수정
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

