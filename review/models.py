from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    expire=models.DateTimeField(null=True,blank=True)
    publish=models.BooleanField(default=False)
    photo=models.ImageField(upload_to='review/userreviews/images',blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ExpertProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    number=models.PositiveIntegerField(blank=True,null=True)
    description=models.TextField(blank=True)
    category=models.CharField(max_length=100,blank=True,null=True)
    photo=models.ImageField(upload_to='review/images',blank=True)
    facebook=models.CharField(max_length=100,blank=True,null=True)
    Credits=models.PositiveIntegerField(blank=True,default=0)
    Admin=models.BooleanField(default=False)

    def __str__(self):
        if self.name==None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return self.name

class GenerateCode(models.Model):
    code=models.CharField(max_length=100)
    value=models.PositiveIntegerField(blank=True)
    def __str__(self):
        if self.code==None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return self.code