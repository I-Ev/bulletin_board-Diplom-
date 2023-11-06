from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from djoser import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import UserActivationView

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# TODO здесь необходимо подключить нужные нам urls к проекту


urlpatterns = [

                  path("api/admin/", admin.site.urls),
                  path("api/redoc-tasks/", include("redoc.urls")),

                  path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

                  path("api/users/", include("users.urls")),
                  path("api/ads/", include("ads.urls")),
                  path('api/token/', TokenObtainPairView.as_view()),
                  path('api/refresh/', TokenRefreshView.as_view()),

                  path('auth/users/activate/<str:uid>/<str:token>/', UserActivationView.as_view(), name='activation'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
