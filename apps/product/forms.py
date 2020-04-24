from django import forms

from apps.product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = "__all__"

        labels = {
            'name': 'Nombre del producto',
            'quantity': 'Cantidad',
            'image': 'Imagen',
            'price': 'Precio',
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})