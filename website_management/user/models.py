from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

''' 下面是新增内容,测试没过'''
# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)