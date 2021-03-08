from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Asset 



class SignUpForm(UserCreationForm):
    #first_name = forms.CharField(max_length=100, help_text='Last Name')
    #last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    password2 = None

    class Meta:
        model = User
        fields = ('username','email', 'password1')


class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset      
        fields = ('asset_name', 'buy_price','count')  