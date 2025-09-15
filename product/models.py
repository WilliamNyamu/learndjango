from django.db import models

# Create your models here.

class Product(models.Model):
    GET_CATEGORY = [
        ('TS', 'T-shirt'),
        ('MV', 'Marvin'),
        ('SH', 'Shoe'),
        ('HT', 'HAT'),
        ('HD', 'Hoodie')
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True )
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.CharField(max_length=2, choices=GET_CATEGORY, default='TS')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
    
    
