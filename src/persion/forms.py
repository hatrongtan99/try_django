from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={
        "placeholder": "your title",
    }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder": "your description"
    }))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = ["title", "description", "price"]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "your title",
    }))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "placeholder": "abc"
        }
    ))
    price = forms.DecimalField(decimal_places=2, max_digits=1000, initial=100)
