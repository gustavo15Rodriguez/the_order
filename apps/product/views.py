from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.product.forms import ProductForm
from apps.product.models import Product


class CreateProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/form_product.html'
    # success_url = reverse_lazy('product_list')


class ListProduct(ListView):
    model = Product
    template_name = 'product/list_product.html'


class DeleteProduct(DeleteView):
    model = Product
    form_class = ProductForm
    template_name = 'product/delete_product.html'
    # success_url = reverse_lazy('product_list')


class UpdateProduct(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/form_product.html'
    # success_url = reverse_lazy('product_list')