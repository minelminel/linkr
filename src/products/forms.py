from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your Title"}))
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                                attrs={
                                    "class":"new-class-name",
                                    "id":"my-id-for-text-area",
                                    "rows":20,
                                    "cols":50
                                }
                            )
                        )
    price       = forms.DecimalField(initial=199.99)