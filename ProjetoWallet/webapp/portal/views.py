# from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from portal.Forms import StockForms
from portal.models import Stock
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from alpha_vantage.timeseries import TimeSeries

def email(html_content):
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives('ALERTA DE PREÇO', text_content, settings.EMAIL_HOST_USER, ['cayoboladao@gmail.com'])
    email.attach_alternative(html_content, 'text/html')
    email.send()


def home(request):
    stocks = Stock.objects.all()
    context = {'stocks': stocks}
    # OBTER O VALOR DAS AÇÕES
    for stock in stocks:
        ts = TimeSeries(key='0WC0DY1J9IV53XEM', output_format='pandas')
        data, meta_data = ts.get_daily(symbol=f'{stock.ticker}', outputsize='full')
        close_data = data['4. close']
        open_data = data['1. open']
        open_price = open_data[0]
        last_price = close_data[0]
        stock.lastprice = last_price
        # ENVIANDO ALERTA POR EMAIL
        if stock.precomax < stock.lastprice:
            html_content = render_to_string('portal/Emails.html', {'preço': f'{stock.precomax}', 'buyorsell': 'VENDA', 'nome': f'{stock.nome}', 'UPORDOWN': 'ABAIXO'})
            email(html_content)
        if stock.precomin > stock.lastprice:
            html_content = render_to_string('portal/Emails.html', {'preço': f'{stock.precomax}', 'buyorsell': 'VENDA', 'nome': f'{stock.nome}', 'UPORDOWN': 'ACIMA'})
            email(html_content)
        if (open_price < stock.precomin or open_price > stock.precomax) and (stock.lastprice > stock.precomin and stock.lastprice < stock.precomax):
            html_content = render_to_string('portal/Emails.html',{'preço': f'{stock.precomax}', 'buyorsell': 'COMPRA','nome': f'{stock.nome}','UPORDOWN':'ABAIXO'})
            email(html_content)
    return render(request, 'portal/home.html', context)


def home_add(request):
    form = StockForms(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}

    return render(request, 'portal/home_add.html', context)


def home_delete(request, stock_pk):
    stock = Stock.objects.get(pk=stock_pk)
    stock.delete()
    return redirect('home')

"""
def envia_email(request):
    html_content = render_to_string('portal/Emails.html', {'preço': '220'})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives('ALERTA DE PREÇO', text_content, settings.EMAIL_HOST_USER, ['cayoboladao@gmail.com'])
    email.attach_alternative(html_content, 'text/html')
    email.send()
    return HttpResponse('olá')
"""