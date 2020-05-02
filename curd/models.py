from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Employee(models.Model):

    empName = models.CharField(max_length=50, null=True, blank=True)
    empMobile = models.CharField(max_length=50, null=True, blank=True)
    empEmail = models.CharField(max_length=50, null=True, blank=True)
    postion = models.CharField(max_length=50, null=True, blank=True)
    empCode = models.CharField(max_length=50, null=True, blank=True)
  

    def __str__(self):
        return self.Employee



#  empId:number;
#     empName:string;
#     empMobile:string;
#     empEmail:string;
#     postion:string;
#     empCode:string