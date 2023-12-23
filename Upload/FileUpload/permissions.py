from rest_framework.permissions import BasePermission

class IsOps(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Operations').exists():
            return True