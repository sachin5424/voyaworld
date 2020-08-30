from django.db import models
from  django.urls import reverse


# Create your models here.

class PackagaesCountry(models.Model):
    Country = models.CharField(max_length=100)

    def __str__(self):
        return self.Country


class PackagaesState(models.Model):
    State = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    Country = models.ForeignKey(PackagaesCountry, on_delete=models.CASCADE)

    def __str__(self):
        return "%s (%s)" %(self.State,self.Country)


class PackagesAdd(models.Model):
    State = models.ForeignKey(PackagaesState, on_delete=models.CASCADE, null=True)
    package_place = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    package_Day = models.IntegerField()
    package_Night = models.IntegerField()
    package_price = models.IntegerField()
    dis = models.TextField()
    def __str__(self):
        return "%s (%s)" % (self.package_place, self.State)

    def get_absolute_url(self):
        return reverse("travel:packagesDetail",kwargs={"slug": self.slug})


class ContactAdd(models.Model):
    contact_name = models.CharField(max_length=100 )
    contact_email = models.EmailField()
    contact_msg = models.TextField()
    def __str__(self):
        return self.contact_name


class tranding_package(models.Model):
    tranding_pack = models.ForeignKey(PackagesAdd,on_delete=models.CASCADE)
    def __str__(self):
        return "%s "%(self.tranding_pack)

class special_package(models.Model):
    special_pack = models.ForeignKey(PackagesAdd, on_delete=models.CASCADE)
    def __str__(self):
        return "%s " % (self.special_pack)

class Devloper_info(models.Model):
    D_image = models.ImageField(null=True, )
    D_name = models.CharField(max_length=100)
    D_info = models.TextField()

