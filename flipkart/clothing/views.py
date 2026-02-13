from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def shirt(request):
    return render(request,'shirt.html')

def jeans(request):
    return render(request,'jeans.html')

def tshirt(request):
    return render(request,'tshirt.html')

def shoes(request):
    return render(request,'shoes.html')
