from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField()
    description = models.TextField(blank=True)
    api_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    products = models.ManyToManyField(Product)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title