from django.shortcuts import render, redirect
from mainsite.forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt

def home_page(request):
    return render(request, 'mainsite/main_page/home_page.html', )

def data_input(request):
    return render(request, 'mainsite/input/asset_list.html', )


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