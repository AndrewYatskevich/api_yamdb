from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, SignUpAPI, TitleViewSet, UserDetail,
                    UserViewSet, YaMDbTokenObtainPairView)

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('users', UserViewSet, basename='user')
router_v1.register('categories', CategoryViewSet)
router_v1.register(r'genres', GenreViewSet)
router_v1.register(r'titles', TitleViewSet)
router_v1.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewViewSet, basename='reviews')
router_v1.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
                   r'/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/auth/signup/', SignUpAPI.as_view(), name='signup'),
    path(
        'v1/auth/token/',
        YaMDbTokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path('v1/users/me/', UserDetail.as_view(), name='user_me'),
    path('v1/', include(router_v1.urls))
]
