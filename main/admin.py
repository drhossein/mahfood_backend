from django.contrib import admin

# Register your models here.

from main.models import *


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'create_date', 'picture', 'image_tag')
    list_filter = ('create_date',)
    search_fields = ('name', 'description', 'create_date')


@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    list_display = ['user', 'food', 'reserve_date', 'type']
    list_filter = ['user', 'food', 'type', 'reserve_date']

admin.site.register(Food, FoodAdmin)
