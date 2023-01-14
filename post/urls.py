from django.urls import path
from . import views


urlpatterns = [  
    path('post/<str:public_id>', views.post_detail ,  name='post_detail' ),  
]