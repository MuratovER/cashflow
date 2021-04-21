from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import Asset, Profile

from .forms import AssetMathForm

from mainsite.forms import SignUpForm, AssetForm

from .services.services import _asset_count,\
                               _form_save, \
                               _user_creations_form_save


@login_required
def home_page(request):
    return render(request, 'mainsite/main_page/home_page.html' )


@login_required
def asset_list(request):
    assets = Asset.objects.all().order_by('asset_name')
    _asset_count(assets)
    context = {'assets': assets}
    return render(request, 'mainsite/input/asset_list.html', context)


@login_required
def new_asset_page(request):

    if request.method == 'POST':
        _form_save(AssetForm(request.POST), 'asset_list')

    form = AssetForm(request.POST)
    context = {'form': form}
    return render(request, 'mainsite/input/new_asset.html', context)


def signup(request):
    if request.method == 'POST':
        _user_creations_form_save(SignUpForm(request.POST), request)
        return redirect('home_page')
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})
