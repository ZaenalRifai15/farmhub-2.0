from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('app/', include('app.urls', namespace='app')),
    path('', views.index),
    path('admin/', admin.site.urls),
]
