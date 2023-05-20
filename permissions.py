from rest_framework.permissions import BasePermission, IsAdminUser
from rest_framework.exceptions import PermissionDenied

    
class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT', 'DELETE', 'PATCH']:
            if request.user.groups.filter(name='Manager').exists() or request.user.is_superuser:
                return True
            else:
                raise PermissionDenied("Access denied. You are not authorized to perform this action 2222")
        return True
         

class ManagerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET','POST', 'PUT', 'DELETE', 'PATCH']:
            if request.user.groups.filter(name='Manager').exists() or request.user.is_superuser:
                return True
            else:
                raise PermissionDenied("Access denied. You are not authorized to perform this action 111")
        return True