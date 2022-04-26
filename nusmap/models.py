from django.db import models
from datetime import datetime


# Create your models here.

# def get_file_path(request, filname):

# user models


class Category(models.Model):
    slug=models.CharField( max_length=150, null=False, blank=False)
    name=models.CharField( max_length=150, null=False, blank=False)
    imge=models.ImageField( upload_to='static\store', null=True, blank=True)
    description=models.TextField(max_length=700, null=False, blank=False)
    status=models.BooleanField(default=False, help_text="0-defult , 1-Hidden")
    trending=models.BooleanField(default=False, help_text="0-defult , 1-trending")
    meta_title=models.CharField( max_length=150, null=False, blank=False)
    meta_keywords=models.CharField( max_length=150, null=False, blank=False)
    meta_description=models.CharField( max_length=550, null=False, blank=False)
    created_at=models.DateField( auto_now_add=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    slug=models.CharField( max_length=150, null=False, blank=False)
    name=models.CharField( max_length=150, null=False, blank=False)
    product_imge=models.ImageField( upload_to='static\store', null=True, blank=True)
    small_description=models.CharField(max_length=250, null=False, blank=False)
    quantity=models.IntegerField(null=False, blank=False )
    original_price=models.FloatField(null=False, blank=False)
    selling_price=models.FloatField(null=False, blank=False)
    description=models.TextField(max_length=700, null=False, blank=False)
    status=models.BooleanField(default=False, help_text="0-defult , 1-Hidden")
    trending=models.BooleanField(default=False, help_text="0-defult , 1-trending")
    tag=models.CharField( max_length=150, null=False, blank=False)
    meta_title=models.CharField( max_length=150, null=False, blank=False)
    meta_keywords=models.CharField( max_length=150, null=False, blank=False)
    meta_description=models.CharField( max_length=550, null=False, blank=False)
    total_sales=models.IntegerField(default=1)
    created_at=models.DateField( auto_now_add=True)   
    def __str__(self):
        return self.name


    