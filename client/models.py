from django.db import models

# Create your models here.





class Faq(models.Model):
    public_id = models.CharField(max_length=1000 , null=True , blank=True)
    question = models.CharField(max_length=500)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)