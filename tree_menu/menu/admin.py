from django.contrib import admin
from .models import MenuItem

# Register your models here.

admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "menu", "parent", "url", "order")

admin.site.register(MenuItem, MenuItemAdmin)
