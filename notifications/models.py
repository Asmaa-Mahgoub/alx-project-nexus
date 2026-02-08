from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model):

    class NotificationType(models.TextChoices):
        TRIAL_DECISION = 'TRIAL', 'Trial Decision'
        TRIAL_REQUEST = 'TRIAL_REQUEST', 'New Trial Request'      # 🔴 ADDED
        ORDER_QTY_CHANGE = 'ORDER_QTY_CHANGE', 'Order Qty Change' 

    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications',
        null=True,
        blank=True
    )

    group = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )  # e.g. SUPPLY_CHAIN, RD_MANAGER

    notification_type = models.CharField(
        max_length=20,
        choices=NotificationType.choices,default=NotificationType.TRIAL_DECISION,
    )

    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
     #  ADDED: Generic reference fields (future-proof, optional)
    related_object_id = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    related_object_type = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.message


""" related_object_id & related_object_type (🔴 ADDED)

These solve a real frontend problem:
Frontend can:

Click notification
Redirect user to:
Trial detail page
Order detail page

Example stored values:

related_object_type = "trial_request"
related_object_id = 12

🚀 This avoids hardcoding logic in frontend later. """