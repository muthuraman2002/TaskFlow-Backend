from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    """
    Custom permission to only allow admin users to access certain views.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsClientUser(permissions.BasePermission):
    """
    Custom permission to only allow clients to manage their own projects and tasks.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsAdminOrClientUser(permissions.BasePermission):
    """
    Custom permission to allow admin users to manage all projects and tasks,
    while clients can only manage their own.
    """

    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.user.is_client)

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.owner == request.user