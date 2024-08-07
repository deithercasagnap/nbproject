from django import forms
from myapp.models import ProductForm

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductForm
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'