from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.edit import FormView

from applications.persona.models import Empleado

from .models import Departamento

from .forms import NewDepartametoForm
# Create your views here.


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'departamento'

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartametoForm
    success_url = '/'

    def form_valid(self, form):
        print('========estamos en el form valid=============')

        depa = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['shortname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depa
        )
        return super(NewDepartamentoView, self).form_valid(form)
