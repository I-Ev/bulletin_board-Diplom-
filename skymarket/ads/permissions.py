from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    """Права доступа для админа"""
    def has_permission(self, request, view):
        """Проверка роли Модератор"""
        if not request.user.is_admin:
                return False
        return True


class IsOwner(BasePermission):
    """Права доступа для пользователя"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
