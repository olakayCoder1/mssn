from django.shortcuts import render
from post.models import Post
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