from django import forms

from apps.order.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = "__all__"

        labels = {
            'username': 'Quien lo solicita',
            'product': 'Nombre del producto',
            'observations': 'Observaciones',
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})