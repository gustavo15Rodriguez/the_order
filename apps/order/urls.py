from django.urls import path

from apps.order import views

urlpatterns = [
    path('create_order/', views.CreateOrder.as_view(), name='create_order'),
    path('list_order/', views.ListOrder.as_view(), name='list_order'),
]
