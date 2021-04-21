from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User

from .. import models


def _form_save(form, redirect_url: str):
    """
    Функция сохраняет форму и принимает в значениях ссылку для редиректа и саму форму
    """
    form = form
    if form.is_valid():
        form.save()
        return redirect(redirect_url)


def _user_creations_form_save(form, request_call):
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        # load the profile instance created by the signal
        user.save()
        raw_password = form.cleaned_data.get('password1')
        # login user after signing up
        user = authenticate(username=user.username, password=raw_password)
        login(request_call, user)




def _asset_count(assets) -> None:
    """
        Подсчитывает процент изменения цены и полную стоимость всех активов данного типа
        Получает значение актива из таблицы asset
    """
    def fixed(number, digits):
        return f"{number:.{digits}f}"

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
