from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('register/', views.register, name='register'),
    
    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),

    # Books
    path('books/', views.book_list, name='books'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),

    # Cart
    path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:cart_item_id>/<str:action>/', views.update_cart, name='update_cart'),
    path('cart/increment/<int:item_id>/', views.increment_cart, name='increment_cart'),
    path('cart/decrement/<int:item_id>/', views.decrement_cart, name='decrement_cart'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
