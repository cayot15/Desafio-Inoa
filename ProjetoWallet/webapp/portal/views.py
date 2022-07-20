from django.shortcuts import render, redirect

# Create your views here.
from portal.Forms import StockForms
from portal.models import Stock


def home(request):
    stocks=Stock.objects.all()
    context={'stocks':stocks}
    return render(request,'portal/home.html',context)
def home_add(request):
    form=StockForms(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={'form':form}
    return render(request,'portal/home_add.html',context)
def home_delete(request,stock_pk):
    stock=Stock.objects.get(pk=stock_pk)
    stock.delete()
    return redirect('home')

def Stocks(request):
    return render(request, 'portal/Stocks.html')
def Closeprice(request):
    return render(request, 'portal/Closeprice.html')