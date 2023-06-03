from django.db import models

# Create your models here.

class Tutorial(models.Model):
    title = models.CharField(max_length=70,blank=False,default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=True)



class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    firm_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=False)

    def __str__(self):
        return self.username
