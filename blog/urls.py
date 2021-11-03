from django.urls import path
from . import  views

urlpatterns = [ #서버 IP/blog/
 #   path('<int:pk>/', views.single_post_page),
 #   path('', views.index),

    path('create_post/', views.PostCreate.as_view()),
    path('tag/<str:slug>', views.tag_page),
    path('category/<str:slug>', views.category_page), #서버 IP/blog/category/slug
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),

]