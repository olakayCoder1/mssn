from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.home),
    path('login', views.login_view , name='account_login'),  
    path('register', views.register , name='account_register'),    
    path('forget-password', views.forget_password , name='account_forget_password'),   
]