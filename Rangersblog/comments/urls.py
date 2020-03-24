from django.urls import path, re_path
from .import views


app_name = 'comments'
urlpatterns = [
path('', views.post_comment, name='post_comment'),
path('view/', views.view_comment, name='view_comment'),

]