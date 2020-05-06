from django.urls import path
from . import views

urlpatterns = [
    # post_list 라는 뷰가 루트 URL에 할당됨. (메인페이지)
    path('', views.post_list, name='post_list'),
]