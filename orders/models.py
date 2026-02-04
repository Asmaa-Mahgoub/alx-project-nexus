from django.db import models
from suppliers.models import Supplier
from components.models import Component
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    class OrderStatus(models.TextChoices):
        ISSUED= 'ISSUED', 'Issued'
        DELIVERED= 'DEL', 'Delivered'
        CANCELLED= 'CANCEL', 'Cancelled'
        REJECTED= 'REJ','Rejected'
        SHIPPED= 'SHIP', 'Shipped'
        ON_HOLD= 'HOLD', 'On Hold'
        COMPLETED= 'COMPLETED', 'Completed'
        PARTIALLY_RECEIVED = 'PARTIAL_REC', 'Partial Receive'
    order_no= models.CharField(max_length=30, unique=True)
    order_date= models.DateField(auto_now_add= True)
    status= models.CharField(max_length=12,choices=OrderStatus.choices, default= OrderStatus.ISSUED)
    supplier= models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='supplier_orders')
    expected_delivery_date = models.DateField(null=True, blank=True) 

    @property
    def total_price(self):
        return sum(
            item.ordered_quantity * item.unit_price
            for item in self.items.all()
    )

class OrderItem(models.Model):
    class OrderUnit(models.TextChoices):
        Kg= 'Kg','Kilogram'
        METER= 'Mt','Meters'
        LITRE= 'Lt','Litres'
    ordered_quantity= models.DecimalField(max_digits=10, decimal_places=3)
    ordered_unit= models.CharField(max_length=10,choices=OrderUnit.choices, default=OrderUnit.Kg)
    unit_price= models.DecimalField(max_digits=10, decimal_places=3)
    component= models.ForeignKey(Component,on_delete=models.PROTECT, related_name='component_items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['order', 'component'],
                name='unique_component_per_order'
            )
        ]


    def __str__(self):
        return f"{self.component} has a placed order of {self.ordered_quantity} {self.ordered_unit}"

class OrderItemChangeLog(models.Model):
    class ApprovalStatus(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        APPROVED = 'APPROVED', 'Approved'
        REJECTED = 'REJECTED', 'Rejected'
    order_item = models.ForeignKey(
        OrderItem,
        on_delete=models.CASCADE,
        related_name='change_logs'
    )
    changed_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    old_quantity = models.DecimalField(max_digits=10, decimal_places=3)
    new_quantity = models.DecimalField(max_digits=10, decimal_places=3)
    changed_at = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=200, blank=True)

    #What is the state of this CHANGE REQUEST?
    status = models.CharField(                        
        max_length=10,
        choices=ApprovalStatus.choices,
        default=ApprovalStatus.PENDING
    )
    approved_by = models.ForeignKey(               
        User,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='approved_changes'
    )

    def __str__(self):
        return f"{self.order_item} changed by {self.changed_by}"
