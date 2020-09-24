from django.db import models

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
        return self.name
    