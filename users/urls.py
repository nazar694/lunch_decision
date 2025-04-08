from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import EmployeeCreateView

urlpatterns = [
    path('user/registration/', EmployeeCreateView.as_view(), name='employee_create'),
    path('user/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]