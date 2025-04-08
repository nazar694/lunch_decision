from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from users.serializers import EmployeeRegisterSerializer


class EmployeeCreateView(CreateAPIView):
    model = User
    serializer_class = EmployeeRegisterSerializer
    permission_classes = [permissions.AllowAny]
