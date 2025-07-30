from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    
class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    picture = models.URLField(max_length=500, 
        default='https://th.bing.com/th/id/OIP.aULahN1LnhlTmcuM_DptkAHaE9?w=215&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7')
    cuisine = models.CharField(max_length=200)
    rating = models.FloatField()

class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="items")
    
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    vegeterian = models.BooleanField(default=True)
    picture = models.URLField(max_length=500, 
        default='https://th.bing.com/th/id/OIP.aULahN1LnhlTmcuM_DptkAHaE9?w=215&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7')
    
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="cart")
    items = models.ManyToManyField("Item", related_name="carts")
    
    def total_price(self):
        return sum(item.price for item in self.items.all())