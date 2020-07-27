from django.contrib import admin
from django.urls import path 


from . import views

app_name = 'persona_app'

urlpatterns = [
    path(
        '',
        views.InicioView.as_view(),
        name ='inicio'
        ),
    path(
        'listar-todo-empleados/',
        views.ListAllEmpleado.as_view(),
        name = 'empleados_all'),
    path(
        'lista-empleados-admin/',
        views.ListaEmpleadoAdmin.as_view(),
        name = 'empleados_admin'),
    path(
        'listar-by-area/<short_name>',
        views.ListByDepartament.as_view(),
        name = 'listarporarea'),
    path('listar-by-job/<job>',views.ListByJob.as_view()),
    path('buscar-empleado',views.ListEmpleadoByKword.as_view()),
    path('lista-habilidades',views.ListHabilidadesEmpleado.as_view()),
    path(
        'detail-empleado/<pk>',
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'),
    path(
        'add-empleado',
        views.EmpleadoCreateView.as_view(),
        name = 'crear'),
    path('success/',views.SuccessView.as_view(), name ='correcto'),
    path(
        'update-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name ='actualizar'),
    path(
        'delete-empleado/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name ='borrar'),
]
