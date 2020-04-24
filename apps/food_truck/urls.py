from django.urls import path

from apps.food_truck import views

urlpatterns = [
    path('', views.CreateFoodTruck.as_view(), name='food_truck_create'),
    path('food_truck_list/', views.CreateFoodTruck.as_view(), name='food_truck_list'),
    path('food_truck_update/', views.CreateFoodTruck.as_view(), name='food_truck_update'),
    path('food_truck_delete/', views.CreateFoodTruck.as_view(), name='food_truck_delete'),
]
