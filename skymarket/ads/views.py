from django.shortcuts import get_object_or_404
from rest_framework import pagination, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.permissions import IsOwner, IsStaff
from ads.serializers import CommentSerializer, AdSerializer, AdDetailSerializer
from users.models import User


class AdPagination(pagination.PageNumberPagination):
    page_size = 4
    page_query_param = 'page'


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filterset_class = AdFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return AdSerializer
        return AdDetailSerializer

    # def get_permissions(self):
    #     """Права доступа"""
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
        ad = serializer.save()
        ad.author = get_object_or_404(User, id=self.request.user.id)
        ad.save()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # def get_permissions(self):
    #     """Права доступа"""
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
        comment = serializer.save()
        comment.author = get_object_or_404(User, id=self.request.user.id)
        comment.save()

class UserAdsListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    # permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(author=request.user)
        return super().list(request, *args, **kwargs)