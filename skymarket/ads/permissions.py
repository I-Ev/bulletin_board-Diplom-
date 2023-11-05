from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsStaff(BasePermission):
    """
        Права доступа для админа.
        Пользователи с ролью ADMIN имеют доступ.
        """
    def has_permission(self, request, view):

        if not request.user.role == UserRoles.ADMIN:
                return False
        return True


class IsOwner(BasePermission):
    """
    Права доступа для пользователя.
    Пользователь имеет доступ только к своим объектам.
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
