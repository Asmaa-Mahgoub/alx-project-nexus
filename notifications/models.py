from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    class NotificationType(models.TextChoices):
        LOW_STOCK= 'LWSTK','Low Stock'
        EXPIRY= 'EXPIR','Expiry'
        APROVAL= 'APROV','Aproval'
    user= models.ForeignKey(User, on_delete= models.CASCADE, related_name="notifications")
    type= models.CharField(max_length=10, choices=NotificationType.choices)
    message= models.CharField(max_length=300)
    is_read= models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return f"{self.get_type_display()} → {self.user.username}"