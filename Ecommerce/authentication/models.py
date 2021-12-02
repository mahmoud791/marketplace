from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from home.models import Product

# Create your models here.

class user(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    credits = models.IntegerField(default=0)
    



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.user.save()



