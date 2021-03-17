from django.db import models


class Customer(models.Model):
    name = models.CharField("Customer Name ", max_length=200, null=True)
    phone = models.CharField("Phone Number ", max_length=50, null=True)
    email = models.CharField("Email ", max_length=30, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door')
    )

    name = models.CharField("Product Name ", max_length=200, null=True)
    price = models.FloatField("Price", null=True)
    category = models.CharField("Category ", max_length=30, null=True)
    description = models.CharField("Description ", max_length=250, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )

    # customer
    # product
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField("Status ", max_length=250, null=True, choices=STATUS)
