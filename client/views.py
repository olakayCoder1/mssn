from django.shortcuts import render
from post.models import Post
from .models import Program
# Create your views here.




def home(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request , 'home.html' , context )


def committee_list(request):
    return render(request , 'client/committee.html')


def post_detail(request):
    return render(request , 'client/post/post-details.html')



def feedback(request):
    return render(request , 'help/feedback.html')

def faq(request):
    return render(request , 'help/faq.html')
 

def programs(request):
    mssn_programs = Program.objects.all()
    context = {'programs' : mssn_programs }
    return render(request , 'client/program.html' , context)


def donation(request):
    return render(request , 'client/donation.html')
