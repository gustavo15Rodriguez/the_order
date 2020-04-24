from django import forms
from apps.food_truck.models import FoodTruck


class FoodTruckForm(forms.ModelForm):
    class Meta:
        model = FoodTruck

        fields = "__all__"

        labels = {
            'name': 'Nombre del restaurante',
            'logo': 'Logo',
            'products': 'Productos',
        }

    def __init__(self, *args, **kwargs):
        super(FoodTruckForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
