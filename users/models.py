from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.
class UserProfile(models.Model):        #This creates a separate table: user_profile linked to auth_user
    class Department(models.TextChoices):
        RD = 'RD', 'Research & Development'
        Director = 'DIR', 'Director'
        SUPPLY = 'SUP', 'Supply Chain'

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    department = models.CharField(max_length=25,choices=Department.choices)
   
    def __str__(self):
        return f"{self.user.username} - {self.department}"