from django.contrib import admin
from django.urls import path 

from . import views

app_name = 'departamento_app'

urlpatterns = [
    path('new-departamento/',
        views.NewDepartamentoView.as_view(),
        name = 'agregardepartamento'),
    path('list-departamento/',
        views.DepartamentoListView.as_view(),
        name = 'listardepartamento'),
  
]
