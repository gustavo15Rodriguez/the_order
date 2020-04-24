from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from apps.food_truck.forms import FoodTruckForm
from apps.food_truck.models import FoodTruck


class CreateFoodTruck(CreateView):
    model = FoodTruck
    form_class = FoodTruckForm
    template_name = 'food_truck/food_truck_form.html'
    #success_url = reverse_lazy('food_truck_list')


class ListFoodTruck(ListView):
    model = FoodTruck
    template_name = 'food_truck/food_truck_list.html'


class DetailFoodTruck(DetailView):
    model = FoodTruck
    template_name = 'food_truck/food_truck_detail.html'


class UpdateFoodTruck(UpdateView):
    model = FoodTruck
    form_class = FoodTruckForm
    template_name = 'food_truck/food_truck_form.html'
    success_url = reverse_lazy('food_truck_list')
