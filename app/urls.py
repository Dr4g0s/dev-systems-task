from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from app.views import CreateUserAPIView, CreateUserStatusAPIView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create-user/', CreateUserAPIView.as_view(), name='create_user'),
    path('create-status/', CreateUserStatusAPIView.as_view(), name='create_status')
]
