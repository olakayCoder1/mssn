from django.shortcuts import render
from post.models import Post
from client.models import Program
# Create your views here.





def login_view(request):
    return render(request , 'accounts/login.html')


def register(request):
    return render(request , 'accounts/register.html')


def forget_password(request):
    return render(request , 'accounts/forget-password.html')


def page_not_found(request, exception ):
    return render(request , 'page_not_found.html')







def about(request):
    return render(request , 'help/faq.html')