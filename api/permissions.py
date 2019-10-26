from rest_framework.permissions import BasePermission, SAFE_METHODS

class isAuthor(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.user == obj.created_by:
            return True
        else:
            return False