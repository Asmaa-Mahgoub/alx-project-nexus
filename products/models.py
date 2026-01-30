from django.db import models
from components.models import Components

# Create your models here.
class Product(models.Model):
    class ProductStatus(models.TextChoices):
        DRAFT= 'Dr', 'Draft'
        TRIAL= 'Tr', 'Trial'
        APPROVED='App', 'Approved'
        ARCHIVED= 'Arch', 'Archived' 
    #product_id= models.AutoField(primary_key= True)......Automatically created by Django
    product_code= models.CharField(max_length=100, unique=True)
    name= models.CharField(max_length=100)
    #batch= models.CharField(max_length=100)........ERD currently models raw-material traceability, not finished-goods batching
    status= models.CharField(max_length=10, choices= ProductStatus.choices, default=ProductStatus.DRAFT)
    created_at= models.DateTimeField(auto_now_add= True)

class ProductVersion(models.Model):
    class VersionStatus(models.TextChoices):
        DRAFT = 'DRAFT', 'Draft'
        TRIAL = 'TRIAL', 'Trial'
        APPROVED = 'APPROVED', 'Approved'
        OBSOLETE = 'OBSOLETE', 'Obsolete'
    version_no= models.CharField(max_length=10)
    product= models.ForeignKey(Product, on_delete=models.CASCADE, related_name= 'versions')
    status= models.CharField(max_length=25, choices=VersionStatus.choices, default=VersionStatus.DRAFT)
    created_at= models.DateTimeField(auto_now_add= True)

class ProductComponent(models.Model):    #Which components are used in THIS version, and how much? ProductComponent describes usage, not identity
    component= models.ForeignKey(Components, on_delete=models.PROTECT, related_name="product_usages")
    quantity_used= models.DecimalField(max_digits=10, decimal_places= 3)
    product_version = models.ForeignKey(ProductVersion, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('component', 'product_version')
