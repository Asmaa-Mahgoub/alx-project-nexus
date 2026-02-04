from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model):

    class NotificationType(models.TextChoices):
        TRIAL_DECISION = 'TRIAL', 'Trial Decision'
        QUANTITY_APPROVAL = 'QTY', 'Quantity Approval'

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
        max_length=10,
        choices=NotificationType.choices,default=NotificationType.TRIAL_DECISION,
    )

    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


