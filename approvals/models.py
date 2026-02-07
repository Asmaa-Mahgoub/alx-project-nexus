from django.db import models
from django.contrib.auth.models import User
from products.models import ProductVersion

# Create your models here.
class TrialRequest(models.Model):
    requested_by= models.ForeignKey(User, on_delete=models.PROTECT, related_name='trial_requests')
    request_date= models.DateTimeField(auto_now_add=True)
    decision_maker = models.ForeignKey(User, on_delete=models.PROTECT, related_name='assigned_trials', default=None)
    justification= models.TextField()
    version= models.ForeignKey(ProductVersion, on_delete= models.PROTECT, related_name='trial_requests')
    
    def __str__(self):
        return f"Trial for {self.version} by {self.requested_by}"
    
class Decision(models.Model):
    class DecisionStatus(models.TextChoices):
        APPROVED= 'APP', 'Approved'
        REJECTED= 'REJ', 'Rejected'
        PENDING= 'PEND', 'Pended'

    decided_by= models.ForeignKey(User, on_delete= models.PROTECT, related_name='decisions')
    comment= models.TextField()
    decision_date= models.DateTimeField(auto_now_add=True)
    trial= models.OneToOneField(TrialRequest, on_delete=models.CASCADE, related_name='decision')
    decision= models.CharField(max_length=15, choices=DecisionStatus.choices)

    def __str__(self):
        return f"{self.get_decision_display()} by {self.decided_by}"
    
""" Trials happen on versions, not abstract products

One product can have:
Version 1 → Approved
Version 2 → Trial
Version 3 → Draft """