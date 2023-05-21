from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from artyweb.models import Service,Personnel,Equipe

   
class PersonnelForm(forms.ModelForm):
    equipe = forms.ModelChoiceField(queryset=Equipe.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Personnel
        fields = ['nom', 'cv', 'photo','equipe']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'cv': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        } 
        
class EquipForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nom', 'description', 'image']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['nom', 'description', 'image']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
