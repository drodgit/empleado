from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView )

from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.

class InicioView(TemplateView):
    """ vista que carga la pagina de inicio """

    template_name = 'inicio.html'

class ListAllEmpleado(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    context_object_name='empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        print(palabra_clave)
        return lista

class ListaEmpleadoAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name='empleados'
    model = Empleado



class ListByDepartament(ListView):
    template_name = 'persona/list_by_departament.html'
    
    def get_queryset(self):
        area = self.kwargs['short_name']
        lista = Empleado.objects.filter(
         departamento__short_name = area
    )
        return lista


class ListByJob(ListView):
    template_name = 'persona/list_by_job.html'
    
    def get_queryset(self):
        tarea = self.kwargs['job']
        lista = Empleado.objects.filter(
            job = tarea
    )
        return lista


class ListEmpleadoByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/list_habilidades_empleado.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        id_clave = self.request.GET.get("kid",6)
        empleado = Empleado.objects.get(id = id_clave)
        return empleado.habilidades.all()



class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'persona/detail_empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context
    


class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')


    def form_valid(self, form):
        empleado = form.save(commit= False)
        empleado.full_name = empleado.first_name+' '+empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)



class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = ['first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades'
        ]
    success_url = reverse_lazy('persona_app:empleados_admin')


   
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"

    success_url = reverse_lazy('persona_app:empleados_admin')
