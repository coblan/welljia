from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserInfo
from helpers.func.random_str import get_str


#注意，该事件处理函数，展示没有使用
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        invite_code = get_str(length= 6).lower()
        UserInfo.objects.create(user=instance, invite_code = invite_code)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
    #instance.profile.save()