from django.shortcuts import render, redirect
from mainsite.forms import SignUpForm, AssetForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from .models import Asset, Profile
from .forms import AssetMathForm
from django.contrib.auth.decorators import login_required


@login_required
def home_page(request):
    return render(request, 'mainsite/main_page/home_page.html', )


@login_required
def asset_list(request):
    
    def fixed(number, digits):
        return f"{number:.{digits}f}"  

    assets = Asset.objects.all().order_by('asset_name') 

    for asset in assets:
        buy_price = asset.buy_price
        modified_buy_price = asset.modified_buy_price
        asset.cost_before = buy_price*asset.count

        if asset.modified_buy_price:
            asset.cost_after = modified_buy_price*asset.count
        else:
            asset.cost_after = asset.cost_before

        if asset.modified_buy_price:
            growth_price = ((modified_buy_price-buy_price)/buy_price)*100
            asset.growth = fixed(growth_price, 2)

    
    context = {'assets': assets} 
    return render(request, 'mainsite/input/asset_list.html', context )

def asset_counts(request):
    asset = Asset.objects.all()
    

    context = {'growth_percantage': growth_percantage}

    print('growth_percantage')
    return render(request, 'mainsite/input/asset_list.html',context)

@login_required
def new_asset_page(request):

    
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_list')

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