from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Profile(models.Model):
    '''
    таблица профиля с именем фамилией почтой и краткой биографией
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    def __str__(self):
        return self.user.username    


class Asset(models.Model):


    user = Profile.user
    asset_name = models.CharField(max_length=100, blank=True)
    buy_price = models.FloatField(default=0)
    modified_buy_price = models.FloatField(default=0)
    count = models.PositiveIntegerField(default=1)


    def price(self):
        total_price = buy_price*count
        return float(total_price)


    def percent_changing(self):
        percent = ((modified_buy_price - buy_price)/modified_buy_price)*100
  
        return percent


    def __str__(self):
        return self.asset_name