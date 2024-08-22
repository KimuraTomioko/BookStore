from django.urls import path
from .views import *
urlpatterns = [
    path('product/one-filter/', get_one_filter_product, name='get_one_filter_product'),
    path('product/all/', product_list, name='product_list'),
    path('product/more-filter/', get_more_filter_product, name='get_more_filter_product'),
    path('product/all-filter/', product_catalog_with_filter, name='product_filter_page'),
    path('product/create/', create_product, name='create_product'),
    path('product/details/<int:id>/', get_product_by_id, name='about_product'),
    path('product/review/<int:id>', UpdateReview.as_view(), name ='edit_review'),
    path('supplier/', ListSupplier.as_view(), name='supplier_list'),
    path('supplier/create/', CreateSupplier.as_view(), name='supplier_create'),
    path('supplier/detail/<int:pk>/', DetailSupplier.as_view(), name='supplier_detail'),
    path('supplier/update/<int:pk>', UpdateSupplier.as_view(), name = 'supplier_update'),
    path('supplier/delete/<int:pk>', DeleteSupplier.as_view(), name = 'supplier_delete'),
    path('warehouse/add/', AddWarehouse.as_view(), name='add_warehouse'),
    path('order/<int:pk>', OrderDetail.as_view(), name='order_detail')
]