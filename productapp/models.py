from django.db import models

class ProductDetails(models.Model):
    productName = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.productName