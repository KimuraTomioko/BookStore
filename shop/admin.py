from django.contrib import admin
from .models import *

@admin.register(Supplier)
class AdminSupplier(admin.ModelAdmin):
    list_display = ('pk', 'name', 'is_exists')
    list_filter = ('name', 'is_exists')
    list_display_links = ('name', 'is_exists')

@admin.register(Supply)
class AdminSupply(admin.ModelAdmin):
    pass

@admin.register(Parametr)
class AdminParametr(admin.ModelAdmin):
    pass

@admin.register(Tag)
class AdminTab(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('user', 'buyer_lastname', 'buyer_name', 'buyer_surname', 'delivery_address', 'date_create', 'is_packed', 'is_ready')
    list_editable = ('is_packed', 'is_ready')

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'create_date', 'is_exists')
    list_display_links = ('name',)
    list_filter = ('is_exists',)
    list_editable = ('price', 'is_exists')

@admin.register(Pos_parametr)
class AdminPos_parametr(admin.ModelAdmin):
    list_display = ('product', 'parametr', 'value')

@admin.register(Pos_order)
class AdminPos_order(admin.ModelAdmin):
    list_display = ('id', 'product', 'order', 'count', 'discount', 'sum_price_count_display')

    def sum_price_count_display(self, obj):
        return obj.sum_price_count()
    
    sum_price_count_display.short_description = 'Сумма (с учётом скидки)'

    list_display_links = ('order',)

@admin.register(Manufacturer)
class AdminManufacturer(admin.ModelAdmin):
    pass

@admin.register(Pos_supply)
class AdminPos_supply(admin.ModelAdmin):
    list_display = ('product', 'supply', 'count')

@admin.register(Warehouse)
class AdminWarehouse(admin.ModelAdmin):
    pass

@admin.register(Inventory)
class AdminInventory(admin.ModelAdmin):
    pass

@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating')
    list_display_links = ('user',)

@admin.register(Discount)
class AdminDiscount(admin.ModelAdmin):
    pass

@admin.register(Shipment)
class AdminShipment(admin.ModelAdmin):
    pass

@admin.register(Return)
class AdminReturn(admin.ModelAdmin):
    pass