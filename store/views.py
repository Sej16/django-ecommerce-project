
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order
from django.db.models import Q
from django.conf import settings



def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        return redirect('products')

    return render(request, 'store/register.html')

@login_required
def checkout(request):
    product_id = request.GET.get('product_id')
    quantity = int(request.POST.get('quantity', 1))

    total = 0
    if product_id:
        product = Product.objects.get(id=product_id)
        total = product.price * quantity

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')

        Order.objects.create(
            user=request.user,
            total_amount=total,
            payment_method=payment_method,
            payment_status='Pending'
        )
        return redirect('order_success')

    return render(request, "store/checkout.html", {
        "product": product,
        "total": product.price
    })

@login_required
def order_success(request):
    return render(request, "store/order_success.html")


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('products')  # ✅ FIXED
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'store/login.html')



def user_logout(request):
    logout(request)
    return redirect('login')


def product_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if category:
        products = products.filter(category=category)

    return render(request, 'store/products.html', {
        'products': products,
        'selected_category': category
    })


