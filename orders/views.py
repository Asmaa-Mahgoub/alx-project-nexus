from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from rest_framework import viewsets, status
from .models import Order, OrderItem, OrderItemChangeLog
from .serializers import OrderSerializer, OrderItemSerializer, OrderQuantityUpdateSerializer, OrderItemChangeLogSerializer
from rest_framework.decorators import action
from .permissions import IsSupplyChain

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    queryset= Order.objects.all()
    serializer_class= OrderSerializer

    @action(detail=True, methods=['post'], serializer_class=OrderQuantityUpdateSerializer, permission_classes=[IsSupplyChain])

    def adjust_quantity(self,request, pk=None):
        #serializer= OrderQuantityUpdateSerializer(data=request.data) #Serializers validate request payload, not tables
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception= True)

        order=self.get_object()   #Instead of you writing Order.objects.get(id=12).
        item = OrderItem.objects.get(
            id=serializer.validated_data['order_item_id'],
            order=order
        )
        #order_item_id, This is the ID of a specific OrderItem (like a specific component or product) that exists inside that order.
        new_qty = serializer.validated_data['new_quantity']
        old_qty = item.ordered_quantity
        reason = serializer.validated_data.get('reason', '')


        # BUSINESS LOGIC
       # Approval required ONLY when increasing quantity
        if new_qty > old_qty:
            OrderItemChangeLog.objects.create(
                order_item=item,
                changed_by=request.user,
                old_quantity=old_qty,
                new_quantity=new_qty,
                reason=reason,
                status=OrderItemChangeLog.ApprovalStatus.PENDING   #We mark this log as PENDING. It will sit in this state until a manager later calls an approve function (
            )
            return Response(
                {"status": "Approval required"},
                status=status.HTTP_202_ACCEPTED
            )
 
        # Direct decrease. This code runs only if the business rules (like increasing quantity) were not met—meaning the change is considered safe enough to happen instantly.
        item.ordered_quantity = new_qty
        item.save()

        OrderItemChangeLog.objects.create(
            order_item=item,
            changed_by=request.user,
            old_quantity=old_qty,
            new_quantity=new_qty,
            reason=reason,
            status=OrderItemChangeLog.ApprovalStatus.APPROVED
        )

        return Response({"status": "quantity updated"})
    
    # URL becomes POST /orders/{order_id}/adjust-quantity/ """


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset= OrderItem.objects.all()
    serializer_class= OrderItemSerializer

class OrderItemChangeLogViewSet(viewsets.ModelViewSet):
    queryset= OrderItemChangeLog.objects.all()
    serializer_class= OrderItemChangeLogSerializer
    filterset_fields = ['order_item', 'status']  #This enables query filtering via URL.

"""     Without it:
GET /change-logs/
→ returns EVERYTHING

With it:
GET /change-logs/?order_item=5
GET /change-logs/?status=PENDING
GET /change-logs/?order_item=5&status=PENDING


This is critical for:

Managers seeing pending approvals

Auditors reviewing history
 """
   
   
""" Quantity decrease
POST /orders/{id}/adjust_quantity/
→ updated immediately
→ logged as APPROVED

Quantity increase
POST /orders/{id}/adjust_quantity/
→ saved as PENDING
→ no quantity change yet

Audit trail
GET /change-logs/?order_item=5 """
        
       
        
