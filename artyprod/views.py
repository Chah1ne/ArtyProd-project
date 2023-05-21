from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from artyweb.forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#@user_passes_test(lambda u: u.is_superuser)#, login_url='/error/'
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.urls import reverse
from django.db import transaction
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from artyweb.forms import ContactForm



@login_required
def home(request):
    return render(request, 'artyweb/welcome.html')

#--------------------------------------------REGISTER----------------------------------------------------------------------

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenue, {username} ! Votre compte a été créé avec succès.')
                return redirect('home')
            else:
                messages.error(request, 'Une erreur est survenue lors de la connexion.')
        else:
            messages.error(request, 'Une erreur est survenue lors de la validation du formulaire.')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
