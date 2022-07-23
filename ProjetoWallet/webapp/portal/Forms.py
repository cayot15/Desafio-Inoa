from django import forms

from portal.models import Stock
periodo_de_checagem=[('1m','1m'),('2m','2m'),('5m','5m'),('15m','15m'),('30m','30m'),('60m','60m'),('90m','90m')]
#Formulário para adicionar e editar objeto do card
class StockForms(forms.ModelForm):
    class Meta:
        model = Stock
        exclude = ('lastprice',)

        widgets = {'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
                   'ticker': forms.TextInput(attrs={'class': 'form-control'}),
                   'precomax': forms.TextInput(attrs={'class': 'form-control'}),
                   'precomin': forms.TextInput(attrs={'class': 'form-control'}),
                   'frequencia':forms.Select(choices=periodo_de_checagem,attrs={'class': 'form-check-control'})
                   }
