from django.shortcuts import render

# Create your views here.





def login_view(request):
    return render(request , 'home.html')



def feedback(request):
    return render(request , 'help/feedback.html')

def faq(request):
    return render(request , 'help/faq.html')


def about(request):
    return render(request , 'help/faq.html')