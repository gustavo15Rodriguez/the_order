from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.order.forms import OrderForm
from apps.order.models import Order


class CreateOrder(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/form_order.html'
    success_url = reverse_lazy('list_product')