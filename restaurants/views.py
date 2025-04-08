from rest_framework import generics, permissions
from .models import Menu, Restaurant
from .serializers import MenuSerializer, RestaurantSerializer
from django.utils import timezone


class RestaurantCreateView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuTodayView(generics.ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        today = timezone.now().weekday()
        return Menu.objects.filter(day=today)

