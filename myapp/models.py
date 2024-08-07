from django.db import models

# Create your models here.
class ProductForm(models.Model):
    product_code = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    size = models.IntegerField()
    expiration_date = models.DateField()
    file = models.FileField()

    class Meta:
        db_table = 'products'