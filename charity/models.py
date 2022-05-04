from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.

class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class volunteer_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password= models.CharField(max_length=50,null=True)
    Home_Address = models.CharField(max_length=50,null=True)
    City_Address = models.CharField(max_length=50,null=True)
    Street_Address = models.CharField(max_length=50,null=True)
    image=models.ImageField('images/',null=True)
    proof= models.FileField('file/',null=True)
    qualification = models.CharField(max_length=50)
    phone = models.CharField(max_length=50,null=True)
    location = models.CharField(max_length=50)
    status= models.CharField(max_length=100,null=True)

class Benefactorr(models.Model):


    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    password= models.CharField(max_length=50,null=True)
    location = models.CharField(max_length=50)
    Home_Address = models.CharField(max_length=50,null=True)
    City_Address = models.CharField(max_length=50,null=True)
    Street_Address = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    type1 = models.CharField(max_length=50)
    status= models.CharField(max_length=100,default=0)

class Benefactor_Report(models.Model):
    benefactor_id = models.ForeignKey(Benefactorr, on_delete=models.CASCADE,null=True)
    location = models.CharField(max_length=50,null=True)

    reply = models.CharField(max_length=50)
    status= models.CharField(max_length=100,default=0)

class Beneficiary(models.Model):


    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    location = models.CharField(max_length=50)
    password= models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    home_Address = models.CharField(max_length=50,null=True)
    city_Address = models.CharField(max_length=50,null=True)
    street_Address = models.CharField(max_length=50,null=True)
    type1 = models.CharField(max_length=50)
    status= models.CharField(max_length=100,default=0)

class Beneficiary_Report(models.Model):
    beneficiary_id = models.ForeignKey(Beneficiary, on_delete=models.CASCADE,null=True)
    location = models.CharField(max_length=50,null=True)

    reply = models.CharField(max_length=50)
    status= models.CharField(max_length=100,default=0)


class Location(models.Model):
    location= models.CharField(max_length=50)
    status  = models.CharField(max_length=50,default=1)



class Request_Need(models.Model):
    location =models.CharField(max_length=50,null=True)
    benfi_id =models.ForeignKey(Beneficiary, on_delete=models.CASCADE,null=True)
    members = models.CharField(max_length=50,null=True)
    product_need =models.CharField(max_length=300,null=True)
    status= models.CharField(max_length=100,default=0)
    status1= models.CharField(max_length=100,default=0)
    volunteer=models.ForeignKey(volunteer_reg, on_delete=models.CASCADE,null=True)
    need_status=models.CharField(max_length=100,default='apply')



class product_add(models.Model):
    volunteer=models.ForeignKey(volunteer_reg, on_delete=models.CASCADE,null=True)
    benefactor =models.ForeignKey(Benefactorr, on_delete=models.CASCADE,null=True)
    location =models.CharField(max_length=300,null=True)
    products =models.CharField(max_length=300,null=True)
    expiry_date = models.DateField(max_length=50,null=True)
    collected_date = models.DateField(max_length=50,null=True)
    # Quantity = models.IntegerField(null=True)
    members =models.IntegerField(null=True)
    status= models.CharField(max_length=100,default=0)
    status1= models.CharField(max_length=100,default=0)

class feedback(models.Model):
    feedback=models.CharField(max_length=300,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)





