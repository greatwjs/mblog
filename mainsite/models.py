from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20,null=False)
    password=models.CharField(max_length=20,null=False)
    enabled=models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Yanzheng(models.Model):
    mobile=models.CharField(max_length=20,null=False)
    code=models.CharField(max_length=5)
    name=models.CharField(max_length=20,null=False)

    def __unicode__(self):
        return self.mobile

class Post(models.Model):
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    body=models.TextField()
    pub_date=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=('-pub_date',)

    def __unicode__(self):
        return self.title




