from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.home),
    path('post/olakay', views.post_detail ), 
]