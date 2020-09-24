from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class login(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class game_data(models.Model):
    user_name = models.CharField(max_length=50, null=True)
    bingo1 = models.ImageField(upload_to='bingo', null=True)
    bingo2 = models.ImageField(upload_to='bingo', null=True)
    bingo3 = models.ImageField(upload_to='bingo', null=True)
    bingo4 = models.ImageField(upload_to='bingo', null=True)
    bingo5 = models.ImageField(upload_to='bingo', null=True)
    bingo6 = models.ImageField(upload_to='bingo', null=True)
    bingo7 = models.ImageField(upload_to='bingo', null=True)
    bingo8 = models.ImageField(upload_to='bingo', null=True)
    bingo9 = models.ImageField(upload_to='bingo', null=True)

    def __str__(self):
        return self.user_name

class Bangkoker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bangkoker')
    bingo1 = models.ImageField(upload_to='bingo', null=True)
    bingo2 = models.ImageField(upload_to='bingo', null=True)
    bingo3 = models.ImageField(upload_to='bingo', null=True)
    bingo4 = models.ImageField(upload_to='bingo', null=True)
    bingo5 = models.ImageField(upload_to='bingo', null=True)
    bingo6 = models.ImageField(upload_to='bingo', null=True)
    bingo7 = models.ImageField(upload_to='bingo', null=True)
    bingo8 = models.ImageField(upload_to='bingo', null=True)
    bingo9 = models.ImageField(upload_to='bingo', null=True)
    # Add image data
    # bingo1 = 
    # bingo2 = 