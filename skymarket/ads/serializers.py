from rest_framework import serializers
from ads.models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""

    class Meta:
        model = Comment
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Ad."""

    class Meta:
        model = Ad
        fields = ["id", "title", "description", "price", "image"]


class AdDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Ad с полными деталями."""

    class Meta:
        model = Ad
        fields = "__all__"
