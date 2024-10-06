from django.urls import path
from . import views

urlpatterns=[
    path('', views.landingPage, name='landing-page'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('books/', views.books, name='books'),
    path('book/<str:book_id>/', views.book, name='book'),
    path('profile/', views.profile, name='profile'),
]