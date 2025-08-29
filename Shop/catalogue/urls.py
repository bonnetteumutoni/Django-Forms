from django.urls import path
from .views import list_products
from .views import product_detail
from .views import create_product
from .views import add_to_cart
from .views import cart_detail
from .views import delete_cart

urlpatterns=[
    path('products/',list_products,name='product_list'),
    path('products/<int:id>/',product_detail,name='product_detail'),
    path('products/upload/',create_product,name='create_product'),
    path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('delete_cart/<int:id>/', delete_cart, name='delete_cart'),
] 