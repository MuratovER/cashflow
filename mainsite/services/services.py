from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from mainsite.forms import SignUpForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.template import RequestContext