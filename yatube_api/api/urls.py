from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='Post')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='Comment')
router.register('groups', GroupViewSet, basename='Group')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token, name='url_api_token')
]
