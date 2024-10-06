from django.urls import path
from . import views

urlpatterns=[
    path('', views.landingPage, name='landing-page'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('books/', views.books, name='books'),
    path('book/<str:book_id>/', views.book, name='book'),
    path('profile/<str:user_id>', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('signup/', views.signup_view, name='signup'),
    path('auth/', views.auth_view, name='auth'),
]