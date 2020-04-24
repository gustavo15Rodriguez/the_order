from django.urls import path

from apps.product import views

urlpatterns = [
    path('create_product/', views.CreateProduct.as_view(), name='create_product'),
    path('list_product/', views.ListProduct.as_view(), name='list_product'),
    path('update_product/', views.UpdateProduct.as_view(), name='update_product'),
    path('delete_product/', views.DeleteProduct.as_view(), name='delete_product'),
]
