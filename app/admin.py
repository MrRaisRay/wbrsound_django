from django.contrib import admin
from app.models import Client, Manufacturer, Product, Order

# Register your models here.
admin.site.register(Client)
admin.site.register(Product)

@admin.register(Manufacturer)
class OrderAdminPanel(admin.ModelAdmin):
    list_display = ('id', 'name')
    #list_filter = ('state', 'date')
    #search_fields = ('id',)
    #prepopulated_fields = {'date': ('id',)}

@admin.register(Order)
class OrderAdminPanel(admin.ModelAdmin):
    list_display = ('id', 'date', 'user', 'client', 'order_price')
    #list_filter = ('state', 'date')
    #search_fields = ('id',)
    #prepopulated_fields = {'date': ('id',)}