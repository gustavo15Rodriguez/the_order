from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.food_truck.forms import FoodTruckForm
from apps.food_truck.models import FoodTruck


class CreateFoodTruck(CreateView):
    model = FoodTruck
    form_class = FoodTruckForm
    template_name = 'food_truck/form_food_truck.html'
    # success_url = reverse_lazy('list_food_truck')


class ListFoodTruck(ListView):
    model = FoodTruck
    template_name = 'food_truck/list_food_truck.html'


class DeleteFoodTruck(DeleteView):
    model = FoodTruck
    form_class = FoodTruckForm
    template_name = 'food_truck/delete_food_truck.html'
    # success_url = reverse_lazy('list_food_truck')


class UpdateFoodTruck(UpdateView):
    model = FoodTruck
    form_class = FoodTruckForm
    template_name = 'food_truck/form_food_truck.html'
    # success_url = reverse_lazy('list_food_truck')
