from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (SignUpAPI, UserViewSet,
                    UserDetail, YaMDbTokenObtainPairView)

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('users', UserViewSet, basename='user')

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
