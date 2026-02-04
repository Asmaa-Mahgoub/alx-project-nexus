from rest_framework.permissions import BasePermission

class IsRDManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='RD_MANAGER').exists()











