from django import views
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('' ,  index  , name="index"),
    path('register/' , register_attempt , name="register_attempt"),
    path('login/' , login_attempt , name="login_attempt"),
    path('token/' , token_send , name="token_send"),
    path('success/' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error/' , error_page , name="error"),
    path('logout/', logout_user, name="logout"),
    path('post/', post, name="post"),
    path('post/<slug:post_slug>/', show_post, name='post'),
    # path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
]
