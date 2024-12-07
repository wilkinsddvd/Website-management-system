from django.db import models
from django.contrib.auth.models import User

class Website(models.Model):
    web_id = models.AutoField(primary_key=True)
    url = models.URLField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.url

# class WebsiteManage(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     website = models.ForeignKey(Website, on_delete=models.CASCADE)
#     url = models.URLField()
#
#     class Meta:
#         unique_together = ('user', 'website')
#
#     def __str__(self):
#         return f"{self.user.username} - {self.website.url}"

''' 新增内容'''
# from django.db import models
#
# class Website(models.Model):
#     url = models.URLField(unique=True)
#     description = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)