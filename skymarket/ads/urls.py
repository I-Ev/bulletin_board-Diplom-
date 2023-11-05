from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from ads.apps import SalesConfig
from ads.views import AdViewSet, CommentViewSet, UserAdsListView

app_name = SalesConfig.name

# ads_router = SimpleRouter()
# ads_router.register('', AdViewSet)
# comments_router = SimpleRouter()
# comments_router.register('', CommentViewSet)
#
# urlpatterns = [
#     path('me/', UserAdsListView.as_view(), name='user_ads'),
#     path('', include(ads_router.urls)),
#     path('<int:ad_pk>/comments/', include(comments_router.urls), name='comments'),
# ]


#
# ads_router = routers.SimpleRouter()
# ads_router.register('', AdViewSet, basename='ad')
# comments_router = routers.NestedSimpleRouter(ads_router, '', lookup='ad')
# comments_router.register(r'(?P<ad_id>\d+)/comments', CommentViewSet, basename='ad_comments')
#
# urlpatterns = [
#     path('', include(ads_router.urls)),
#     path('', include(comments_router.urls)),
# ]


ads_router = SimpleRouter()
ads_router.register('', AdViewSet)
comments_router = SimpleRouter()
comments_router.register('', CommentViewSet)

urlpatterns = [
    path('me/', UserAdsListView.as_view(), name='user_ads'),
    path('', include(ads_router.urls)),
    path('<int:ad_pk>/comments/', include(comments_router.urls), name='comments'),
]