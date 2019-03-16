from django.urls import path
from .views import PasteListView, PasteDetailView, PasteCreateView, PasteUpdateView, PasteDeleteView
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', PasteListView.as_view(), name='MSbin-home'),
    path('paste/<int:pk>/', PasteDetailView.as_view(), name='paste-detail'),
    path('paste/new/', PasteCreateView.as_view(), name='paste-create'),
    path('paste/<int:pk>/update', PasteUpdateView.as_view(), name='paste-update'),
    path('paste/<int:pk>/delete', PasteDeleteView.as_view(), name='paste-delete'),
    path('about/', views.about, name='MSbin-about'),
    path('paste/', include('shortener.urls')),

]
