from datetime import datetime
import uuid
from django.db import models
from django.core.exceptions import ValidationError
from  account.models import User


# Create your models here.

class Tribes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    tribe = models.CharField(max_length=150, default="")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.tribe
    
class Biodata(models.Model):
    Firstname = models.CharField(max_length=100, default="")
    Othernames = models.CharField(max_length=100, default="")
    Age = models.CharField(max_length=100, default="")
    weight = models.CharField(max_length=100, default="")
    sex = models.CharField(max_length=100, default="")
    height = models.CharField(max_length=100, default="")
    tribe = models.ForeignKey(Tribes, on_delete=models.SET_NULL, null=True) 
    Address = models.TextField(default="")
    Phone = models.CharField(max_length=100, default="")
    Emailaddress = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    day_of_week = models.CharField(max_length=10, blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.now()
        # Set the day_of_week based on created_at
        if self.created_at:
            self.day_of_week = self.created_at.strftime('%A')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Firstname
    
    
    

class ServiceCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    category = models.CharField(max_length=150, default="")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.category
    

class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True)
    service = models.CharField(max_length=100, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.service
    

class Drugcategory(models.Model):
    category = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.category


class Drugs(models.Model):
    category = models.ForeignKey(Drugcategory, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=100, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.category
    

    

class Providedservices(models.Model):
    patient = models.ForeignKey(Biodata, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.service)




    


            


    
