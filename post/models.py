from django.db import models
from accounts.models import CustomUser 
# Create your models here.




def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class Post(models.Model):
    public_id = models.CharField(max_length=1000 , null=True , blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_to ,  null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






