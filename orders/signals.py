from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notification
from .models import OrderItemChangeLog

@receiver(post_save, sender=OrderItemChangeLog)
def notify_quantity_increase(sender, instance, created, **kwargs):
    if created and instance.new_quantity > instance.old_quantity:
        Notification.objects.create(
            message="Quantity increase requires approval",
            group="SUPPLY_CHAIN"
        )


