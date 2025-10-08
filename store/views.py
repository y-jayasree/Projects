# from django.shortcuts import render
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login as auth_login  # rename to avoid conflict

# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             auth_login(request, user)  # logs in the user
#             return redirect('index')  # redirect to homepage
#         else:
#             return render(request, 'login.html', {'error': 'Invalid credentials'})
#     return render(request, 'login.html')


# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login as auth_login

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)  # auto login after register
#             return redirect('index')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .models import Book, CartItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib import messages
from .models import Book  
# Home page view
# def index(request):
#     return render(request, 'index.html')  # Make sure you have index.html in templates

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # auto login after register
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Other views you already have
def cart(request):
    return render(request, 'cart.html')

# def checkout(request):
#     return render(request, 'checkout.html')

# def book(request):
#     return render(request, 'book.html')
def checkout(request):
    if request.method == 'POST':
        # You can access form data like this:
        name = request.POST.get('name')
        address = request.POST.get('address')
        card = request.POST.get('card')
        if not name or not address or not card:
            messages.error(request, "Please fill in all fields!")
        else:
            messages.success(request, f"Payment processed for {name}!")
        # For now, just show a confirmation message
        message = f"Payment processed for {name}!"
        return render(request, 'checkout.html', {'message': message})
    return render(request, 'checkout.html')
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in items)
    return render(request, 'cart.html', {'items': items, 'total': total})
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})

@login_required
def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')
@login_required
def update_cart(request, cart_item_id, action):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    
    if action == 'increment':
        cart_item.quantity += 1
        cart_item.save()
    elif action == 'decrement':
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()  # Remove item if quantity goes to 0
    return redirect('cart')
def book_detail(request, book_id):
    # Get the specific book or 404 if not found
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})
def increment_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect('cart')

def decrement_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()  # remove if quantity reaches 0
    return redirect('cart')
# views.py
def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})



