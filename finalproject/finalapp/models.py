from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Marvel(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to="marvel")
    year=models.DateField()
    cast=models.TextField()
    category=models.CharField(max_length=250)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    url=models.URLField()
    # review=models.TextField(null=True,blank=True)

class Dccomics(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to="dccomics")
    year=models.DateField()
    cast=models.TextField()
    category=models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()

    # review = models.TextField(null=True,blank=True)


class Monster(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to="monster")
    year=models.DateField()
    cast=models.TextField()
    category=models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    # review = models.TextField(null=True,blank=True)

# class user_details(models.Model):
#     first_name=models.CharField(max_length=100)
#     last_name=models.CharField(max_length=100)
#     email=models.CharField(max_length=100)
#     password=models.CharField(max_length=100)

class Review(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(Marvel,on_delete=models.CASCADE)
    review=models.CharField(max_length=100)
    rating=models.TextField()

class DReview(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(Dccomics,on_delete=models.CASCADE)
    review=models.CharField(max_length=100)
    rating=models.TextField()

class MReview(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(Monster,on_delete=models.CASCADE)
    review=models.CharField(max_length=100)
    rating=models.TextField()



