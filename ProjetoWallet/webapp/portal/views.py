from django.shortcuts import render

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
def Stocks(request):
    return render(request, 'portal/Stocks.html')
def Closeprice(request):
    return render(request, 'portal/Closeprice.html')