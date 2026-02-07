from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Decision, TrialRequest
from notifications.tasks import send_notification
from notifications.models import Notification

@receiver(post_save, sender=TrialRequest)
def notify_decision_maker_on_trial_request(sender, instance, created, **kwargs):
    if created:
        send_notification.delay(
            recipient_id=instance.decision_maker.id,
            notification_type=Notification.NotificationType.TRIAL_REQUEST,
            message=(
                f"New trial request submitted for {instance.version} "
                f"by {instance.requested_by}."
            )
        )


@receiver(pre_save, sender=Decision)
def cache_old_decision(sender, instance, **kwargs):
    if instance.pk:
        old = Decision.objects.get(pk=instance.pk)
        instance._old_decision = old.decision
    else:
        instance._old_decision = None


@receiver(post_save, sender=Decision)
def notify_trial_decision(sender, instance, created, **kwargs):
    decision_changed = (
        not created and instance._old_decision != instance.decision
    )

    if created or decision_changed:
        send_notification.delay(
            recipient_id=instance.trial.requested_by.id,
            notification_type=Notification.NotificationType.TRIAL_DECISION,
            message=(
                f"Your trial request for {instance.trial.version} "
                f"is now {instance.get_decision_display()}."
            )
        )

        

""" 
@receiver(post_save, sender=Decision)
def notify_trial_decision(sender, instance, created, **kwargs):
    if not created:
        return

    Notification.objects.create(
        recipient=instance.trial.requested_by,
        notification_type=Notification.NotificationType.TRIAL_DECISION,
        message=(
            f"Your trial request for {instance.trial.version} "
            f"was {instance.get_decision_display()}."
        )
    )

@receiver(post_save, sender=OrderItemChangeLog)
def notify_quantity_increase(sender, instance, created, **kwargs):
    if not created:
        return

    if instance.new_quantity > instance.old_quantity:
        Notification.objects.create(
            group='SUPPLY_CHAIN',
            notification_type=Notification.NotificationType.QUANTITY_APPROVAL,
            message=(
                f"Quantity increase requires approval "
                f"(Order Item ID: {instance.order_item.id})"
            )
        )
 """