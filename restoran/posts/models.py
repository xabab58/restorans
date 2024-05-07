from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()  

class restorans(models.Model):
    name =  models.CharField(max_length=40)
    image = models.ImageField(upload_to='pictures/', blank=True, null=True)
 
    def __str__(self):
        return self.name
    

class person(models.Model):
    name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    patronymic = models.CharField(max_length=10)
    tabel = models.IntegerField(
        default=9999,
        validators=[MaxValueValidator(9999)]
    )
    
    def __str__(self):
        return self.name
    
class Score(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    name_restoran = models.ForeignKey(restorans, on_delete=models.CASCADE)
    dish_name = models.CharField(max_length=100, blank=True, null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])

    def __str__(self):
        return f"{self.name} - {self.name_restoran} - {self.dish_name} - {self.rating}"
