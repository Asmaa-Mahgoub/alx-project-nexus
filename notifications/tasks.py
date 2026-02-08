from celery import shared_task # type: ignore
from django.contrib.auth.models import User
from .models import Notification


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=5,
    retry_kwargs={'max_retries': 3}
)
def send_notification(
    self,
    message,
    recipient_id=None,
    group=None,
    notification_type=None,
):
    """
    Generic async notification task
    - Supports user-based notifications
    - Supports group-based notifications
    """

    recipient = None

    if recipient_id:
        recipient = User.objects.get(id=recipient_id)

    Notification.objects.create(
        recipient=recipient,
        group=group,
        notification_type=notification_type,
        message=message,
    )
