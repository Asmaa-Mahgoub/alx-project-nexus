from celery import shared_task # type: ignore
from django.contrib.auth.models import User
from .models import Notification


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=5, retry_kwargs={'max_retries': 3})
def send_notification(self, recipient_id, notification_type, message):
    """
    Generic async notification task
    """
    recipient = User.objects.get(id=recipient_id)

    Notification.objects.create(
        recipient=recipient,
        notification_type=notification_type,
        message=message
    )
