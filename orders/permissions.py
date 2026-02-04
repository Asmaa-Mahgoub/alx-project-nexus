from rest_framework.permissions import BasePermission

class IsSupplyChain(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='SUPPLY_CHAIN').exists()

