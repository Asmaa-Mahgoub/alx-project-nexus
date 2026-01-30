from django.db import models
from suppliers.models import Suppliers

# Create your models here.
class Component(models.Model):  #Representing component identity, not stock, not supplier, not price
    component_name= models.CharField(max_length=100)

    def __str__(self):
        return self.component_name

class ComponentBatch(models.Model):
    class BatchStatus(models.TextChoices):
        AVAILABLE = 'AVL', 'Available'
        EXPIRED = 'EXP', 'Expired'
        CONSUMED = 'CON', 'Consumed'
        QUARANTINED = 'QTN', 'Quarantined'
    component=models.ForeignKey(Component,on_delete= models.PROTECT, related_name='batches')
    quantity= models.DecimalField(max_digits=10, decimal_places=3)
    batch_no= models.CharField(unique=True) 
    expiry_date= models. DateField()
    received_date= models.DateField() #business reality
    created_at = models.DateTimeField(auto_now_add=True) #system metadata
    supplier= models.ForeignKey(Suppliers, on_delete= models.PROTECT, related_name='component_batches')
    status= models.CharField(max_length=25, choices=BatchStatus.choices, default=BatchStatus.AVAILABLE)

    #Batch no. is supplier specific. A batch number must be unique PER SUPPLIER, not globally. 
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['supplier', 'batch_no'],
                name='unique_batch_per_supplier'
            )
        ]

    def __str__(self):
        return f"{self.component} | Batch {self.batch_no}"

"""  related_name

“How do I want to access CHILDREN from the PARENT?”

UniqueConstraint

“What combination of fields must never repeat in real life?”"""