# from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='books/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.book.price * self.quantity

    def __str__(self):
        return f"{self.book.title} ({self.quantity})"