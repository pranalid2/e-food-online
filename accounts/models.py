from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.models import Permission

# Create your models here.
@receiver(post_save, sender=User)
def user_per(sender, instance, created, **kwargs):
    if created:
        permission_1 = Permission.objects.get(name='Can add item')
        permission_2 = Permission.objects.get(name='Can change item')
        permission_3 = Permission.objects.get(name='Can delete item')
        permission_4 = Permission.objects.get(name='Can view item')
        instance.user_permissions.add(permission_1)
        instance.user_permissions.add(permission_2)
        instance.user_permissions.add(permission_3)
        instance.user_permissions.add(permission_4)
        instance.is_staff = True
        instance.save()




