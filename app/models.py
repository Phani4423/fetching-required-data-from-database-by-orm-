from typing import Any
from django.db import models

# Create your models here.
class Dept(models.Model):
    dnum = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=100)
    dloc= models.CharField(max_length=100)
    def __str__(self):
        return self.dname + str(self.dnum)
class Emp(models.Model):
    enum = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    hirehate = models.DateField(auto_now_add=True)
    sal = models.DecimalField(max_digits=10,decimal_places=2)
    comm = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    dnum = models.ForeignKey(Dept,on_delete=models.CASCADE)
    mgr = models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    
