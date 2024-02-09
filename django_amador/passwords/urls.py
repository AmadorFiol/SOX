from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.testing,name=""),
    path('new/', views.new, name='nueva-contraseña'),
    path('change/',views.change, name="cambiar-contraseña"),
    path('delete/', views.delete, name="eliminar-contraseña"),
    path('show/',views.show,name='mostras contraseña'),
]