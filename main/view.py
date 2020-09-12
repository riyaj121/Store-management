from django.shortcuts import render
from django.http import HttpResponse


def signUp_page(request):

    return render(request,'signUp.html')

def view_Product(request):

    return render(request,'product.html')
    
def wrongPath(request):

    return HttpResponse("error 404")

def admin_dbps(request):

    return render(request,'showProduct.py')
