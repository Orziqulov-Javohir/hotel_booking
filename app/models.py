from django.db import models


# Create your models here.

class order(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=12)
    message = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name} {self.phone}"
    
    class Meta:
        verbose_name_plural = "orders"