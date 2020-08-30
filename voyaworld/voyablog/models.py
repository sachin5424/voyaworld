from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db.models.deletion import CASCADE


class Category(models.Model):
    Blog_title = models.CharField(max_length=100)

    def __str__(self):
        return self.Blog_title


class Blog(models.Model):
    Blog_title = models.CharField(max_length=100, null=True, )
    img = models.ImageField(upload_to='media')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    dec = models.TextField(null=True)
    def __str__(self):
        return "%s" % self.Blog_title



class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    name = models.CharField(max_length=50, )
    Profile_image = models.ImageField(upload_to='media/profile')

    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=15, null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    def __str__(self):
        return "%s" % self.user





