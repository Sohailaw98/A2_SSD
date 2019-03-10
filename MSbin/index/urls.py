from django.urls import path
from .views import PasteListView, PasteDetailView
from . import views


urlpatterns = [
    path('', PasteListView.as_view(), name='MSbin-home'),
    path('paste/<int:pk>/', PasteDetailView.as_view(), name='paste-detail'),
    path('about/', views.about, name='MSbin-about'),
]
