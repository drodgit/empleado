from django import forms

class NewDepartametoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    shortname = forms.CharField(max_length=20)