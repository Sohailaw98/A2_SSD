from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='MSbin-home'),
    path('about/', views.about, name='MSbin-about'),
]
