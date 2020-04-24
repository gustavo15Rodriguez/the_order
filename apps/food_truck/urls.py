from django.urls import path

from apps.food_truck import views

urlpatterns = [
    path('create_food_truck/', views.CreateFoodTruck.as_view(), name='create_food_truck'),
    path('', views.ListFoodTruck.as_view(), name='list_food_truck'),
    path('update_food_truck/', views.UpdateFoodTruck.as_view(), name='update_food_truck'),
    path('delete_food_truck/', views.DeleteFoodTruck.as_view(), name='delete_food_truck'),
]
