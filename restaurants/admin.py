from django.contrib import admin

from restaurants.models import Restaurant, Menu


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', )


class MenuAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'day', 'menu')


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)
