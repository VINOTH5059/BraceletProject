from django.shortcuts import render, redirect
from django.contrib import messages

def Home(request):
    # Just render home page (no model data)
    return render(request, 'shop/home.html')

def category(request):
    # Render category page without data
    return render(request, 'shop/category.html')

def product(request):
    # Render product page without data
    return render(request, 'shop/product.html')

def productDetails(request, id):
    # Render product details page without data
    return render(request, 'shop/product_details.html')
def cart(request):
    # your cart logic here
    return render(request, 'shop/cart.html')



# from django.shortcuts import render,redirect
# from .models import *
# from django.contrib import messages
# from shop.form import CustomerUserForm
# from django.contrib.auth import  authenticate,login,logout

# def Home(request):
#     products=Product.objects.filter(status=0) 
#     return render(request,'shop/home.html',{"products":products})

# def Register(request):
#     form=CustomerUserForm()
#     if request.method=='POST':
#         form=CustomerUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Register Success you can Log in Now")
#             return redirect('/login')
#     return render(request,'shop/register.html' ,{'form':form})
# def login_page(request):
#     if request.method=="POST":
#         name=request.POST.get('username')
#         pwd=request.POST.get('password')
#         user=authenticate(request,username=name,password=pwd)
#         if user is not None:
#             login(request,user)
#             messages.success(request,"Logged in Successfully")
#             redirect('/')
#         else:
#             messages.error(request,"invalid User Name or Password")
#             return redirect('/login')
#     return render(request,'shop/login.html')

# def logout_page(request):
#     if request.user.is_authenticated:
#         logout(request)
#         messages.success(request,"Logged out Successfully")
#         return redirect("/")
# def category(request):
#     categorys=Category.objects.filter(status=0)
#     return render(request,'shop/category.html',{"categorys":categorys})
# def product(request):
#     products=Product.objects.filter(status=0)   
#     return render(request,'shop/product.html',{"products":products})
# def productDetails(request, id):
    try:
        product_detail = Product.objects.get(id=id, status=0)
        return render(request, 'shop/product_details.html', {"products_details": product_detail})
    except Product.DoesNotExist:
        messages.error(request, "No such product found")
        return redirect('product')

# def productDetails(request, id):
#     try:
#         product_detail = Product.objects.get(id=id, status=0)
#     except Product.DoesNotExist:
#         messages.error(request, "No such product found")
#         return redirect('product')
#     return render(request, 'shop/product_details.html', {"products_details": product_detail})

# def productDetails(request, pname):
#     if Product.objects.filter(name=pname, status=0).exists():
#         product_detail = Product.objects.get(name=pname, status=0)
#         return render(request, 'shop/product_details.html', {"products_details": product_detail})
#     else:
#         messages.error(request, "No such product found")
#         return redirect('product')
