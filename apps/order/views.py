from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from apps.order.forms import OrderForm
from apps.order.models import Order


class CreateOrder(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/form_order.html'
    success_url = reverse_lazy('list_order')


class ListOrder(ListView):
    model = Order
    template_name = 'order/list_order.html'
