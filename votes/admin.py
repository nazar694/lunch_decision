from django.contrib import admin

# Register your models here.
from django.contrib import admin

from votes.models import Vote


class VoteAdmin(admin.ModelAdmin):
    list_display = ('employee', 'restaurant', 'day')


admin.site.register(Vote, VoteAdmin)
