from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
#from notifications.models import Notification
from .models import OrderItemChangeLog
from notifications.tasks import send_notification

""" @receiver(pre_save, sender=OrderItemChangeLog)
def cache_old_status(sender, instance, **kwargs):
    if instance.pk:
        old = OrderItemChangeLog.objects.get(pk=instance.pk)
        instance._old_status = old.status
    else:
        instance._old_status = None
@receiver(post_save, sender=OrderItemChangeLog)
def notify_quantity_change(sender, instance, created, **kwargs):

    #  New quantity increase request
    if created and instance.status == OrderItemChangeLog.ApprovalStatus.PENDING:
        Notification.objects.create(
            group="SUPPLY_CHAIN",
            message=(
                f"Quantity increase pending approval "
                f"(Order Item ID: {instance.order_item.id})"
            )
        )

    #  Approval or rejection happened later
    status_changed = (
        not created and instance._old_status != instance.status
    )

    if status_changed and instance.status in [
        OrderItemChangeLog.ApprovalStatus.APPROVED,
        OrderItemChangeLog.ApprovalStatus.REJECTED,
    ]:
        Notification.objects.create(
            recipient=instance.changed_by,
            message=(
                f"Your quantity change for Order Item "
                f"{instance.order_item.id} was {instance.status.lower()}."
            )
        )
 """

@receiver(pre_save, sender=OrderItemChangeLog)
def cache_old_status(sender, instance, **kwargs):
    if instance.pk:
        old = OrderItemChangeLog.objects.get(pk=instance.pk)
        instance._old_status = old.status
    else:
        instance._old_status = None


@receiver(post_save, sender=OrderItemChangeLog)
def notify_quantity_change(sender, instance, created, **kwargs):

    # New quantity increase request (PENDING)
    if created and instance.status == OrderItemChangeLog.ApprovalStatus.PENDING:
        send_notification.delay(
            message=(
                f"Quantity increase pending approval "
                f"(Order Item ID: {instance.order_item.id})"
            ),
            group="SUPPLY_CHAIN",
        )

    # Approval or rejection happened later
    status_changed = (
        not created and instance._old_status != instance.status
    )

    if status_changed and instance.status in [
        OrderItemChangeLog.ApprovalStatus.APPROVED,
        OrderItemChangeLog.ApprovalStatus.REJECTED,
    ]:
        send_notification.delay(
            message=(
                f"Your quantity change for Order Item "
                f"{instance.order_item.id} was {instance.status.lower()}."
            ),
            recipient_id=instance.changed_by_id,
        )