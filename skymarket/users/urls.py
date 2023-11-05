from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig

# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этого рекомендуется использовать SimpleRouter

app_name = UsersConfig.name

users_router = SimpleRouter()
users_router.register("", UserViewSet, basename="users")

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path("", include(users_router.urls)),
]

# [#####  DJOSER URLs  ######]:
# GET "users/" — список профилей пользователей
# POST "users/" — регистрация пользователя
# GET, PATCH, DELETE "users/{id}" — в соответствии с REST и необходимыми permissions (для администратора)
# GET PATCH "users/me" — получение и изменение своего профиля
# POST "users/set_password" — ручка для изменения пароля
# POST "users/reset_password" — ручка для направления ссылки сброса пароля на email*
# POST "users/reset_password_confirm" — ручка для сброса своего пароля*
#  https://djoser.readthedocs.io/en/latest/base_endpoints.html