# from django.http import HttpResponse
from django.shortcuts import render, redirect
from yahooquery import Ticker
# Create your views here.
from portal.Forms import StockForms
from portal.models import Stock
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


#função que envia um template html como email
def email(html_content):
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives('ALERTA DE PREÇO', text_content, settings.EMAIL_HOST_USER, ['desafioinoa02@gmail.com'])
    email.attach_alternative(html_content, 'text/html')
    email.send()

#view principal home
def home(request):
    stocks = Stock.objects.all()
    context = {'stocks': stocks}
    # OBTER O VALOR DAS AÇÕES
    #for stock in stocks:
    #    abev = Ticker(f'{stock.ticker}')
        # Intraday - 1 minuto
    #    abev = abev.history(period='1d', interval=f'{stock.frequencia}')
    #    close_data = abev['close']
    #    ultimo = len(abev['close'])
    #    last_price = close_data[ultimo - 1]
    #   stock.lastprice = round(last_price, 2)

        # ENVIANDO ALERTA POR EMAIL
    #    if stock.precomax < stock.lastprice:
    #        html_content = render_to_string('portal/Emails.html', {'preço': f'{stock.precomax}', 'buyorsell': 'VENDA', 'nome': f'{stock.nome}', 'UPORDOWN': 'ACIMA'})
    #        email(html_content)
    #    if stock.precomin > stock.lastprice:
    #        html_content = render_to_string('portal/Emails.html', {'preço': f'{stock.precomin}', 'buyorsell': 'COMPRA', 'nome': f'{stock.nome}', 'UPORDOWN': 'ABAIXO'})
    #        email(html_content)

    return render(request, 'portal/home.html', context)



#view para adicionar por formulário
def home_add(request):
    form = StockForms(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'portal/home_add.html', context)

#funçaõ que deleta elemento da nossa tabela
def home_delete(request, stock_pk):
    stock = Stock.objects.get(pk=stock_pk)
    stock.delete()
    return redirect('home')
#VIEW que edita elemento da tabela
def home_edit(request, stock_pk):
    stock = Stock.objects.get(pk=stock_pk)
    form = StockForms(request.POST or None, instance=stock)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'stock':stock.id}
    return render(request, 'portal/home_edit.html', context)
