from django.db import models
# python manage.py makemigrations
# python manage.py migrate

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=1000)
    summary = models.TextField() # default='this is cool'