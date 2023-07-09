from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')

def productlist(request):
    return render(request, 'pages/productlist.html')

def productlist_detail(request):
    return render(request, 'pages/product_detail.html')

def brand(request):
    return render(request, 'pages/brand_info.html')
def brand_ph(request):
    return render(request, 'pages/brand_ph.html')
def brand_cs(request):
    return render(request, 'pages/brand_cs.html')
def login(request):
    return render(request, 'pages/login.html')
def login_signup(request):
    return render(request, 'pages/signup.html')

def login_password_reset(request):
    return render(request, 'pages/login_password_reset.html')
