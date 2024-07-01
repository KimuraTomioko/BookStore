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
    pass

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    pass

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass

@admin.register(Pos_parametr)
class AdminPos_parametr(admin.ModelAdmin):
    pass

@admin.register(Pos_order)
class AdminPos_order(admin.ModelAdmin):
    pass

@admin.register(Manufacturer)
class AdminManufacturer(admin.ModelAdmin):
    pass

@admin.register(Pos_supply)
class AdminPos_supply(admin.ModelAdmin):
    pass

@admin.register(Warehouse)
class AdminWarehouse(admin.ModelAdmin):
    pass

@admin.register(Inventory)
class AdminInventory(admin.ModelAdmin):
    pass

@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    pass

@admin.register(Discount)
class AdminDiscount(admin.ModelAdmin):
    pass

@admin.register(Shipment)
class AdminShipment(admin.ModelAdmin):
    pass

@admin.register(Return)
class AdminReturn(admin.ModelAdmin):
    pass