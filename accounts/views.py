from django.shortcuts import render

# Create your views here.





def login_view(request):
    return render(request , 'accounts/login.html')


def register(request):
    return render(request , 'accounts/register.html')


def forget_password(request):
    return render(request , 'accounts/forget-password.html')


def home(request):
    return render(request , 'home.html')



def feedback(request):
    return render(request , 'help/feedback.html')

def faq(request):
    return render(request , 'help/faq.html')


def about(request):
    return render(request , 'help/faq.html')