from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('deskripsi/', views.deskripsi, name='deskripsi'),
    path('profile/', views.profile, name='profile'),
    path('riwayat/', views.riwayat, name='riwayat'),
]
