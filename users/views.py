from django.contrib.auth import logout
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from users.serializers import EmployeeRegisterSerializer


class EmployeeCreateView(CreateAPIView):
    model = User
    serializer_class = EmployeeRegisterSerializer
    permission_classes = [permissions.AllowAny]
