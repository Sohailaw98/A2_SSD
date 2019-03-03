from django.urls import path
from . import views

test

urlpatterns = [
    path('', views.home, name='MSbin-home'),
    path('about/', views.about, name='MSbin-about'),
]
