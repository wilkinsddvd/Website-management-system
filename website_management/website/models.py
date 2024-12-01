from django.db import models

class Website(models.Model):
    web_id = models.AutoField(primary_key=True)
    url = models.URLField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.url

''' 新增内容'''
# from django.db import models
#
# class Website(models.Model):
#     url = models.URLField(unique=True)
#     description = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)