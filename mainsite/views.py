from django.shortcuts import render, redirect
from mainsite.forms import SignUpForm, AssetForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from .models import Asset, Profile
from django.contrib.auth.decorators import login_required


@login_required
def home_page(request):
    return render(request, 'mainsite/main_page/home_page.html', )


@login_required
def asset_list(request):

    assets = Asset.objects.all()
    context = {'assets': assets}
    
    return render(request, 'mainsite/input/asset_list.html', context )


@login_required
def new_asset_page(request):


    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()

    form = AssetForm
    context = {'form': form}
    return render(request, 'mainsite/input/new_asset.html',context)



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('home_page')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})