from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Faq , Program
# from .utils import unique_public_id_generator , unique_slug_generator 
from django.template.defaultfilters import slugify
from uuid import uuid4







@receiver(post_save , sender=Faq)
def user_profile_signal(sender, instance , created , **kwarg):
    if created:
        slug = slugify(instance.question)
        if Faq.objects.filter(public_id=slug).exists():
            ref = uuid4().hex
            instance.public_id = f'{slug}-{ref}'
        else:
            instance.public_id = slug
        instance.save()



@receiver(post_save , sender=Program)
def user_profile_signal(sender, instance , created , **kwarg):
    if created:
        slug = slugify(instance.title) 
        if Program.objects.filter(public_id=slug).exists():
            ref = uuid4().hex
            instance.public_id = f'{slug}-{ref}'
        else:
            instance.public_id = slug
        instance.save()
