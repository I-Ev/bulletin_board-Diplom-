from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsStaff(BasePermission):
    """Права доступа для админа"""
    def has_permission(self, request, view):
        """Проверка роли Модератор"""
        if not request.user.role == UserRoles.ADMIN:
                return False
        return True


class IsOwner(BasePermission):
    """Права доступа для пользователя"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
