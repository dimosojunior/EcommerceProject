
from django.urls import path
from . import views

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signin2', views.signin2, name='signin2'),
    
    path('logout', views.logout, name='logout'),



    path('signin_for_my_account', views.signin_for_my_account, name='signin_for_my_account'),
    path('signup_for_my_account', views.signup_for_my_account, name='signup_for_my_account'),
    
]