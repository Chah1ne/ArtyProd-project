from django.shortcuts import render
from artyweb.models import Service,Projet
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from .models import Equipe, Projet, Service, Personnel
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from .forms import   ServiceForm, PersonnelForm,EquipForm

from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from .models import Projet, Service
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from .forms import    ServiceForm


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject=request.POST['subject']
        message = request.POST['message']

        message_body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

        send_mail(
            'Contact Form Submission',
            message_body,
            settings.DEFAULT_FROM_EMAIL,
            ['tsouri.chahine@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'artyweb/contact/contact.html', {'success': True})
    return render(request, 'artyweb/contact/contact.html')
def services(request):
    services = Service.objects.all()
    return render(request, 'artyweb/service/services.html', {'services': services})

def projet(request):	
  projets= Projet.objects.all()
  return render( request, 'artyweb/projet/projets.html',{'projets':projets} )

def welcome(request):
  return render( request, 'artyweb/welcome.html' )
 
def personnel(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)
    personnels = Personnel.objects.filter(equipe=equipe)
    context = {
        'equipe': equipe,
        'personnels': personnels,
    }
    return render(request, 'artyweb/personnel/personnel.html', context)

def equipe(request):
    equipe= Equipe.objects.all()
    return render(request, 'artyweb/equipe/equipe.html', {'equipe': equipe})
@require_POST
def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    return redirect('service')

def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'artyweb/service/edit_service.html', {'form': form})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('service')
    else:
        form = ServiceForm()
    return render(request, 'artyweb/service/add_service.html', {'form': form})

def personnel(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)
    personnels = Personnel.objects.filter(equipe=equipe)
    context = {
        'equipe': equipe,
        'personnels': personnels,
    }
    return render(request, 'artyweb/personnel/personnel.html', context)
def equipe(request):
    equipe= Equipe.objects.all()
    return render(request, 'artyweb/equipe/equipe.html', {'equipe': equipe})
def delete_personnel(request, personnel_id):
    personnel = get_object_or_404(Personnel, id=personnel_id)
    personnel.delete()
    return redirect('equipe')

def edit_personnel(request, personnel_id):
    personnel = get_object_or_404(Personnel, id=personnel_id)
    if request.method == 'POST':
        form = PersonnelForm(request.POST, request.FILES, instance=personnel)
        if form.is_valid():
            form.save()
            return redirect('equipe')
    else:
        form = PersonnelForm(instance=personnel)
    return render(request, 'artyweb/personnel/edit_personnel.html', {'form': form})
def add_personnel(request):
    if request.method == 'POST':
        form = PersonnelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('equipe')
    else:
        form = PersonnelForm()
    return render(request, 'artyweb/personnel/add_personnel.html', {'form': form})
def delete_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    equipe.delete()
    return redirect('equipe')

def edit_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    if request.method == 'POST':
        form = EquipForm(request.POST, request.FILES, instance=equipe)
        if form.is_valid():
            form.save()
            return redirect('service')
    else:
        form = EquipForm(instance=equipe)
    return render(request, 'artyweb/equipe/edit_equipe.html', {'form': form})
def add_equipe(request):
    if request.method == 'POST':
        form = EquipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('equipe')
    else:
        form = EquipForm()
    return render(request, 'artyweb/equipe/add_equipe.html', {'form': form})