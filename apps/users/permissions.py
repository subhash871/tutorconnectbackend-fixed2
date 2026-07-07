from rest_framework import permissions


class IsTeacherUser(permissions.BasePermission):
    """
    Permission to check if the user is a teacher.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'teacher'


class IsStudentUser(permissions.BasePermission):
    """
    Permission to check if the user is a student.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'


class IsVerifiedUser(permissions.BasePermission):
    """
    Permission to check if the user is verified.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_verified