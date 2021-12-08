from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Products(models.Model):
    # User model is created by Django. Instead of creating our own User model, we can simply use Django's user model.
    # the following line create a ForeignKey in your table
    # Since each user can have many todos, 1-to-many relationship is needed.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_point = models.IntegerField(null=True, blank=True)
    sent_text = models.BooleanField(default=False)
    product_url = models.TextField(null=True, blank=True)
    product_img = models.CharField(max_length=200, null=True, blank=True)
    alert = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.product_name
