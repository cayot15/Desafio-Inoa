from django import forms

from portal.models import Stock


class StockForms(forms.ModelForm):
    class Meta:
        model = Stock
        exclude = ('exchange',)

        widgets = {'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
                   'ticker': forms.TextInput(attrs={'class': 'form-control'}),
                   'precomax': forms.TextInput(attrs={'class': 'form-control'}),
                   'precomin': forms.TextInput(attrs={'class': 'form-control'})
                   }
