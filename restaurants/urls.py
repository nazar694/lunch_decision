from django.urls import path
from .views import RestaurantCreateView, MenuCreateView, MenuTodayView

urlpatterns = [
    path('restaurants/', RestaurantCreateView.as_view(), name='restaurant_create'),
    path('menus/', MenuCreateView.as_view(), name='menu_create'),
    path('menus/today/', MenuTodayView.as_view(), name='menu_today'),
]