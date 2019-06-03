
# Create your models here.
from django.db import models

# Create your models here.
class NestedModel(models.Model):
    age=models.PositiveIntegerField()
    speciality=models.CharField(max_length=20)

    def __str__(self):
        return self.speciality

class LoginModel(models.Model):

    login = models.ForeignKey(NestedModel, on_delete=models.CASCADE)
    address=models.CharField(max_length=30)
    phone=models.PositiveIntegerField()
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


