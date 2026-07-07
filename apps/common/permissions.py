from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow owners to edit their objects,
    while others can only read.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsTeacher(permissions.BasePermission):
    """
    Permission to allow only teachers to access the view.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'teacher'


class IsStudent(permissions.BasePermission):
    """
    Permission to allow only students to access the view.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'


class IsAdmin(permissions.BasePermission):
    """
    Permission to allow only admin users to access the view.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsVerifiedTeacher(permissions.BasePermission):
    """
    Permission to allow only verified teachers to access the view.
    """
    def has_permission(self, request, view):
        return (request.user.is_authenticated and 
                request.user.role == 'teacher' and 
                request.user.is_verified)


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Permission to allow owners or admin to access the view.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        return obj.user == request.user