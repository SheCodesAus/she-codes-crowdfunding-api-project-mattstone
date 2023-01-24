from rest_framework import permissions

class isOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permissions(self, request, view, obj):
      if request.method in permissions.SAFE_METHOD:
          return True
    
      return obj.owner == request.user