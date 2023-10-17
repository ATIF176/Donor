from django.db import models

# Create your models here.
class DonorRegister(models.Model):
    fname = models.CharField(max_length=50, blank=False, null=False)
    lname = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)
    phone = models.CharField(max_length=11, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    bgroup = models.CharField(max_length=3, blank=False, null=False)
    donorid = models.CharField(max_length=10, unique=True)    
    more = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.donorid
    
# class BloodRequest(models.Model):
#     ldonation = models.DateField(null=True, blank=True)