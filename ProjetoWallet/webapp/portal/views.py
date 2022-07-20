from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from portal.Forms import StockForms
from portal.models import Stock
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def home(request):
    stocks = Stock.objects.all()
    context = {'stocks': stocks}
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


def envia_email(request):
    html_content = render_to_string('portal/Emails.html', {'preço': '220'})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives('ALERTA DE PREÇO', text_content, settings.EMAIL_HOST_USER, ['cayoboladao@gmail.com'])
    email.attach_alternative(html_content, 'text/html')
    email.send()
    return HttpResponse('olá')
