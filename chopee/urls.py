from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home_slash'),
    path('menu/', menu, name='menu'),
    path('sales/', sales, name='sales'),
    path('product/', product, name='product'),
    path('product/create/', product_create, name='create'),
    path('product/update/', product_update, name='update_empty'),
    path('product/update/<int:pk>/', product_update, name='update'),
    path('product/delete/', product_delete, name='delete_empty'),
    path('product/delete/<int:pk>/', product_delete, name='delete'),
    path('product/read/', product_read, name='read_empty'),
    path('product/read/<int:pk>/', product_read, name='read'),
    path('product/list/', product_list, name='list'),
]
