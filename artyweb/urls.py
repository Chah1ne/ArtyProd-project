from django.urls import include, path

from . import views


urlpatterns = [	
    
        path('services/', views.services, name='services'),
        path('',views.welcome, name='welcome'),
        path('projet/', views.projet, name='projet'),
        path('services/<int:service_id>/delete/', views.delete_service, name='delete_service'),
        path('services/<int:service_id>/edit/', views.edit_service, name='edit_service'),
        path('add_service/', views.add_service, name='add_service'),
        path('contact/', views.contact, name='contact'),
        path('personnel/<int:equipe_id>/', views.personnel, name='personnel'),
        path('personnel/add/', views.add_personnel, name='add_personnel'),
        path('personnel/<int:personnel_id>/edit/', views.edit_personnel, name='edit_personnel'),
        path('personnel/<int:personnel_id>/delete/', views.delete_personnel, name='delete_personnel'),
        path('equipe/',views.equipe, name = 'equipe'),
        path('equipe/', views.equipe, name='equipe'),
        path('add_equipe/', views.add_equipe, name='add_equipe'),
        path('equipes/<int:equipe_id>/edit/', views.edit_equipe, name='edit_equipe'),
        path('equipes/<int:equipe_id>/delete/', views.delete_equipe, name='delete_equipe'),
        
    ]
