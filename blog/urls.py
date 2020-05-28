from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new', views.post_new, name='post_new'),
    #post - author list
    path('post/post_author_list<int:author_id>', views.post_author_list, name='post_author_list'),
    #
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('join/', views.signup, name='join'),
]