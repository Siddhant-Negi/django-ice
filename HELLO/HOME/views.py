from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from HOME.models import Contact,Transaction
from django.contrib import messages
def index(request):
    context={
        "var1":"anand is great",
        "var2":"ankit is great"
    }
    messages.success(request,"delicious ice-creams waiting for you")
    return render(request, 'index.html', context)
    #return HttpResponse("I am homepage")
def details(request):
    return render(request, 'details.html')
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("I am about Page")

def services(request):
    return render(request, 'service.html')
    #return HttpResponse("I am service page")
    
def contacts(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Responese hase been Recorded!!!!')
        
    return render(request, 'contact.html')
    #return HttpResponse("I am contacts page")
# Create your views here.
def order(request):
    Name=request.POST.get('name')
    email=request.POST.get('Email')
    Address=request.POST.get('Address')
    city=request.POST.get('city')
    state=request.POST.get('state')
    zi=request.POST.get('zip')
    flavour=request.POST.get('Flavour')
    Price=request.POST.get('Price')
    Qty=request.POST.get('Qty')
    amount=request.POST.get('Amount')
    Payment=request.POST.get('Payment')
    if(Payment=="COD"):
        order=Transaction(Name=Name,email=email,address=Address,city=city,state=state,zipp=zi, date=datetime.today(),Flavour=flavour,Price=Price,Qty=Qty,Amount=amount,Payment=Payment)
        order.save()
        return render(request, 'order_sucess.html')
    else:
        details={"Name":Name,"email":email,"address":Address,"city":city,"state":state,"zipp":zi,"Flavour":flavour,"Price":Price,"Qty":Qty,"Amount":amount,"Payment":Payment}
        return render(request,'payment.html',details)

def cart(request):
    Product=request.GET.get('Product')
    price=request.GET.get('price')
    piece=request.GET.get('piece')
    amount=int(price)*int(piece)
    return render(request,'details.html',{"amount":amount,"price":price,"piece":piece,"product":Product})
def order_success(request):
    Name=request.POST.get('name')
    email=request.POST.get('Email')
    Address=request.POST.get('Address')
    city=request.POST.get('city')
    state=request.POST.get('state')
    zi=request.POST.get('zip')
    flavour=request.POST.get('Flavour')
    Price=request.POST.get('Price')
    Qty=request.POST.get('Qty')
    amount=request.POST.get('Amount')
    Payment=request.POST.get('Payment')
    order=Transaction(Name=Name,email=email,address=Address,city=city,state=state,zipp=zi, date=datetime.today(),Flavour=flavour,Price=Price,Qty=Qty,Amount=amount,Payment=Payment)
    order.save()
    return render(request, 'order_sucess.html')
