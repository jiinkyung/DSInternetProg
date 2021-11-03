from django.urls import path
from . import  views

urlpatterns = [ #서버 IP/blog/
 #   path('<int:pk>/', views.single_post_page),
 #   path('', views.index),

    path('category/<str:slug>', views.category_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),

]