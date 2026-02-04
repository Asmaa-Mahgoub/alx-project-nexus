from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import TrialRequest, Decision
from .serializers import TrialRequestSerializer, DecisionSerializer
from .permissions import IsRDManager

# Create your views here.
class TrialRequestViewSet(viewsets.ModelViewSet):
    queryset= TrialRequest.objects.all()
    serializer_class= TrialRequestSerializer
    
    """ @action(
       detail=True,
        methods=['post'],
        permission_classes=[IsRDManager]
    )
    def approve(self, request, pk=None):
        trial = self.get_object()
        trial.status = 'APPROVED'
        trial.approved_by = request.user
        trial.save()
        return Response({"status": "approved"})

    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsRDManager]
    )
    def decline(self, request, pk=None):
        trial = self.get_object()
        trial.status = 'Rejected'
        trial.approved_by = request.user
        trial.save()
        return Response({"status": "rejected"})
    
    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsRDManager]
    )
    def pend(self, request, pk=None):
        trial = self.get_object()
        trial.status = 'Pended'
        trial.approved_by = request.user
        trial.save()
        return Response({"status": "pended"})
 """
class DecisionViewSet(viewsets.ModelViewSet):
    queryset= Decision.objects.all()
    serializer_class= DecisionSerializer
    permission_classes = [IsRDManager]

    @action(detail=False, methods=['post'])
    def decide(self, request):
        """
        RD Manager approves/rejects a trial.Inside the decide function, we pull three pieces of information sent by the frontend
        """
        trial_id = request.data.get('trial_id')
        decision_value = request.data.get('decision')
        comment = request.data.get('comment', '') #.get('comment', ''): The '' is a "fallback." If the manager leaves the comment box empty, the code won't crash; it will just save an empty string.


        trial = TrialRequest.objects.get(id=trial_id)

        decision, created = Decision.objects.update_or_create(
            trial=trial,
            defaults={
                'decided_by': request.user,
                'decision': decision_value,
                'comment': comment
            }
        )     #decision, created: This method returns two things: the object itself (decision) and a true/false value (created) telling you if it was a brand new record.

        return Response({
            "trial": trial.id,
            "decision": decision.get_decision_display()
        })
""" Summary of how this works in "Real Life":
An RD Manager opens a trial request.
They type a comment and click "Approve".
The frontend sends the trial_id, the decision, and the comment to the /decide/ endpoint.
The backend either creates a new Decision record or updates an old one if they had already voted.
The system now has a permanent record of who approved it and why """