from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def contato(request):
    pagina = ('<body bgcolor="#FF8DC"><h1>python</h1><p>sarahcris@gmail.com</h1>')
    return HttpResponse(pagina)
