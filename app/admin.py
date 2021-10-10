from django.contrib import admin
from .models import order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "message",)

admin.site.register(order, OrderAdmin)
