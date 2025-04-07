from datetime import date
from django.db import models # type: ignore

class Farmer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class SoilCropDetail(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    soil_type = models.CharField(max_length=100)
    crop_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.soil_type} - {self.crop_name}"

class Fertilizer(models.Model):
    name = models.CharField(max_length=255)
    composition = models.CharField(max_length=255, default="N/A")  # Add default value
    soil_type = models.CharField(max_length=255, default="General")  # Add this line
    crop_name = models.CharField(max_length=255, default="Unknown")  # Change "Unknown" to any default value you prefer

    def __str__(self):
        return self.name



class Inventory(models.Model):
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    stock_level = models.IntegerField()

    def __str__(self):
        return f"{self.fertilizer.name} - {self.stock_level} in stock"

class Order(models.Model):
    FERTILIZER_CHOICES = [
        ('Urea', 'Urea'),
        ('DAP', 'DAP'),
        ('Potash', 'Potash'),
        ('NPK', 'NPK'),
    ]

    PAYMENT_CHOICES = [
        ('Cash on Delivery', 'Cash on Delivery'),
        ('Online Payment', 'Online Payment'),
        ('Bank Transfer', 'Bank Transfer'),
    ]

    fertilizer_name = models.CharField(max_length=255, default="Unknown")  # Set a default value
    quantity = models.PositiveIntegerField()
    address = models.TextField(default="Default Address")

    delivery_date = models.DateField(default=date.today) 
    payment_method = models.CharField(max_length=50, default="Cash")  # Set a default value
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.fertilizer_name}"