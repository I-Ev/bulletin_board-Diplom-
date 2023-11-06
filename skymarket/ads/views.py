from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.paginations import AdPagination
from ads.permissions import IsOwner, IsStaff
from ads.serializers import CommentSerializer, AdSerializer, AdDetailSerializer
from users.models import User


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    """
    ViewSet для объявлений.
    """
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    def get_serializer_class(self):
        """
        Определяет класс сериализатора в зависимости от действия.
        """
        if self.action in ['list', 'personal_list']:
            return AdSerializer
        return AdDetailSerializer

    # def get_permissions(self):
    #     """
    #     Определяет права доступа в зависимости от выполняемого действия.
    #     """
    #     if self.action == 'retrieve':
    #         permission_classes = [IsAuthenticated]
    #     elif self.action == 'create':
    #         permission_classes = [IsAuthenticated]
    #     elif self.action in ['destroy', 'update', 'partial_update']:
    #         permission_classes = [IsAuthenticated, IsOwner | IsStaff]
    #     else:
    #         permission_classes = [AllowAny]
    #     return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """
        Создает новое объявление и устанавливает автора.
        """
        ad = serializer.save()
        ad.author = get_object_or_404(User, id=self.request.user.id)
        ad.save()

    @action(methods=['get'], detail=False, url_path='me')
    def personal_list(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author=request.user)
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet для комментариев к объявлениям.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # def get_permissions(self):
    #     """
    #     Определяет права доступа в зависимости от выполняемого действия.
    #     """
    #     if self.action == 'retrieve':
    #         permission_classes = [IsStaff]
    #     elif self.action == 'create':
    #         permission_classes = [IsAuthenticated]
    #     elif self.action in ['destroy', 'update', 'partial_update']:
    #         permission_classes = [IsAuthenticated, IsOwner | IsStaff]
    #     else:
    #         permission_classes = [AllowAny]
    #     return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """
        Создает новый комментарий и устанавливает автора.
        """
        comment = serializer.save()
        comment.author = get_object_or_404(User, id=self.request.user.id)
        comment.save()

    def get_queryset(self):
        return self.queryset.filter(ad=self.kwargs['ad_pk']).select_related("author")

class UserAdsListView(ListAPIView):
    """
    Представление для списка объявлений пользователя.
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    # permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """
        Фильтрует список объявлений по автору (пользователю).
        """
        self.queryset = self.queryset.filter(author=request.user)
        return super().list(request, *args, **kwargs)