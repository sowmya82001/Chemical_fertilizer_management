from django.contrib import admin # type: ignore
from .models import Fertilizer
from .models import Farmer, Order

admin.site.register(Fertilizer)
admin.site.register(Order)

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

