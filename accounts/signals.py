from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from .utils import unique_public_id_generator , unique_slug_generator 








@receiver(post_save , sender=CustomUser)
def user_profile_signal(sender, instance , created , **kwarg):
    if created:
        instance.public_id = unique_public_id_generator(instance)
        instance.save()




