from django.shortcuts import render

from django.views.generic import (
    TemplateView, ListView, CreateView )

#import models

from .models import Prueba

from .forms import PruebaForm

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class ResumenFoundationView(TemplateView):
    template_name = 'home/Resumen_Foundation.html'




class PruebaListView(ListView):
    template_name = 'home/lista.html'
    context_object_name = 'listaNumeros'
    queryset = ['1','10','30']

class ListarPrueba(ListView):
    template_name = "home/listaprueba.html"
    model = Prueba
    context_object_name = 'lista'




class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'