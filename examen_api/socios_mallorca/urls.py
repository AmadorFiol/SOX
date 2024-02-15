from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.options,name=""),
    path('introducir/', views.introducir, name="introducir"),
    path('modificar/', views.modificar, name="modificar"),
    path('mostrar/',views.show, name="mostrar"),
]