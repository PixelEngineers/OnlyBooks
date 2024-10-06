from django.urls import path
from . import views

urlpatterns=[
    path('', views.landingPage, name='landing-page'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
]