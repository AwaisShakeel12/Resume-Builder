from django.urls import path
from .import views

urlpatterns = [
    path('', views.resume_form, name='resume_form'), 
    path('aspremium', views.aspremium, name='aspremium'), 
    path('blackedition', views.blackedition, name='blackedition'), 
    path('generate_pdf/<int:pk>/', views.generate_pdf, name='generate_pdf'), 
]