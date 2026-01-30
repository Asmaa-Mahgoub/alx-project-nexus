from django.db import models
from components.models import Component

# Create your models here.
class Supplier(models.Model):
    class PaymentMethod(models.TextChoices):
        CASH_ON_DELIVERY= 'COD', 'Cash'
        VISA='CC', 'CreditCard'
        INSTALLEMENT= 'VALU', 'Installement'

    class ShipmentMethods(models.TextChoices):
        AIR_FREIGHT= 'AIR', 'Air Freight'
        SEA_FREIGHT= 'SEA', 'Sea Freight'
        EXPRESS= 'XPRESS', 'Express'

    supplier_name= models.CharField(max_length= 100)
    email= models.EmailField(unique= True)
    phone= models.CharField(max_length=11, unique= True)
    address= models.CharField(max_length=100)
    shipment_method= models.CharField(max_length=12, choices=ShipmentMethods.choices, default=ShipmentMethods.EXPRESS)
    payment_method=models.CharField(max_length=12, choices= PaymentMethod.choices, default=PaymentMethod.VISA)

    def __str__(self):
        return f"{self.supplier_name} | email: {self.email}"
    
class SupplierComponent(models.Model):
    minimum_order_quantity= models.DecimalField(max_digits=7, decimal_places=3)
    expected_delivery_period= models.PositiveIntegerField()
    unit_price= models.DecimalField(max_digits=15, decimal_places=3)
    supplier=models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='supplier_components')   #Show me all supplier–component commercial agreements
    component= models.ForeignKey(Component, on_delete=models.PROTECT, related_name='supplier_components') #wShow me all supplier–component commercial agreements
    #A supplier should have only one active commercial agreement per component
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['supplier', 'component'],
                name='unique_supplier_component'
            )
        ]

    def __str__(self):
        return f"{self.supplier} has minimum order quantity : {self.minimum_order_quantity} for {self.component}"