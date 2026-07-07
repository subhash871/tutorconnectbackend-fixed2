from django.db.models import Q
from apps.users.models import User


class UserSelector:
    """
    Selector layer for user queries.
    """
    
    @staticmethod
    def get_user_by_id(user_id):
        """Get user by ID."""
        return User.objects.filter(id=user_id).first()
    
    @staticmethod
    def get_user_by_email(email):
        """Get user by email."""
        return User.objects.filter(email__iexact=email).first()
    
    @staticmethod
    def get_user_by_username(username):
        """Get user by username."""
        return User.objects.filter(username__iexact=username).first()
    
    @staticmethod
    def get_verified_teachers():
        """Get all verified and approved teachers."""
        return User.objects.filter(
            role='teacher',
            is_verified=True,
            is_teacher_approved=True,
            is_active=True
        )
    
    @staticmethod
    def get_active_students():
        """Get all active students."""
        return User.objects.filter(role='student', is_active=True)
    
    @staticmethod
    def search_users(query):
        """Search users by name, email, or username."""
        return User.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(username__icontains=query)
        )
    
    @staticmethod
    def get_pending_teacher_approvals():
        """Get teachers pending admin approval."""
        return User.objects.filter(
            role='teacher',
            is_teacher_approved=False,
            is_active=True
        )