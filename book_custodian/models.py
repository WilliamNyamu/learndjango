from django.db import models

# Create your models here.
class Custodians(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    department = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, a {self.age} years old works in the {self.department} department for {self.salary} per month"
    

    
