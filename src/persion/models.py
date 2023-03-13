from django.urls import reverse
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=50)
    sumary = models.TextField(blank=True, null=False)
    featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("detail-product", kwargs={"id": self.id})
