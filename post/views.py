from django.shortcuts import render
from .models import Post
# Create your views here.




def post_detail(request , public_id ): 
    try:
        post = Post.objects.get(public_id=public_id)
    except:
        post = Post.objects.get(id=1)
        pass
    context = {
        'post' : post
    }
    return render(request , 'client/post/post-details.html' , context )

