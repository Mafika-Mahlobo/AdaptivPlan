"""
Custom permission for resource ownership.
"""

from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Returns True if current user is an owner of a resource.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user